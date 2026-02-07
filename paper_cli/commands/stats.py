"""Stats command - show library statistics."""

from __future__ import annotations

from pathlib import Path

import typer

from ..core.storage import PaperStorage
from ..utils.cli_args import resolve_cli_value
from ..utils.date import date_key
from ..utils.display import display_stats
from ..utils.paths import papers_csv_path


def show_stats(
    repo_path: Path = typer.Option(Path("."), "--repo", help="Repository path"),
):
    """Show paper library statistics."""
    repo_path = resolve_cli_value(repo_path)

    csv_path = papers_csv_path(repo_path)
    storage = PaperStorage(csv_path)

    papers = storage.load_all()
    total = len(papers)
    topics = storage.get_topics()
    tags = storage.get_all_tags()

    parsed_dates = [date_key(p.date) for p in papers]
    valid_dates = [d for d in parsed_dates if d]
    if valid_dates:
        min_y, min_m = min(valid_dates)
        max_y, max_m = max(valid_dates)
        date_range = (f"{min_y:04d}.{min_m:02d}", f"{max_y:04d}.{max_m:02d}")
    else:
        date_range = (None, None)

    display_stats(total, topics, tags, date_range)
