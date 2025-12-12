"""arXiv paper fetcher."""

import re
import arxiv
from typing import Optional

from . import BaseFetcher
from ..models import Paper


class ArxivFetcher(BaseFetcher):
    """Fetcher for arXiv papers."""

    def __init__(self):
        self.client = arxiv.Client(
            page_size=1,
            delay_seconds=3.0,
            num_retries=3
        )

    def can_handle(self, url: str) -> bool:
        """Check if URL is an arXiv link or ID."""
        # Match: arxiv.org/abs/xxx, arxiv:xxx, or bare ID like 2312.00752
        return bool(
            "arxiv.org" in url or
            url.startswith("arxiv:") or
            re.match(r'^\d{4}\.\d{4,5}(v\d+)?$', url)
        )

    def fetch(self, url: str, custom_tag: Optional[str] = None) -> Paper:
        """Fetch paper metadata from arXiv."""
        paper_id = self._extract_id(url)
        search = arxiv.Search(id_list=[paper_id])
        result = next(self.client.results(search), None)

        if not result:
            raise ValueError(f"Paper not found on arXiv: {paper_id}")

        # Format authors
        authors = self._format_authors(result.authors)

        # Extract version
        version = self._extract_version(result.pdf_url)

        # Build source string
        year = result.updated.year
        source = f"arXiv({version}) {year}"

        # Format date
        date = result.updated.strftime('%Y.%m')

        # Categories
        subjects = ", ".join(result.categories)

        return Paper(
            source=source,
            title=result.title.replace('\n', ' '),
            authors=authors,
            doi=result.doi or "",
            journal_ref=result.journal_ref or "",
            link=result.entry_id,
            tag=custom_tag if custom_tag else "arxiv",
            subjects=subjects,
            additional_info=result.comment or "",
            date=date,
            topic="",
        )

    def _extract_id(self, url: str) -> str:
        """Extract arXiv ID from URL or string."""
        # Support: 2403.06201, https://arxiv.org/abs/2403.06201, arxiv:2403.06201
        match = re.search(r'(\d{4}\.\d{4,5})', url)
        if not match:
            raise ValueError(f"Invalid arXiv link or ID: {url}")
        return match.group(1)

    def _format_authors(self, authors: list) -> str:
        """Format author list, max 3 authors."""
        if not authors:
            return ""
        names = [a.name for a in authors[:3]]
        result = ", ".join(names)
        if len(authors) > 3:
            result += ", et al."
        return result

    def _extract_version(self, pdf_url: str) -> str:
        """Extract version number from PDF URL."""
        match = re.search(r'v(\d+)$', pdf_url)
        return f"v{match.group(1)}" if match else "v1"
