#!/usr/bin/env python3
"""
Add arXiv Paper Script (LEGACY)

⚠️  DEPRECATION WARNING ⚠️
This script is deprecated and kept for backward compatibility only.
Use the new `paper add` command instead.

Legacy Usage:
    python src/add_arxiv_paper.py <ARXIV_LINK_OR_ID> <TOPIC>

Modern Alternative:
    paper add <ARXIV_LINK_OR_ID> <TOPIC> [OPTIONS]

Advantages of new command:
    • Auto-sync README after adding
    • Git commit and push integration
    • Preview with --dry-run
    • Custom tags with -t option
    • Support for multiple sources (arXiv, ACM DL, IEEE, DOI)
    • Better error handling and user feedback

Example:
    Legacy:  python src/add_arxiv_paper.py 2308.00352 Agent
    Modern:  paper add 2308.00352 Agent -t "multi-agent, framework"
"""

import sys
import warnings
import arxiv
import csv
import re
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict


# Issue deprecation warning
warnings.warn(
    "\n\n"
    "="*70 + "\n"
    "⚠️  DEPRECATION WARNING\n"
    "="*70 + "\n"
    "This script (add_arxiv_paper.py) is deprecated.\n\n"
    "Please use the new paper CLI instead:\n"
    "  $ paper add <ARXIV_ID> <TOPIC> -t \"your, tags\"\n\n"
    "The new command provides:\n"
    "  • Auto-sync README\n"
    "  • Git integration\n"
    "  • Multiple source support\n"
    "  • Better user experience\n"
    "="*70 + "\n",
    DeprecationWarning,
    stacklevel=2
)


def get_arxiv_paper_details(arxiv_link: str) -> Optional[Dict[str, str]]:
    """
    Fetch paper details from arXiv API.

    NOTE: This is the old implementation. The new version in
    paper_cli/core/fetchers/arxiv.py has better error handling.

    Args:
        arxiv_link: arXiv URL or paper ID

    Returns:
        Dictionary of paper fields or None if error
    """
    # Extract paper ID
    match = re.search(r'(\d{4}\.\d{4,5})', arxiv_link)
    if not match:
        print("❌ Error: Could not extract a valid arXiv ID from the link.")
        return None

    paper_id = match.group(1)

    try:
        client = arxiv.Client(
            page_size=1,
            delay_seconds=3.0,
            num_retries=3
        )
        search = arxiv.Search(id_list=[paper_id])
        paper = next(client.results(search), None)
    except Exception as e:
        print(f"❌ Error fetching data from arXiv API: {e}")
        return None

    if not paper:
        print(f"❌ Could not find paper with ID: {paper_id}")
        return None

    # Extract details
    title = paper.title

    # Authors (up to 3)
    authors = ", ".join([author.name for author in paper.authors[:3]])
    if len(paper.authors) > 3:
        authors += ", et al."

    # Version and Date
    version_match = re.search(r'v(\d+)$', paper.pdf_url)
    version = f"v{version_match.group(1)}" if version_match else 'v1'
    updated_date = paper.updated
    year = updated_date.year
    date_formatted = updated_date.strftime('%Y.%m')

    source = f"arXiv({version}) {year}"
    subjects = ", ".join(paper.categories)
    doi = paper.doi or ''
    journal_ref = paper.journal_ref or ''

    return {
        'Source': source,
        'Title': title,
        'Authors': authors,
        'DOI': doi,
        'Journal_Ref': journal_ref,
        'Link': paper.entry_id,
        'Tag': 'arxiv',
        'Subjects': subjects,
        'Additional_Info': paper.comment or '',
        'Date': date_formatted,
    }


def append_to_csv(
    file_path: Path,
    paper_details: Dict[str, str],
    topic: str
) -> bool:
    """
    Append paper to CSV file.

    Args:
        file_path: Path to papers.csv
        paper_details: Dictionary of paper fields
        topic: Paper topic (HCI/LLM/RAG/Agent)

    Returns:
        True if successful, False otherwise
    """
    paper_details['Topic'] = topic
    fieldnames = [
        'Source', 'Title', 'Authors', 'DOI', 'Journal_Ref',
        'Link', 'Tag', 'Subjects', 'Additional_Info', 'Date', 'Topic'
    ]

    try:
        file_exists = file_path.exists()
        with open(file_path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            if not file_exists or f.tell() == 0:
                writer.writeheader()
            writer.writerow(paper_details)

        print(f"✅ Successfully added '{paper_details['Title']}' to {file_path}")
        return True
    except Exception as e:
        print(f"❌ Error writing to CSV file: {e}")
        return False


def main() -> int:
    """Main entry point."""
    if len(sys.argv) != 3:
        print("Usage: python add_arxiv_paper.py <ARXIV_PAPER_LINK_OR_ID> <TOPIC>")
        print("\nExample:")
        print("  python add_arxiv_paper.py 2308.00352 Agent")
        print("\n⚠️  This script is deprecated. Use instead:")
        print("  paper add 2308.00352 Agent -t \"your, tags\"")
        return 1

    print("\n⚠️  WARNING: You are using a deprecated script!")
    print("Consider switching to: paper add <ID> <TOPIC> -t \"tags\"\n")

    arxiv_identifier = sys.argv[1]
    topic = sys.argv[2]

    print(f"🔍 Fetching paper: {arxiv_identifier}...")
    details = get_arxiv_paper_details(arxiv_identifier)

    if not details:
        return 1

    csv_file = Path('papers.csv')
    if append_to_csv(csv_file, details, topic):
        print("\n💡 Next steps:")
        print("  1. Update README: paper sync")
        print("  2. Or just use 'paper add' next time (auto-syncs!)")
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
