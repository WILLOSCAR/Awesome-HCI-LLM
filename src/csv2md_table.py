#!/usr/bin/env python3
"""
CSV to Markdown Table Generator (LEGACY)

⚠️  DEPRECATION WARNING ⚠️
This script is deprecated and kept for backward compatibility only.
Use the new `paper sync` command instead.

Legacy Usage:
    python src/csv2md_table.py

Modern Alternative:
    paper sync --readme-only

Advantages of new command:
    • Smart Source column formatting (arXiv version detection)
    • Automatic Journal_Ref merging
    • Better error handling
    • Consistent with other paper CLI commands
"""

import warnings
import pandas as pd
import re
from pathlib import Path


# Issue deprecation warning
warnings.warn(
    "\n\n"
    "="*70 + "\n"
    "⚠️  DEPRECATION WARNING\n"
    "="*70 + "\n"
    "This script (csv2md_table.py) is deprecated.\n\n"
    "Please use the new paper CLI instead:\n"
    "  $ paper sync --readme-only\n\n"
    "The new command provides:\n"
    "  • Smart Source formatting (arXiv version detection)\n"
    "  • Better integration with other tools\n"
    "  • More features and better maintenance\n"
    "="*70 + "\n",
    DeprecationWarning,
    stacklevel=2
)


def generate_md_tables_by_topic(csv_file: Path) -> dict:
    """
    Generate Markdown tables from CSV, grouped by topic.

    NOTE: This is the old implementation. The new version in
    paper_cli/core/markdown.py includes smart Source column formatting.

    Args:
        csv_file: Path to papers.csv

    Returns:
        Dictionary mapping topic to Markdown table string
    """
    df = pd.read_csv(csv_file)
    df.fillna('', inplace=True)
    tables = {}

    if 'Topic' not in df.columns or df['Topic'].isnull().all():
        return tables

    for topic, group in df.groupby('Topic'):
        if group.empty:
            continue

        # Define table header
        md_table = "| Source | Title (Link) | Authors | Tag | Subjects | Additional info | Date |\n"
        md_table += "|---|---|---|---|---|---|---|\n"

        for _, row in group.iterrows():
            # Extract fields
            title = row.get('Title', '')
            link = row.get('Link', '')
            source = row.get('Source', '')
            authors_full = row.get('Authors', '')
            journal_ref = row.get('Journal_Ref', '')
            tag = row.get('Tag', '')
            subjects = row.get('Subjects', '')
            additional_info = row.get('Additional_Info', '')
            date = row.get('Date', '')

            # Simple Source and Journal Ref combination (old way)
            if journal_ref:
                source = f"{source} ({journal_ref})"

            # Format authors for display
            if authors_full:
                first_author = authors_full.split(',')[0]
                authors_display = f"{first_author}, et al."
            else:
                authors_display = ''

            # Create linked title
            linked_title = f"[{title}]({link})" if link else title

            # Build table row
            md_table += f"| {source} | {linked_title} | {authors_display} | {tag} | {subjects} | {additional_info} | {date} |\n"

        tables[topic] = md_table

    return tables


def update_readme(readme_file: Path, tables: dict) -> None:
    """
    Update README.md with generated tables.

    Args:
        readme_file: Path to README.md
        tables: Dictionary of topic -> Markdown table
    """
    with open(readme_file, 'r', encoding='utf-8') as f:
        content = f.read()

    for topic, table in tables.items():
        start_marker = f"<!-- TABLE_START: {topic} -->"
        end_marker = f"<!-- TABLE_END: {topic} -->"

        pattern = re.compile(f"(?s){re.escape(start_marker)}(.*?){re.escape(end_marker)}")

        if pattern.search(content):
            content = pattern.sub(f"{start_marker}\n{table}{end_marker}", content)
        else:
            content += f"\n# {topic}\n{start_marker}\n{table}{end_marker}\n"

    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(content)


def main() -> int:
    """Main entry point."""
    print("\n⚠️  WARNING: You are using a deprecated script!")
    print("Consider switching to: paper sync --readme-only\n")

    csv_file = Path("papers.csv")
    readme_file = Path("README.md")

    if not csv_file.exists():
        print(f"❌ Error: {csv_file} not found")
        return 1

    print(f"📖 Reading {csv_file}...")
    tables = generate_md_tables_by_topic(csv_file)

    print(f"📝 Updating {readme_file}...")
    update_readme(readme_file, tables)

    print(f"✅ Successfully updated README.md with {len(tables)} topic(s).")
    print("\n💡 Next time, try: paper sync --readme-only")

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
