"""Search papers command."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from ..core.storage import PaperStorage
from ..utils.cli_args import resolve_cli_values
from ..utils.date import date_key, is_strict_yyyymm
from ..utils.display import display_papers_table, print_error, print_info
from ..utils.paths import papers_csv_path


def search_papers(
    query: Optional[str] = typer.Argument(None, help="Search query (searches title, tags, authors)"),
    tag: Optional[str] = typer.Option(None, "-t", "--tag", help="Filter by tag"),
    author: Optional[str] = typer.Option(None, "-a", "--author", help="Filter by author"),
    topic: Optional[str] = typer.Option(None, "--topic", help="Filter by topic"),
    date_from: Optional[str] = typer.Option(None, "--from", help="Start date (YYYY.MM)"),
    date_to: Optional[str] = typer.Option(None, "--to", help="End date (YYYY.MM)"),
    recent: bool = typer.Option(False, "--recent", help="Sort by date (most recent first)"),
    limit: int = typer.Option(20, "-l", "--limit", help="Max results (0 for all)"),
    show_all: bool = typer.Option(False, "--all", help="Show all fields"),
    repo_path: Path = typer.Option(Path("."), "--repo", help="Repository path"),
):
    """Search papers in the library."""
    (
        query,
        tag,
        author,
        topic,
        date_from,
        date_to,
        recent,
        limit,
        show_all,
        repo_path,
    ) = resolve_cli_values(
        query,
        tag,
        author,
        topic,
        date_from,
        date_to,
        recent,
        limit,
        show_all,
        repo_path,
    )

    if limit < 0:
        print_error("--limit must be >= 0")
        raise typer.Exit(2)

    for label, value in (("--from", date_from), ("--to", date_to)):
        if value and not is_strict_yyyymm(value):
            print_error(f"{label} must be in YYYY.MM format (e.g., 2024.07)")
            raise typer.Exit(2)

    if date_from and date_to and date_key(date_from) > date_key(date_to):
        print_error("--from must be earlier than or equal to --to")
        raise typer.Exit(2)

    csv_path = papers_csv_path(repo_path)
    storage = PaperStorage(csv_path)

    results = storage.search(
        query=query,
        tag=tag,
        author=author,
        topic=topic,
        date_from=date_from,
        date_to=date_to,
    )

    if recent:
        results = sorted(results, key=lambda p: date_key(p.date) or (-1, -1), reverse=True)

    filters = []
    if query:
        filters.append(f"query='{query}'")
    if tag:
        filters.append(f"tag='{tag}'")
    if author:
        filters.append(f"author='{author}'")
    if topic:
        filters.append(f"topic='{topic}'")
    if date_from or date_to:
        filters.append(f"date={date_from or '*'} to {date_to or '*'}")
    if recent:
        filters.append("sort=recent")

    filter_str = ", ".join(filters) if filters else "all"
    title = f"Search Results ({len(results)} found, {filter_str})"

    if limit > 0 and len(results) > limit:
        print_info(f"Showing top {limit} results (use --limit 0 for all)")
        results = results[:limit]

    display_papers_table(results, title=title, show_all=show_all)
