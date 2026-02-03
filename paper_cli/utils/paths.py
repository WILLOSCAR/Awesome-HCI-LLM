"""Repository path helpers.

Most commands accept a --repo option, and then need to resolve the standard
files inside that repository. Centralize the filenames here to avoid repeated
string literals across commands.
"""

from __future__ import annotations

from pathlib import Path
from typing import Tuple

PAPERS_CSV_FILENAME = "papers.csv"
README_FILENAME = "README.md"


def repo_files(repo_path: Path) -> Tuple[Path, Path]:
    """Return (papers.csv, README.md) paths for a repository root."""
    repo = Path(repo_path)
    return repo / PAPERS_CSV_FILENAME, repo / README_FILENAME


def papers_csv_path(repo_path: Path) -> Path:
    """Return the papers.csv path for a repository root."""
    return Path(repo_path) / PAPERS_CSV_FILENAME


def readme_path(repo_path: Path) -> Path:
    """Return the README.md path for a repository root."""
    return Path(repo_path) / README_FILENAME

