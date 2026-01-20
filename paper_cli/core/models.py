"""Paper data model."""

from pydantic import BaseModel
from typing import Optional


class Paper(BaseModel):
    """论文数据模型，对应 papers.csv 的 11 列。"""

    source: str = ""           # 来源 (CHI 2023, arXiv(v1) 2024, etc.)
    title: str = ""            # 标题
    authors: str = ""          # 作者
    doi: str = ""              # DOI
    journal_ref: str = ""      # 期刊引用
    link: str = ""             # 链接
    tag: str = ""              # 标签 (用户自定义)
    subjects: str = ""         # arXiv 分类
    additional_info: str = ""  # 附加信息
    date: str = ""             # 日期 (YYYY.MM)
    topic: str = ""            # 主题分类 (free-form; e.g., Memory/Personalization/MLLM)

    @classmethod
    def from_csv_row(cls, row: dict) -> "Paper":
        """从 CSV 行创建 Paper 对象。"""
        return cls(
            source=row.get("Source", "") or "",
            title=row.get("Title", "") or "",
            authors=row.get("Authors", "") or "",
            doi=row.get("DOI", "") or "",
            journal_ref=row.get("Journal_Ref", "") or "",
            link=row.get("Link", "") or "",
            tag=row.get("Tag", "") or "",
            subjects=row.get("Subjects", "") or "",
            additional_info=row.get("Additional_Info", "") or "",
            date=row.get("Date", "") or "",
            topic=row.get("Topic", "") or "",
        )

    def to_csv_row(self) -> dict:
        """转换为 CSV 行。"""
        return {
            "Source": self.source,
            "Title": self.title,
            "Authors": self.authors,
            "DOI": self.doi,
            "Journal_Ref": self.journal_ref,
            "Link": self.link,
            "Tag": self.tag,
            "Subjects": self.subjects,
            "Additional_Info": self.additional_info,
            "Date": self.date,
            "Topic": self.topic,
        }

    def matches_query(self, query: str) -> bool:
        """检查论文是否匹配关键字查询。"""
        query_lower = query.lower()
        return any([
            query_lower in self.title.lower(),
            query_lower in self.tag.lower(),
            query_lower in self.authors.lower(),
            query_lower in self.subjects.lower(),
        ])
