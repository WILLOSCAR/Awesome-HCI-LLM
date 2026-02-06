"""CSV storage layer for paper management."""

import csv
import pandas as pd
from pathlib import Path
from typing import List, Optional, Dict
from collections import Counter
from .models import Paper
from ..utils.date import date_key


class PaperStorage:
    """CSV 存储管理，负责论文数据的读写和查询。"""

    FIELDNAMES = [
        'Source', 'Title', 'Authors', 'DOI', 'Journal_Ref',
        'Link', 'Tag', 'Subjects', 'Additional_Info', 'Date', 'Topic'
    ]

    def __init__(self, csv_path: Path):
        self.csv_path = Path(csv_path)

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

        with open(self.csv_path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.FIELDNAMES, quoting=csv.QUOTE_ALL)
            if not file_exists:
                writer.writeheader()
            writer.writerow(paper.to_csv_row())

    def exists(self, link: str) -> bool:
        """检查论文是否已存在。

        Notes:
            - arXiv IDs are only extracted/compared when the input looks like an arXiv link/ID.
              (Avoid false positives on ACM DOIs like 10.1145/3706598.3713728.)
            - DOIs are compared against stored DOI fields to avoid duplicates across different URLs.
        """
        if not link:
            return False

        import re

        def extract_arxiv_id(s: str) -> Optional[str]:
            if not s:
                return None
            s_stripped = str(s).strip()
            s_lower = s_stripped.lower()
            if (
                "arxiv.org" in s_lower
                or s_lower.startswith("arxiv:")
                or re.fullmatch(r"\d{4}\.\d{4,5}(v\d+)?", s_stripped)
            ):
                m = re.search(r"(\d{4}\.\d{4,5})", s_stripped)
                return m.group(1) if m else None
            return None

        def extract_doi(s: str) -> Optional[str]:
            if not s:
                return None
            m = re.search(r"(10\.\d{4,9}/[^\s]+)", str(s), flags=re.IGNORECASE)
            if not m:
                return None
            doi = m.group(1)
            doi = re.split(r"[&#?]", doi, maxsplit=1)[0]
            doi = doi.lstrip("(<[{\"'")
            doi = doi.rstrip(".,;:)]}>\"'")
            return doi.lower()

        papers = self.load_all()

        # Prefer DOI-based matching when possible.
        link_doi = extract_doi(link)
        if link_doi:
            for paper in papers:
                if paper.doi and paper.doi.strip().lower() == link_doi:
                    return True
                paper_link_doi = extract_doi(paper.link)
                if paper_link_doi and paper_link_doi == link_doi:
                    return True

        # arXiv-based matching (only when the input is arXiv).
        link_arxiv_id = extract_arxiv_id(link)
        if link_arxiv_id:
            for paper in papers:
                paper_arxiv_id = extract_arxiv_id(paper.link)
                if paper_arxiv_id and paper_arxiv_id == link_arxiv_id:
                    return True

        # Fallback: exact link match.
        return any(paper.link == link for paper in papers)

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
                for t in paper.tag.split(','):
                    t = t.strip()
                    if t:
                        tags[t] += 1
        return dict(tags.most_common())

    def count(self) -> int:
        """返回论文总数。"""
        return len(self.load_all())
