"""CrossRef-based paper fetcher for ACM, IEEE, and other DOI sources."""

import re
import html
import requests
from typing import Optional

from . import BaseFetcher
from ..models import Paper


class CrossRefFetcher(BaseFetcher):
    """Fetcher for papers using CrossRef API (ACM, IEEE, etc.)."""

    CROSSREF_API = "https://api.crossref.org/works/"
    _IMWUT_ISSN = "2474-9567"

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
            f"{self.CROSSREF_API}{doi}",
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
            source_type = "ACM"
        elif "10.1109" in doi:
            default_tag = "IEEE"
            source_type = "IEEE"
        else:
            default_tag = "DOI"
            source_type = "DOI"

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
        # IEEE: https://ieeexplore.ieee.org/document/9878378 (need different handling)
        # DOI: https://doi.org/10.1145/xxx
        # Bare: 10.1145/xxx

        # Try to match DOI pattern
        doi_match = re.search(r'(10\.\d{4,}/[^\s]+)', url)
        if doi_match:
            # Clean up trailing punctuation
            doi = doi_match.group(1).rstrip('.,;:')
            return doi

        # IEEE document ID - need to convert to DOI
        ieee_match = re.search(r'ieeexplore\.ieee\.org/document/(\d+)', url)
        if ieee_match:
            doc_id = ieee_match.group(1)
            # Try to get DOI from IEEE API
            return self._get_ieee_doi(doc_id)

        return None

    def _get_ieee_doi(self, doc_id: str) -> Optional[str]:
        """Get DOI for IEEE document ID."""
        # IEEE provides DOI in their API
        try:
            # Use a simple heuristic - most IEEE DOIs follow this pattern
            # For a more robust solution, we'd need IEEE API access
            # For now, construct a likely DOI
            return f"10.1109/ACCESS.{doc_id}"
        except Exception:
            return None

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
