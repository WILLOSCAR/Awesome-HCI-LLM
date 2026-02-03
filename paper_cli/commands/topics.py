"""Topics command - list all topics."""

import typer
from pathlib import Path

from ..core.storage import PaperStorage
from ..utils.display import display_topics
from ..utils.paths import papers_csv_path


def list_topics(
    repo_path: Path = typer.Option(Path("."), "--repo", help="Repository path"),
):
    """List all topics and their paper counts."""
    csv_path = papers_csv_path(repo_path)
    storage = PaperStorage(csv_path)

    topics = storage.get_topics()

    if not topics:
        typer.echo("No topics found.")
        return

    display_topics(topics)
