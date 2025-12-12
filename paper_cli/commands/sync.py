"""Sync command - update README and push to git."""

import typer
from typing import Optional
from pathlib import Path

from ..core.markdown import MarkdownGenerator
from ..core.git_ops import GitOperations
from ..utils.display import print_success, print_error, print_warning, print_info


def sync_readme(
    readme_only: bool = typer.Option(False, "--readme-only", help="Only update README, skip git"),
    no_push: bool = typer.Option(False, "--no-push", help="Commit but don't push"),
    commit_msg: Optional[str] = typer.Option(None, "-m", "--commit-msg", help="Custom commit message"),
    repo_path: Path = typer.Option(Path("."), "--repo", help="Repository path"),
):
    """Sync README with CSV and optionally push to git."""
    csv_path = repo_path / "papers.csv"
    readme_path = repo_path / "README.md"

    # 更新 README
    print_info("Updating README.md...")
    md_gen = MarkdownGenerator(csv_path, readme_path)

    # 先显示差异
    diff_text = md_gen.get_diff()
    if "No changes" in diff_text:
        print_warning("No changes to sync")
        return

    print_info(diff_text)

    # 执行更新
    md_gen.update_readme()
    print_success("README.md updated")

    if readme_only:
        return

    # Git 操作
    git = GitOperations(repo_path)

    if not git.is_git_repo():
        print_warning("Not a git repository, skipping git operations")
        return

    msg = commit_msg or "Update paper list"
    files = ["papers.csv", "README.md"]

    print_info("Staging files...")
    if not git.add_files(files):
        print_error("Failed to stage files")
        return

    print_info("Committing...")
    if not git.commit(msg):
        print_warning("Nothing to commit")
        return

    print_success("Changes committed")

    if not no_push:
        print_info("Pushing to remote...")
        if git.push():
            print_success("Pushed to remote")
        else:
            print_error("Failed to push")
    else:
        print_info("Skipping push (--no-push)")
