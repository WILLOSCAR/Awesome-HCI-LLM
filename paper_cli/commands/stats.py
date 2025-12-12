"""Stats command - show library statistics."""

import typer
from pathlib import Path

from ..core.storage import PaperStorage
from ..utils.display import display_stats


def show_stats(
    repo_path: Path = typer.Option(Path("."), "--repo", help="Repository path"),
):
    """Show paper library statistics."""
    csv_path = repo_path / "papers.csv"
    storage = PaperStorage(csv_path)

    papers = storage.load_all()
    total = len(papers)
    topics = storage.get_topics()
    tags = storage.get_all_tags()

    # 计算日期范围
    dates = [p.date for p in papers if p.date]
    date_range = (min(dates) if dates else None, max(dates) if dates else None)

    display_stats(total, topics, tags, date_range)
