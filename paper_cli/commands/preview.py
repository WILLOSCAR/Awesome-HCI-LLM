"""Preview markdown command."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from ..core.markdown import MarkdownGenerator
from ..utils.cli_args import resolve_cli_values
from ..utils.display import print_error
from ..utils.paths import repo_files

console = Console()


def preview_markdown(
    topic: Optional[str] = typer.Option(None, "-t", "--topic", help="Preview specific topic only"),
    diff: bool = typer.Option(False, "--diff", help="Show diff with current README"),
    repo_path: Path = typer.Option(Path("."), "--repo", help="Repository path"),
):
    """Preview the Markdown table that will be generated."""
    topic, diff, repo_path = resolve_cli_values(topic, diff, repo_path)

    csv_path, readme_path = repo_files(repo_path)

    if not csv_path.exists():
        print_error(f"papers.csv not found: {csv_path}")
        raise typer.Exit(1)

    md_gen = MarkdownGenerator(csv_path, readme_path)

    try:
        if diff:
            diff_text = md_gen.get_diff()
            console.print(Panel(diff_text, title="Changes Preview"))
            return

        preview_text = md_gen.preview_topic(topic)
    except Exception as exc:  # pragma: no cover - defensive runtime protection
        print_error(f"Failed to render preview: {exc}")
        raise typer.Exit(1)

    if preview_text:
        console.print(Panel(Markdown(preview_text), title="Markdown Preview"))
    else:
        console.print("[yellow]No content to preview.[/yellow]")
