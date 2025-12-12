"""Markdown table generation for README."""

import re
import pandas as pd
from pathlib import Path
from typing import Dict, Optional


class MarkdownGenerator:
    """Markdown 表格生成器，负责更新 README.md。"""

    def __init__(self, csv_path: Path, readme_path: Path):
        self.csv_path = Path(csv_path)
        self.readme_path = Path(readme_path)

    def generate_tables_by_topic(self) -> Dict[str, str]:
        """
        从 CSV 生成按 topic 分组的 Markdown 表格。

        Returns:
            Dict[topic, markdown_table]
        """
        df = pd.read_csv(self.csv_path)
        df.fillna('', inplace=True)

        tables = {}

        if 'Topic' not in df.columns or df['Topic'].isnull().all():
            return tables

        for topic, group in df.groupby('Topic'):
            if group.empty:
                continue

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

                # 合并 Source 和 Journal Ref
                if journal_ref:
                    source = f"{source} ({journal_ref})"

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

    def update_readme(self) -> None:
        """更新 README.md 中的表格。"""
        tables = self.generate_tables_by_topic()

        if not self.readme_path.exists():
            # 如果 README 不存在，创建一个基础版本
            content = "# Paper Collection\n\n"
        else:
            with open(self.readme_path, 'r', encoding='utf-8') as f:
                content = f.read()

        for topic, table in tables.items():
            start_marker = f"<!-- TABLE_START: {topic} -->"
            end_marker = f"<!-- TABLE_END: {topic} -->"

            pattern = re.compile(f"(?s){re.escape(start_marker)}(.*?){re.escape(end_marker)}")

            if pattern.search(content):
                # 已存在标记，替换内容
                content = pattern.sub(f"{start_marker}\n{table}{end_marker}", content)
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

        if diffs:
            return "Changes:\n" + "\n".join(diffs)
        return "No changes detected."
