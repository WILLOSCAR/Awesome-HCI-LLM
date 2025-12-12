"""Paper fetchers for different sources."""

from abc import ABC, abstractmethod
from typing import Optional
import re

from ..models import Paper


class BaseFetcher(ABC):
    """Base class for paper metadata fetchers."""

    @abstractmethod
    def can_handle(self, url: str) -> bool:
        """Check if this fetcher can handle the given URL."""
        pass

    @abstractmethod
    def fetch(self, url: str, custom_tag: Optional[str] = None) -> Paper:
        """Fetch paper metadata from the URL."""
        pass


class FetcherRegistry:
    """Registry for paper fetchers with auto-detection."""

    def __init__(self):
        from .arxiv import ArxivFetcher
        from .crossref import CrossRefFetcher

        self._fetchers = [
            ArxivFetcher(),
            CrossRefFetcher(),
        ]

    def get_fetcher(self, url: str) -> BaseFetcher:
        """Get appropriate fetcher for the given URL."""
        for fetcher in self._fetchers:
            if fetcher.can_handle(url):
                return fetcher
        raise ValueError(f"Unsupported paper source: {url}")

    def detect_source(self, url: str) -> str:
        """Detect the source type from URL."""
        if "arxiv.org" in url or re.match(r'^\d{4}\.\d{4,5}$', url):
            return "arXiv"
        elif "dl.acm.org" in url or "10.1145" in url:
            return "ACM"
        elif "ieeexplore.ieee.org" in url or "10.1109" in url:
            return "IEEE"
        elif re.match(r'^10\.\d+/', url):
            return "DOI"
        else:
            return "Unknown"
