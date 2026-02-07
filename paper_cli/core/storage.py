"""CSV storage layer for paper management."""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urlsplit, urlunsplit

import pandas as pd

from .models import Paper
from ..utils.date import date_key


_ARXIV_ID_RE = re.compile(r"(\d{4}\.\d{4,5})(?:v\d+)?", re.IGNORECASE)
_ARXIV_BARE_RE = re.compile(r"^\d{4}\.\d{4,5}(?:v\d+)?$", re.IGNORECASE)
_DOI_RE = re.compile(r"(10\.\d{4,9}/[^\s]+)", re.IGNORECASE)


class PaperStorage:
    """CSV 存储管理，负责论文数据的读写和查询。"""

    FIELDNAMES = [
        "Source",
        "Title",
        "Authors",
        "DOI",
        "Journal_Ref",
        "Link",
        "Tag",
        "Subjects",
        "Additional_Info",
        "Date",
        "Topic",
    ]

    def __init__(self, csv_path: Path):
        self.csv_path = Path(csv_path)

    @staticmethod
    def _extract_arxiv_id(value: str) -> Optional[str]:
        """Extract canonical arXiv id (without version) from an arXiv-like input."""
        if not value:
            return None

        raw = str(value).strip()
        lowered = raw.lower()
        looks_like_arxiv = (
            "arxiv.org" in lowered
            or lowered.startswith("arxiv:")
            or bool(_ARXIV_BARE_RE.fullmatch(raw))
        )
        if not looks_like_arxiv:
            return None

        match = _ARXIV_ID_RE.search(raw)
        return match.group(1) if match else None

    @staticmethod
    def _extract_doi(value: str) -> Optional[str]:
        """Extract and normalize DOI token from free text/URLs."""
        if not value:
            return None

        match = _DOI_RE.search(str(value))
        if not match:
            return None

        doi = match.group(1)
        doi = re.split(r"[&#?]", doi, maxsplit=1)[0]
        doi = doi.lstrip("(<[{\"'")
        doi = doi.rstrip(".,;:)]}>\"'")
        return doi.lower()

    @staticmethod
    def _normalize_link(value: str) -> str:
        """Normalize links for safer duplicate checks without changing semantics."""
        if not value:
            return ""

        raw = str(value).strip()
        if not raw:
            return ""

        parsed = urlsplit(raw)
        if not (parsed.scheme and parsed.netloc):
            return raw

        # Normalize only scheme/host case and trailing slash in path.
        path = parsed.path.rstrip("/")
        return urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), path, parsed.query, parsed.fragment))

    def load_all(self) -> List[Paper]:
        """加载所有论文。"""
        if not self.csv_path.exists():
            return []

        # Keep all columns as strings (the CSV is a pure metadata store).
        # This avoids dtype-related warnings/errors when filling missing values.
        df = pd.read_csv(self.csv_path, dtype=str, keep_default_na=False)
        return [Paper.from_csv_row(row) for _, row in df.iterrows()]

    def add_paper(self, paper: Paper) -> None:
        """添加单篇论文到 CSV。"""
        file_exists = self.csv_path.exists()

        with open(self.csv_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.FIELDNAMES, quoting=csv.QUOTE_ALL)
            if not file_exists:
                writer.writeheader()
            writer.writerow(paper.to_csv_row())

    def exists(self, link: str) -> bool:
        """检查论文是否已存在。

        Notes:
            - arXiv IDs are only extracted/compared when the input looks like an arXiv link/ID.
              (Avoid false positives on ACM DOIs like 10.1145/3706598.3713728.)
            - DOIs are compared against stored DOI fields and DOI-style links.
            - Fallback link matching uses normalized links (trim + URL host/scheme normalization).
        """
        if not link:
            return False

        papers = self.load_all()
        if not papers:
            return False

        input_doi = self._extract_doi(link)
        input_arxiv_id = self._extract_arxiv_id(link)
        normalized_input_link = self._normalize_link(link)

        stored_dois: set[str] = set()
        stored_arxiv_ids: set[str] = set()
        stored_links: set[str] = set()

        for paper in papers:
            if paper.doi:
                doi = self._extract_doi(paper.doi)
                if doi:
                    stored_dois.add(doi)

            if paper.link:
                stored_links.add(self._normalize_link(paper.link))

                link_doi = self._extract_doi(paper.link)
                if link_doi:
                    stored_dois.add(link_doi)

                arxiv_id = self._extract_arxiv_id(paper.link)
                if arxiv_id:
                    stored_arxiv_ids.add(arxiv_id)

        if input_doi and input_doi in stored_dois:
            return True

        if input_arxiv_id and input_arxiv_id in stored_arxiv_ids:
            return True

        return normalized_input_link in stored_links

    def search(
        self,
        query: Optional[str] = None,
        tag: Optional[str] = None,
        author: Optional[str] = None,
        topic: Optional[str] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
    ) -> List[Paper]:
        """
        搜索论文。

        Args:
            query: 关键字搜索（搜索标题、标签、作者）
            tag: 按标签过滤
            author: 按作者过滤
            topic: 按 topic 过滤
            date_from: 起始日期 (YYYY.MM)
            date_to: 截止日期 (YYYY.MM)
        """
        papers = self.load_all()
        results = []

        for paper in papers:
            # 关键字搜索
            if query and not paper.matches_query(query):
                continue

            # 标签过滤
            if tag and tag.lower() not in paper.tag.lower():
                continue

            # 作者过滤
            if author and author.lower() not in paper.authors.lower():
                continue

            # Topic 过滤
            if topic and topic.lower() != paper.topic.lower():
                continue

            # 日期范围过滤
            if date_from or date_to:
                p_key = date_key(paper.date)
                # If a date filter is requested, rows without a valid date are excluded.
                if not p_key:
                    continue

                from_key = date_key(date_from) if date_from else None
                to_key = date_key(date_to) if date_to else None

                if from_key and p_key < from_key:
                    continue
                if to_key and p_key > to_key:
                    continue

            results.append(paper)

        return results

    def get_topics(self) -> Dict[str, int]:
        """获取所有 topics 及其论文数量。"""
        papers = self.load_all()
        topics: Dict[str, int] = {}
        for paper in papers:
            if paper.topic:
                topics[paper.topic] = topics.get(paper.topic, 0) + 1
        return dict(sorted(topics.items(), key=lambda x: -x[1]))

    def get_all_tags(self) -> Dict[str, int]:
        """获取所有标签及其出现次数。"""
        papers = self.load_all()
        tags: Counter = Counter()
        for paper in papers:
            if paper.tag:
                # 分割逗号分隔的标签
                for t in paper.tag.split(","):
                    t = t.strip()
                    if t:
                        tags[t] += 1
        return dict(tags.most_common())

    def count(self) -> int:
        """返回论文总数。"""
        return len(self.load_all())
