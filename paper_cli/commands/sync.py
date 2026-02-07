"""Sync command - update README and push to git."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from ..core.git_ops import GitOperations
from ..core.markdown import MarkdownGenerator
from ..utils.cli_args import resolve_cli_values
from ..utils.display import print_error, print_info, print_success, print_warning
from ..utils.paths import repo_files


def sync_readme(
    readme_only: bool = typer.Option(False, "--readme-only", help="Only update README, skip git"),
    no_push: bool = typer.Option(False, "--no-push", help="Commit but don't push"),
    commit_msg: Optional[str] = typer.Option(None, "-m", "--commit-msg", help="Custom commit message"),
    repo_path: Path = typer.Option(Path("."), "--repo", help="Repository path"),
):
    """Sync README with CSV and optionally push to git."""
    readme_only, no_push, commit_msg, repo_path = resolve_cli_values(
        readme_only, no_push, commit_msg, repo_path
    )

    csv_path, readme_path = repo_files(repo_path)

    if not csv_path.exists():
        print_error(f"papers.csv not found: {csv_path}")
        raise typer.Exit(1)

    print_info("Updating README.md...")
    md_gen = MarkdownGenerator(csv_path, readme_path)

    try:
        diff_text = md_gen.get_diff()
    except Exception as exc:  # pragma: no cover - defensive runtime protection
        print_error(f"Failed to compute README diff: {exc}")
        raise typer.Exit(1)

    if "No changes" in diff_text:
        print_warning("No changes to sync")
        return

    print_info(diff_text)

    try:
        md_gen.update_readme()
    except Exception as exc:  # pragma: no cover - defensive runtime protection
        print_error(f"Failed to update README.md: {exc}")
        raise typer.Exit(1)

    print_success("README.md updated")

    if readme_only:
        return

    git = GitOperations(repo_path)

    if not git.is_git_repo():
        print_warning("Not a git repository, skipping git operations")
        return

    msg = commit_msg or "Update paper list"
    files = ["papers.csv", "README.md"]

    print_info("Staging files...")
    if not git.add_files(files):
        print_error(f"Failed to stage files: {git.last_error or 'unknown git error'}")
        return

    print_info("Committing...")
    if not git.commit(msg):
        detail = git.last_error or "nothing to commit"
        print_warning(f"Commit skipped: {detail}")
        return

    print_success("Changes committed")

    if not no_push:
        print_info("Pushing to remote...")
        if git.push():
            print_success("Pushed to remote")
        else:
            print_error(f"Failed to push: {git.last_error or 'unknown git error'}")
    else:
        print_info("Skipping push (--no-push)")
