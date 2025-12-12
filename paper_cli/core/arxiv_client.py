"""arXiv API client for fetching paper metadata."""

import re
import arxiv
from typing import Optional
from .models import Paper


class ArxivClient:
    """arXiv API 客户端，封装论文元数据获取逻辑。"""

    def __init__(self):
        self.client = arxiv.Client(
            page_size=1,
            delay_seconds=3.0,
            num_retries=3
        )

    def fetch_paper(self, arxiv_link: str, custom_tag: Optional[str] = None) -> Paper:
        """
        从 arXiv 获取论文详情。

        Args:
            arxiv_link: arXiv 链接或论文 ID
            custom_tag: 自定义标签，如果提供则覆盖默认标签

        Returns:
            Paper 对象
        """
        paper_id = self._extract_id(arxiv_link)
        search = arxiv.Search(id_list=[paper_id])
        result = next(self.client.results(search), None)

        if not result:
            raise ValueError(f"Paper not found: {paper_id}")

        # 格式化作者
        authors = self._format_authors(result.authors)

        # 提取版本号
        version = self._extract_version(result.pdf_url)

        # 构建来源字符串
        year = result.updated.year
        source = f"arXiv({version}) {year}"

        # 格式化日期
        date = result.updated.strftime('%Y.%m')

        # 分类
        subjects = ", ".join(result.categories)

        return Paper(
            source=source,
            title=result.title.replace('\n', ' '),  # 去除标题中的换行
            authors=authors,
            doi=result.doi or "",
            journal_ref=result.journal_ref or "",
            link=result.entry_id,
            tag=custom_tag if custom_tag else "arxiv",
            subjects=subjects,
            additional_info=result.comment or "",
            date=date,
            topic="",  # topic 需要用户指定
        )

    def _extract_id(self, link: str) -> str:
        """从链接或 ID 字符串提取 arXiv ID。"""
        # 支持格式: 2403.06201, https://arxiv.org/abs/2403.06201, arxiv:2403.06201
        match = re.search(r'(\d{4}\.\d{4,5})', link)
        if not match:
            raise ValueError(f"Invalid arXiv link or ID: {link}")
        return match.group(1)

    def _format_authors(self, authors: list) -> str:
        """格式化作者列表，最多显示 3 位作者。"""
        if not authors:
            return ""
        names = [a.name for a in authors[:3]]
        result = ", ".join(names)
        if len(authors) > 3:
            result += ", et al."
        return result

    def _extract_version(self, pdf_url: str) -> str:
        """从 PDF URL 提取版本号。"""
        match = re.search(r'v(\d+)$', pdf_url)
        return f"v{match.group(1)}" if match else "v1"
