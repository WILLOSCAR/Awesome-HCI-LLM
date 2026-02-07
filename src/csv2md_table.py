#!/usr/bin/env python3
"""Legacy wrapper for rebuilding README markdown tables.

Prefer the modern CLI:
    paper sync --readme-only
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from _legacy_cli_bridge import bootstrap_repo_imports, warn_deprecated


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Legacy wrapper of `paper sync --readme-only`.",
    )
    parser.add_argument(
        "--repo",
        type=Path,
        default=Path("."),
        help="Repository root path (default: current directory)",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()

    warn_deprecated(
        legacy_script="src/csv2md_table.py",
        modern_command="paper sync --readme-only",
    )

    bootstrap_repo_imports()
    from paper_cli.commands.sync import sync_readme

    sync_readme(readme_only=True, repo_path=args.repo)
    return 0


if __name__ == "__main__":
    sys.exit(main())
