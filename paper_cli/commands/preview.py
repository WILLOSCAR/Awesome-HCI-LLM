"""Preview markdown command."""

import typer
from typing import Optional
from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from ..core.markdown import MarkdownGenerator
from ..utils.paths import repo_files


console = Console()


def preview_markdown(
    topic: Optional[str] = typer.Option(None, "-t", "--topic", help="Preview specific topic only"),
    diff: bool = typer.Option(False, "--diff", help="Show diff with current README"),
    repo_path: Path = typer.Option(Path("."), "--repo", help="Repository path"),
):
    """Preview the Markdown table that will be generated."""
    csv_path, readme_path = repo_files(repo_path)

    md_gen = MarkdownGenerator(csv_path, readme_path)

    if diff:
        # 显示差异
        diff_text = md_gen.get_diff()
        console.print(Panel(diff_text, title="Changes Preview"))
    else:
        # 显示 Markdown 预览
        preview_text = md_gen.preview_topic(topic)
        if preview_text:
            console.print(Panel(Markdown(preview_text), title="Markdown Preview"))
        else:
            console.print("[yellow]No content to preview.[/yellow]")
