"""Markdown table generation for README."""

import re
import pandas as pd
from pathlib import Path
from typing import Dict, Optional, Set

from ..utils.date import date_key


class MarkdownGenerator:
    """Markdown 表格生成器，负责更新 README.md。"""

    def __init__(self, csv_path: Path, readme_path: Path):
        self.csv_path = Path(csv_path)
        self.readme_path = Path(readme_path)

    @staticmethod
    def _date_sort_value(value: str) -> int:
        """Return sortable YYYYMM integer, or -1 when invalid/missing."""
        k = date_key(str(value))
        return (k[0] * 100 + k[1]) if k else -1

    @staticmethod
    def _extract_existing_topics(content: str) -> Set[str]:
        """Extract all topic names from TABLE_START markers in README content."""
        topics = set(re.findall(r"<!--\s*TABLE_START:\s*(.*?)\s*-->", content))
        return {t.strip() for t in topics if t and t.strip()}

    @staticmethod
    def _remove_topic_section(content: str, topic: str) -> str:
        """Remove a topic section (optional heading + table markers) from README content."""
        start_marker = re.escape(f"<!-- TABLE_START: {topic} -->")
        end_marker = re.escape(f"<!-- TABLE_END: {topic} -->")
        # Remove only headings directly attached to the managed table block.
        pattern = re.compile(
            rf"(?:\n#+\s+{re.escape(topic)}\s*\n)?{start_marker}\n.*?{end_marker}\n?",
            flags=re.DOTALL,
        )
        return pattern.sub("\n", content)

    def generate_tables_by_topic(self) -> Dict[str, str]:
        """
        从 CSV 生成按 topic 分组的 Markdown 表格。

        Returns:
            Dict[topic, markdown_table]
        """
        # Keep all columns as strings to preserve formatting like 'YYYY.MM'.
        df = pd.read_csv(self.csv_path, dtype=str, keep_default_na=False)

        tables = {}

        if 'Topic' not in df.columns or df['Topic'].isnull().all():
            return tables

        # Treat blank/whitespace-only topic as missing metadata.
        df = df.copy()
        df['Topic'] = df['Topic'].astype(str).str.strip()
        df = df[df['Topic'] != ""]
        if df.empty:
            return tables

        for topic, group in df.groupby('Topic'):
            if group.empty:
                continue

            # Default: show newest papers first (invalid/missing dates go last).
            group = group.copy()
            if "Date" in group.columns:
                group["__date_sort"] = group["Date"].apply(self._date_sort_value)
            else:
                group["__date_sort"] = -1
            group = group.sort_values(
                by=["__date_sort", "Title"],
                ascending=[False, True],
                kind="mergesort",
            )
            group.drop(columns=["__date_sort"], inplace=True)

            # 表格头
            md_table = "| Source | Title (Link) | Authors | Tag | Subjects | Additional info | Date |\n"
            md_table += "|---|---|---|---|---|---|---|\n"

            for _, row in group.iterrows():
                source = row.get('Source', '')
                title = row.get('Title', '')
                link = row.get('Link', '')
                authors_full = row.get('Authors', '')
                journal_ref = row.get('Journal_Ref', '')
                tag = row.get('Tag', '')
                subjects = row.get('Subjects', '')
                additional_info = row.get('Additional_Info', '')
                date = row.get('Date', '')

                # 格式化 Source 列：优先显示 arXiv 信息
                source = self._format_source_column(source, link, journal_ref)

                # 格式化作者显示
                if authors_full:
                    first_author = authors_full.split(',')[0]
                    authors_display = f"{first_author}, et al."
                else:
                    authors_display = ''

                # 带链接的标题
                linked_title = f"[{title}]({link})" if link else title

                # 构建表格行
                md_table += f"| {source} | {linked_title} | {authors_display} | {tag} | {subjects} | {additional_info} | {date} |\n"

            tables[topic] = md_table

        return tables

    def _format_source_column(self, source: str, link: str, journal_ref: str) -> str:
        """
        格式化 Source 列，优先显示 arXiv 信息。

        规则：
        1. 如果 Source 已经是 arXiv 格式 (如 "arXiv(v1) 2024")：
           - 有会议信息：arXiv(v1) 2024 (ICLR 2024)
           - 无会议信息：arXiv(v1) 2024
        2. 如果 Source 是会议名但 Link 是 arXiv：
           - 从 Link 提取版本号，构建：arXiv(v?) year (CHI 2023)
        3. 如果都不是 arXiv：
           - 保持原有逻辑

        Args:
            source: 原始 Source 字段
            link: 论文链接
            journal_ref: 期刊/会议引用

        Returns:
            格式化后的 Source 字符串
        """
        is_arxiv_link = 'arxiv.org' in link.lower()
        is_arxiv_source = 'arxiv' in source.lower()

        # 情况1: Source 已经包含 arXiv 格式
        if is_arxiv_source:
            # 提取会议信息（优先用 Journal_Ref，否则从 Source 中查找括号内容）
            conf_info = journal_ref.strip()
            if not conf_info and '(' in source:
                # Source 可能已经包含会议信息，如 "arXiv(v1) 2024 (ICLR)"
                return source

            if conf_info:
                # 添加会议信息到括号中
                return f"{source} ({conf_info})"
            return source

        # 情况2: Source 是会议名，但 Link 是 arXiv
        if is_arxiv_link and not is_arxiv_source:
            # 从 Link 提取版本号
            version = self._extract_arxiv_version(link)

            # 尝试从 source 或其他地方获取年份
            # 通常会议名格式是 "CHI 2023", "ICLR 2024"
            year_match = re.search(r'20\d{2}', source)
            year = year_match.group(0) if year_match else ''

            # 构建 arXiv 格式
            arxiv_format = f"arXiv({version})"
            if year:
                arxiv_format += f" {year}"

            # 添加会议信息到括号中
            return f"{arxiv_format} ({source})"

        # 情况3: 非 arXiv 论文，保持原有逻辑
        if journal_ref:
            return f"{source} ({journal_ref})"
        return source

    def _extract_arxiv_version(self, link: str) -> str:
        """
        从 arXiv 链接中提取版本号。

        Args:
            link: arXiv 链接

        Returns:
            版本号字符串，如 "v1", "v2"
        """
        # 匹配版本号: https://arxiv.org/abs/2308.00352v1 或 .../pdf/2308.00352v2
        match = re.search(r'v(\d+)(?:\.pdf)?$', link)
        if match:
            return f"v{match.group(1)}"
        return "v1"  # 默认 v1

    def update_readme(self) -> None:
        """更新 README.md 中的表格。"""
        tables = self.generate_tables_by_topic()

        if not self.readme_path.exists():
            # 如果 README 不存在，创建一个基础版本
            content = "# Paper Collection\n\n"
        else:
            with open(self.readme_path, 'r', encoding='utf-8') as f:
                content = f.read()

        existing_topics = self._extract_existing_topics(content)
        table_topics = set(tables.keys())

        # Remove stale topic sections that no longer exist in CSV.
        for stale_topic in sorted(existing_topics - table_topics):
            content = self._remove_topic_section(content, stale_topic)

        for topic, table in tables.items():
            start_marker = f"<!-- TABLE_START: {topic} -->"
            end_marker = f"<!-- TABLE_END: {topic} -->"

            pattern = re.compile(f"(?s){re.escape(start_marker)}(.*?){re.escape(end_marker)}")

            if pattern.search(content):
                # 已存在标记，替换内容
                # Use a function replacement so backslashes in table content (e.g., LaTeX \href)
                # are not treated as regex replacement escapes.
                replacement = f"{start_marker}\n{table}{end_marker}"
                content = pattern.sub(lambda _m: replacement, content)
            else:
                # 不存在标记，在文件末尾添加新 section
                content += f"\n# {topic}\n{start_marker}\n{table}{end_marker}\n"

        with open(self.readme_path, 'w', encoding='utf-8') as f:
            f.write(content)

    def preview_topic(self, topic: Optional[str] = None) -> str:
        """
        预览指定 topic 的 Markdown 表格。

        Args:
            topic: 要预览的 topic，None 表示预览所有

        Returns:
            Markdown 格式的表格字符串
        """
        tables = self.generate_tables_by_topic()

        if topic:
            if topic in tables:
                return f"# {topic}\n\n{tables[topic]}"
            else:
                return f"Topic '{topic}' not found."

        # 预览所有
        result = []
        for t, table in tables.items():
            result.append(f"# {t}\n\n{table}")
        return "\n".join(result)

    def get_diff(self) -> str:
        """
        获取当前 CSV 与 README 的差异。

        Returns:
            差异描述字符串
        """
        if not self.readme_path.exists():
            return "README.md does not exist. Will be created."

        tables = self.generate_tables_by_topic()

        with open(self.readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        existing_topics = self._extract_existing_topics(content)
        table_topics = set(tables.keys())

        diffs = []
        for topic, new_table in tables.items():
            start_marker = f"<!-- TABLE_START: {topic} -->"
            end_marker = f"<!-- TABLE_END: {topic} -->"

            pattern = re.compile(f"(?s){re.escape(start_marker)}(.*?){re.escape(end_marker)}")
            match = pattern.search(content)

            if match:
                old_table = match.group(1).strip()
                new_table_stripped = new_table.strip()
                if old_table != new_table_stripped:
                    # 计算行数差异
                    old_lines = len(old_table.split('\n'))
                    new_lines = len(new_table_stripped.split('\n'))
                    diffs.append(f"  {topic}: {old_lines} -> {new_lines} rows")
            else:
                new_lines = len(new_table.strip().split('\n'))
                diffs.append(f"  {topic}: NEW ({new_lines} rows)")

        for topic in sorted(existing_topics - table_topics):
            diffs.append(f"  {topic}: REMOVED")

        if diffs:
            return "Changes:\n" + "\n".join(diffs)
        return "No changes detected."
