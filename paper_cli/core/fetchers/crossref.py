"""CrossRef-based paper fetcher for ACM, IEEE, and other DOI sources."""

import re
import html
import requests
from typing import Optional
from urllib.parse import quote

from . import BaseFetcher
from ..models import Paper


class CrossRefFetcher(BaseFetcher):
    """Fetcher for papers using CrossRef API (ACM, IEEE, etc.)."""

    CROSSREF_API = "https://api.crossref.org/works/"
    _IMWUT_ISSN = "2474-9567"
    _DOI_RE = re.compile(r"(10\.\d{4,9}/[^\s\"'<>]+)", re.IGNORECASE)

    def _clean_doi(self, doi: str) -> str:
        """Clean a DOI token extracted from text/URLs."""
        if not doi:
            return ""
        doi = doi.strip()
        # IEEE pages may embed DOI inside URLs with extra query params.
        doi = re.split(r"[&?]", doi, maxsplit=1)[0]
        return doi.rstrip(".,;:")

    def _normalize_title(self, title: str) -> str:
        """Normalize CrossRef titles (strip HTML and collapse whitespace)."""
        if not title:
            return ""
        title = re.sub(r"<[^>]+>", "", title)
        # Crossref sometimes returns escaped entities like "&amp;".
        title = html.unescape(title)
        title = re.sub(r"\s+", " ", title).strip()
        return title

    def _is_imwut(self, data: dict) -> bool:
        """Detect IMWUT (Proceedings of the ACM on IMWUT / UbiComp journal track)."""
        issns = [str(x) for x in (data.get("ISSN") or [])]
        if self._IMWUT_ISSN in issns:
            return True
        container = (data.get("container-title") or [""])[0]
        return "Interactive, Mobile, Wearable and Ubiquitous Technologies" in str(container)

    def _format_imwut_journal_ref(self, data: dict) -> str:
        """Format IMWUT volume/issue string for Source column parentheses."""
        volume = data.get("volume")
        issue = data.get("issue")
        ref = "IMWUT"
        if volume:
            ref += f" Vol {volume}"
        if issue:
            ref += f" Issue {issue}"
        return ref

    def can_handle(self, url: str) -> bool:
        """Check if URL is from ACM, IEEE, or contains a DOI."""
        return bool(
            "dl.acm.org" in url or
            "ieeexplore.ieee.org" in url or
            "doi.org" in url or
            re.match(r'^10\.\d+/', url)  # Bare DOI
        )

    def fetch(self, url: str, custom_tag: Optional[str] = None) -> Paper:
        """Fetch paper metadata from CrossRef API."""
        doi = self._extract_doi(url)
        if not doi:
            raise ValueError(f"Could not extract DOI from: {url}")

        # Fetch from CrossRef
        response = requests.get(
            f"{self.CROSSREF_API}{quote(doi)}",
            headers={"Accept": "application/json"},
            timeout=10
        )

        if response.status_code != 200:
            raise ValueError(f"CrossRef API error: {response.status_code}")

        data = response.json().get("message", {})

        # Extract metadata
        title = self._normalize_title(data.get("title", [""])[0])
        if not title:
            raise ValueError("No title found in CrossRef response")

        authors = self._format_authors(data.get("author", []))
        year = self._extract_year(data)
        date = self._extract_date(data)
        venue = self._extract_venue(data)

        journal_ref = ""
        source = f"{venue} {year}" if venue and year else (venue or str(year) or "")

        # UbiComp papers are published in IMWUT by issue; keep that info in Journal_Ref.
        if self._is_imwut(data):
            source = f"Ubicomp{year % 100:02d}" if year else "Ubicomp"
            journal_ref = self._format_imwut_journal_ref(data)

        # Detect source type for default tag
        if "10.1145" in doi:
            default_tag = "ACM"
        elif "10.1109" in doi:
            default_tag = "IEEE"
        else:
            default_tag = "DOI"

        return Paper(
            source=source,
            title=title.replace('\n', ' '),
            authors=authors,
            doi=doi,
            journal_ref=journal_ref,
            link=f"https://doi.org/{doi}",
            tag=custom_tag if custom_tag else default_tag,
            subjects="",
            additional_info="",
            date=date,
            topic="",
        )

    def _extract_doi(self, url: str) -> Optional[str]:
        """Extract DOI from various URL formats."""
        # ACM: https://dl.acm.org/doi/10.1145/3544548.3581468
        # IEEE: https://ieeexplore.ieee.org/document/9878378
        # DOI: https://doi.org/10.1145/xxx
        # Bare: 10.1145/xxx

        # Try to match DOI pattern anywhere in the input (URLs or bare DOI).
        doi_match = self._DOI_RE.search(url or "")
        if doi_match:
            return self._clean_doi(doi_match.group(1))

        # IEEE document URL: fetch the landing page and parse DOI from metadata.
        if re.search(r"ieeexplore\.ieee\.org/document/\d+", url or ""):
            return self._fetch_ieee_doi(url)

        return None

    def _extract_ieee_doi_from_html(self, html_text: str) -> Optional[str]:
        """Extract DOI from an IEEE Xplore HTML page.

        IEEE pages usually include a standard meta tag: <meta name="citation_doi" ...>
        """
        if not html_text:
            return None

        # Prefer the citation_doi meta tag when present.
        meta = re.search(
            r'<meta[^>]+name=["\']citation_doi["\'][^>]+content=["\']([^"\']+)["\']',
            html_text,
            flags=re.IGNORECASE,
        )
        if meta:
            val = meta.group(1).strip()
            m = self._DOI_RE.search(val)
            return self._clean_doi(m.group(1) if m else val)

        # Fallback: look for a single DOI-looking token in the HTML.
        candidates = {self._clean_doi(m.group(1)) for m in self._DOI_RE.finditer(html_text)}
        if len(candidates) == 1:
            return next(iter(candidates))
        return None

    def _fetch_ieee_doi(self, url: str) -> Optional[str]:
        """Fetch IEEE Xplore page and parse DOI."""
        try:
            resp = requests.get(
                url,
                headers={
                    # Some sites block requests without a UA; keep it simple.
                    "User-Agent": "paper-cli/0.1.0",
                    "Accept": "text/html,application/xhtml+xml",
                },
                timeout=10,
            )
        except requests.RequestException:
            return None

        if resp.status_code != 200:
            return None

        return self._extract_ieee_doi_from_html(resp.text)

    def _format_authors(self, authors: list) -> str:
        """Format CrossRef author list."""
        if not authors:
            return ""

        names = []
        for i, author in enumerate(authors[:3]):
            given = author.get("given", "")
            family = author.get("family", "")
            if given and family:
                names.append(f"{given} {family}")
            elif family:
                names.append(family)

        result = ", ".join(names)
        if len(authors) > 3:
            result += ", et al."
        return result

    def _extract_venue(self, data: dict) -> str:
        """Extract venue/conference name."""
        # Try different fields
        venue = data.get("container-title", [""])[0]
        if not venue:
            venue = data.get("event", {}).get("name", "")
        if not venue:
            venue = data.get("publisher", "")
        return venue

    def _extract_year(self, data: dict) -> Optional[int]:
        """Extract publication year."""
        # Try published-print first, then published-online
        for field in ["published-print", "published-online", "published", "created"]:
            if field in data:
                date_parts = data[field].get("date-parts", [[]])
                if date_parts and date_parts[0]:
                    return date_parts[0][0]
        return None

    def _extract_date(self, data: dict) -> str:
        """Extract date in YYYY.MM format."""
        for field in ["published-print", "published-online", "published", "created"]:
            if field in data:
                date_parts = data[field].get("date-parts", [[]])
                if date_parts and date_parts[0]:
                    parts = date_parts[0]
                    year = parts[0]
                    month = parts[1] if len(parts) > 1 else 1
                    return f"{year}.{month:02d}"
        return ""
