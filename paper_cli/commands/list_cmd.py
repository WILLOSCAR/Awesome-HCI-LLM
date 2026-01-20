"""List papers command."""

import typer
from typing import Optional
from pathlib import Path

from ..core.storage import PaperStorage
from ..utils.display import display_papers_table, print_info
from ..utils.date import date_key


def list_papers(
    topic: Optional[str] = typer.Option(None, "-t", "--topic", help="Filter by topic"),
    limit: int = typer.Option(10, "-l", "--limit", help="Max results (0 for all)"),
    recent: bool = typer.Option(False, "--recent", help="Sort by date (most recent first)"),
    show_all: bool = typer.Option(False, "--all", help="Show all fields"),
    repo_path: Path = typer.Option(Path("."), "--repo", help="Repository path"),
):
    """List papers in the library."""
    csv_path = repo_path / "papers.csv"
    storage = PaperStorage(csv_path)

    # 加载论文
    if topic:
        papers = storage.search(topic=topic)
        title = f"Papers in '{topic}' ({len(papers)} total)"
    else:
        papers = storage.load_all()
        title = f"All Papers ({len(papers)} total)"

    # 按日期排序
    if recent:
        # Put invalid/missing dates last.
        papers = sorted(papers, key=lambda p: date_key(p.date) or (-1, -1), reverse=True)

    # 限制结果数量
    if limit > 0 and len(papers) > limit:
        print_info(f"Showing {limit} papers (use --limit 0 for all)")
        papers = papers[:limit]

    display_papers_table(papers, title=title, show_all=show_all)
