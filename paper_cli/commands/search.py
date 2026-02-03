"""Search papers command."""

import typer
from typing import Optional
from pathlib import Path

from ..core.storage import PaperStorage
from ..utils.display import display_papers_table, print_info
from ..utils.paths import papers_csv_path


def search_papers(
    query: Optional[str] = typer.Argument(None, help="Search query (searches title, tags, authors)"),
    tag: Optional[str] = typer.Option(None, "-t", "--tag", help="Filter by tag"),
    author: Optional[str] = typer.Option(None, "-a", "--author", help="Filter by author"),
    topic: Optional[str] = typer.Option(None, "--topic", help="Filter by topic"),
    date_from: Optional[str] = typer.Option(None, "--from", help="Start date (YYYY.MM)"),
    date_to: Optional[str] = typer.Option(None, "--to", help="End date (YYYY.MM)"),
    limit: int = typer.Option(20, "-l", "--limit", help="Max results (0 for all)"),
    show_all: bool = typer.Option(False, "--all", help="Show all fields"),
    repo_path: Path = typer.Option(Path("."), "--repo", help="Repository path"),
):
    """Search papers in the library."""
    csv_path = papers_csv_path(repo_path)
    storage = PaperStorage(csv_path)

    # 执行搜索
    results = storage.search(
        query=query,
        tag=tag,
        author=author,
        topic=topic,
        date_from=date_from,
        date_to=date_to,
    )

    # 构建标题
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

    filter_str = ", ".join(filters) if filters else "all"
    title = f"Search Results ({len(results)} found, {filter_str})"

    # 限制结果数量
    if limit > 0 and len(results) > limit:
        print_info(f"Showing top {limit} results (use --limit 0 for all)")
        results = results[:limit]

    display_papers_table(results, title=title, show_all=show_all)
