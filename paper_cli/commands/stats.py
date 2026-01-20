"""Stats command - show library statistics."""

import typer
from pathlib import Path

from ..core.storage import PaperStorage
from ..utils.display import display_stats
from ..utils.date import date_key


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
    parsed_dates = [date_key(p.date) for p in papers]
    valid_dates = [d for d in parsed_dates if d]
    if valid_dates:
        min_y, min_m = min(valid_dates)
        max_y, max_m = max(valid_dates)
        date_range = (f"{min_y:04d}.{min_m:02d}", f"{max_y:04d}.{max_m:02d}")
    else:
        date_range = (None, None)

    display_stats(total, topics, tags, date_range)
