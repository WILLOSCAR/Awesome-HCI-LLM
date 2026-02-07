"""List papers command."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from ..core.storage import PaperStorage
from ..utils.cli_args import resolve_cli_values
from ..utils.date import date_key
from ..utils.display import display_papers_table, print_error, print_info
from ..utils.paths import papers_csv_path


def list_papers(
    topic: Optional[str] = typer.Option(None, "-t", "--topic", help="Filter by topic"),
    limit: int = typer.Option(10, "-l", "--limit", help="Max results (0 for all)"),
    recent: bool = typer.Option(False, "--recent", help="Sort by date (most recent first)"),
    show_all: bool = typer.Option(False, "--all", help="Show all fields"),
    repo_path: Path = typer.Option(Path("."), "--repo", help="Repository path"),
):
    """List papers in the library."""
    topic, limit, recent, show_all, repo_path = resolve_cli_values(
        topic, limit, recent, show_all, repo_path
    )

    if limit < 0:
        print_error("--limit must be >= 0")
        raise typer.Exit(2)

    csv_path = papers_csv_path(repo_path)
    storage = PaperStorage(csv_path)

    if topic:
        papers = storage.search(topic=topic)
        title = f"Papers in '{topic}' ({len(papers)} total)"
    else:
        papers = storage.load_all()
        title = f"All Papers ({len(papers)} total)"

    if recent:
        papers = sorted(papers, key=lambda p: date_key(p.date) or (-1, -1), reverse=True)

    if limit > 0 and len(papers) > limit:
        print_info(f"Showing {limit} papers (use --limit 0 for all)")
        papers = papers[:limit]

    display_papers_table(papers, title=title, show_all=show_all)
