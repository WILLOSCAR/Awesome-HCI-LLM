"""Add paper command."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer
from rich.console import Console

from ..core.fetchers import FetcherRegistry
from ..core.git_ops import GitOperations
from ..core.markdown import MarkdownGenerator
from ..core.models import Paper
from ..core.storage import PaperStorage
from ..utils.cli_args import resolve_cli_values
from ..utils.display import display_paper_detail, print_error, print_info, print_success, print_warning
from ..utils.paths import repo_files

console = Console()


def prompt_manual_input(link: str, topic: str, custom_tag: Optional[str] = None) -> Paper:
    """Prompt user for manual paper input when auto-fetch fails."""
    console.print("
[yellow]Please enter paper details manually:[/yellow]
")

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
    topic: str = typer.Argument(..., help="Topic (free-form, e.g., Memory/Personalization/LLM/MLLM)"),
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
    (
        link,
        topic,
        tag,
        note,
        source,
        no_sync,
        no_git,
        dry_run,
        commit_msg,
        repo_path,
    ) = resolve_cli_values(
        link,
        topic,
        tag,
        note,
        source,
        no_sync,
        no_git,
        dry_run,
        commit_msg,
        repo_path,
    )

    link = str(link).strip()
    topic = str(topic).strip()
    if not link:
        print_error("Paper link/ID cannot be empty")
        raise typer.Exit(2)
    if not topic:
        print_error("Topic cannot be empty")
        raise typer.Exit(2)

    csv_path, readme_path = repo_files(repo_path)

    storage = PaperStorage(csv_path)
    registry = FetcherRegistry()
    allow_duplicate = False

    if storage.exists(link):
        print_warning("This paper already exists in the library")
        if not typer.confirm("Add anyway?", default=False):
            raise typer.Exit(0)
        allow_duplicate = True

    source_type = registry.detect_source(link)
    print_info(f"Detected source: {source_type}")

    paper = None
    try:
        fetcher = registry.get_fetcher(link)
        print_info("Fetching paper metadata...")
        paper = fetcher.fetch(link, custom_tag=tag)
    except ValueError as exc:
        print_error(f"Failed to fetch metadata: {exc}")
        if typer.confirm("Enter details manually?", default=True):
            paper = prompt_manual_input(link, topic, tag)
        else:
            raise typer.Exit(1)
    except Exception as exc:  # pragma: no cover - network/service/runtime failures
        print_error(f"Error: {exc}")
        if typer.confirm("Enter details manually?", default=True):
            paper = prompt_manual_input(link, topic, tag)
        else:
            raise typer.Exit(1)

    if not paper:
        raise typer.Exit(1)

    if not allow_duplicate:
        for candidate in [paper.doi, paper.link]:
            if candidate and storage.exists(candidate):
                print_warning("This paper already exists in the library (matched by fetched metadata)")
                if not typer.confirm("Add anyway?", default=False):
                    raise typer.Exit(0)
                allow_duplicate = True
                break

    paper.topic = topic

    if tag and not paper.tag:
        paper.tag = tag

    if note:
        paper.additional_info = note

    if source:
        paper.source = source

    console.print()
    display_paper_detail(paper)
    console.print()

    if dry_run:
        print_warning("Dry run mode - no changes made")
        raise typer.Exit(0)

    storage.add_paper(paper)
    print_success("Paper added to CSV")

    if not no_sync:
        try:
            md_gen = MarkdownGenerator(csv_path, readme_path)
            md_gen.update_readme()
        except Exception as exc:  # pragma: no cover - runtime I/O protection
            print_error(f"Failed to update README.md: {exc}")
            raise typer.Exit(1)
        print_success("README.md updated")

    if not no_git and not no_sync:
        git = GitOperations(repo_path)
        short_title = paper.title[:50]
        default_msg = f"Add paper: {short_title}{'...' if len(paper.title) > 50 else ''}"
        msg = commit_msg or default_msg
        files = ["papers.csv", "README.md"]

        print_info("Committing and pushing...")
        success, error = git.add_commit_push(files, msg)
        if success:
            print_success("Changes committed and pushed")
        else:
            print_warning(f"Git operation: {error}")

    print_success("Done!")
