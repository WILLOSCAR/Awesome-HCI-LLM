"""Topics command - list all topics."""

from __future__ import annotations

from pathlib import Path

import typer

from ..core.storage import PaperStorage
from ..utils.cli_args import resolve_cli_value
from ..utils.display import display_topics
from ..utils.paths import papers_csv_path


def list_topics(
    repo_path: Path = typer.Option(Path("."), "--repo", help="Repository path"),
):
    """List all topics and their paper counts."""
    repo_path = resolve_cli_value(repo_path)

    csv_path = papers_csv_path(repo_path)
    storage = PaperStorage(csv_path)

    topics = storage.get_topics()

    if not topics:
        typer.echo("No topics found.")
        return

    display_topics(topics)
