"""Add paper command."""

import typer
from typing import Optional
from pathlib import Path
from rich.console import Console

from ..core.fetchers import FetcherRegistry
from ..core.models import Paper
from ..core.storage import PaperStorage
from ..core.markdown import MarkdownGenerator
from ..core.git_ops import GitOperations
from ..utils.display import display_paper_detail, print_success, print_error, print_warning, print_info

console = Console()


def prompt_manual_input(link: str, topic: str, custom_tag: Optional[str] = None) -> Paper:
    """Prompt user for manual paper input when auto-fetch fails."""
    console.print("\n[yellow]Please enter paper details manually:[/yellow]\n")

    title = typer.prompt("Title")
    authors = typer.prompt("Authors (comma-separated)", default="")
    source = typer.prompt("Source/Venue (e.g., CHI 2024)", default="")
    date = typer.prompt("Date (YYYY.MM)", default="")

    return Paper(
        source=source,
        title=title,
        authors=authors,
        doi="",
        journal_ref="",
        link=link,
        tag=custom_tag or "",
        subjects="",
        additional_info="",
        date=date,
        topic=topic,
    )


def add_paper(
    link: str = typer.Argument(..., help="Paper URL (arXiv, ACM, IEEE) or arXiv ID"),
    topic: str = typer.Argument(..., help="Topic (HCI/LLM/RAG/Agent)"),
    tag: Optional[str] = typer.Option(None, "-t", "--tag", help="Custom tags (comma-separated)"),
    note: Optional[str] = typer.Option(None, "-n", "--note", help="Additional notes"),
    source: Optional[str] = typer.Option(None, "-s", "--source", help="Custom source (e.g., 'CHI 2024')"),
    no_sync: bool = typer.Option(False, "--no-sync", help="Don't update README"),
    no_git: bool = typer.Option(False, "--no-git", help="Don't commit/push"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Preview only, don't save"),
    commit_msg: Optional[str] = typer.Option(None, "-m", "--commit-msg", help="Custom commit message"),
    repo_path: Path = typer.Option(Path("."), "--repo", help="Repository path"),
):
    """Add a new paper to the library.

    Supports multiple sources:
    - arXiv: https://arxiv.org/abs/2312.00752 or just 2312.00752
    - ACM DL: https://dl.acm.org/doi/10.1145/xxx
    - IEEE: https://ieeexplore.ieee.org/document/xxx
    - Any DOI: https://doi.org/10.xxxx/xxx or 10.xxxx/xxx
    """
    csv_path = repo_path / "papers.csv"
    readme_path = repo_path / "README.md"

    storage = PaperStorage(csv_path)
    registry = FetcherRegistry()

    # Check if already exists
    if storage.exists(link):
        print_warning("This paper already exists in the library")
        if not typer.confirm("Add anyway?", default=False):
            raise typer.Exit(0)

    # Detect source
    source_type = registry.detect_source(link)
    print_info(f"Detected source: {source_type}")

    # Try to fetch paper metadata
    paper = None
    try:
        fetcher = registry.get_fetcher(link)
        print_info(f"Fetching paper metadata...")
        paper = fetcher.fetch(link, custom_tag=tag)
    except ValueError as e:
        print_error(f"Failed to fetch metadata: {e}")
        if typer.confirm("Enter details manually?", default=True):
            paper = prompt_manual_input(link, topic, tag)
        else:
            raise typer.Exit(1)
    except Exception as e:
        print_error(f"Error: {e}")
        if typer.confirm("Enter details manually?", default=True):
            paper = prompt_manual_input(link, topic, tag)
        else:
            raise typer.Exit(1)

    if not paper:
        raise typer.Exit(1)

    # Set topic
    paper.topic = topic

    # Custom tag (override if provided and not already set)
    if tag and not paper.tag:
        paper.tag = tag

    # Additional notes
    if note:
        paper.additional_info = note

    # Custom source
    if source:
        paper.source = source

    # Display preview
    console.print()
    display_paper_detail(paper)
    console.print()

    if dry_run:
        print_warning("Dry run mode - no changes made")
        raise typer.Exit(0)

    # Add to CSV
    storage.add_paper(paper)
    print_success("Paper added to CSV")

    # Update README
    if not no_sync:
        md_gen = MarkdownGenerator(csv_path, readme_path)
        md_gen.update_readme()
        print_success("README.md updated")

    # Git operations
    if not no_git and not no_sync:
        git = GitOperations(repo_path)
        msg = commit_msg or f"Add paper: {paper.title[:50]}..."
        files = ["papers.csv", "README.md"]

        print_info("Committing and pushing...")
        success, error = git.add_commit_push(files, msg)
        if success:
            print_success("Changes committed and pushed")
        else:
            print_warning(f"Git operation: {error}")

    print_success("Done!")
