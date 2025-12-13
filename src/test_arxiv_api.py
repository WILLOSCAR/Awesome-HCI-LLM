#!/usr/bin/env python3
"""
arXiv API Response Inspector

This script fetches and displays all available fields from the arXiv API
for a given paper ID. Useful for debugging and understanding API responses.

Usage:
    python test_arxiv_api.py <ARXIV_PAPER_ID>

Example:
    python test_arxiv_api.py 2308.00352
    python test_arxiv_api.py 2403.06201
"""

import sys
import arxiv
from typing import Optional


def fetch_arxiv_paper(paper_id: str) -> Optional[arxiv.Result]:
    """
    Fetch paper metadata from arXiv API.

    Args:
        paper_id: arXiv paper ID (e.g., "2308.00352")

    Returns:
        arxiv.Result object if found, None otherwise
    """
    try:
        client = arxiv.Client(
            page_size=1,
            delay_seconds=3.0,
            num_retries=3
        )
        search = arxiv.Search(id_list=[paper_id])
        return next(client.results(search), None)
    except Exception as e:
        print(f"❌ Error fetching paper: {e}", file=sys.stderr)
        return None


def display_paper_fields(paper: arxiv.Result) -> None:
    """
    Display all available fields from arXiv API response.

    Args:
        paper: arxiv.Result object containing paper metadata
    """
    print(f"\n{'='*70}")
    print(f"arXiv API Response for: {paper.entry_id}")
    print(f"{'='*70}\n")

    # Core fields
    print(f"📄 Title: {paper.title}")
    print(f"👥 Authors: {[author.name for author in paper.authors]}")
    print(f"🏷️  Primary Category: {paper.primary_category}")
    print(f"🔖 Categories: {paper.categories}")

    # Dates
    print(f"📅 Published: {paper.published}")
    print(f"🔄 Updated: {paper.updated}")

    # Links
    print(f"🔗 Entry ID: {paper.entry_id}")
    print(f"📥 PDF URL: {paper.pdf_url}")

    # Optional fields
    print(f"\n--- Optional Fields ---")
    print(f"🆔 DOI: {paper.doi or 'N/A'}")
    print(f"📰 Journal Ref: {paper.journal_ref or 'N/A'}")
    print(f"💬 Comment: {paper.comment or 'N/A'}")

    # Abstract
    print(f"\n--- Abstract ---")
    print(f"{paper.summary[:500]}...")

    # Links detail
    print(f"\n--- Links ---")
    for link in paper.links:
        print(f"  • {link.title or 'untitled'}: {link.href}")

    print(f"\n{'='*70}\n")


def main() -> int:
    """Main entry point."""
    if len(sys.argv) != 2:
        print("Usage: python test_arxiv_api.py <ARXIV_PAPER_ID>")
        print("\nExample:")
        print("  python test_arxiv_api.py 2308.00352")
        return 1

    paper_id = sys.argv[1]
    print(f"🔍 Fetching paper: {paper_id}...")

    paper = fetch_arxiv_paper(paper_id)

    if not paper:
        print(f"❌ Could not find paper with ID: {paper_id}")
        return 1

    display_paper_fields(paper)

    # Usage tip
    print("💡 Tip: Use 'paper add' command to add this paper to your collection:")
    print(f"   paper add {paper_id} <TOPIC> -t \"your, tags\"")

    return 0


if __name__ == "__main__":
    sys.exit(main())
