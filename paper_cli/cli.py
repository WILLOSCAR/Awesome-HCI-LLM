"""Paper CLI - Main entry point."""

import typer
from pathlib import Path

from .commands.add import add_paper
from .commands.search import search_papers
from .commands.list_cmd import list_papers
from .commands.preview import preview_markdown
from .commands.sync import sync_readme
from .commands.topics import list_topics
from .commands.stats import show_stats

app = typer.Typer(
    name="paper",
    help="CLI tool for managing academic paper collections.",
    add_completion=True,
    no_args_is_help=True,
)


# Register commands
app.command(name="add", help="Add a new paper to the library")(add_paper)
app.command(name="search", help="Search papers")(search_papers)
app.command(name="s", hidden=True)(search_papers)  # alias
app.command(name="list", help="List papers")(list_papers)
app.command(name="ls", hidden=True)(list_papers)  # alias
app.command(name="preview", help="Preview Markdown table")(preview_markdown)
app.command(name="sync", help="Sync README and push to git")(sync_readme)
app.command(name="topics", help="List all topics")(list_topics)
app.command(name="stats", help="Show library statistics")(show_stats)


@app.callback()
def main():
    """
    Paper CLI - Manage your academic paper collection.

    Add papers from arXiv, search your library, and keep your README in sync.
    """
    pass


if __name__ == "__main__":
    app()
