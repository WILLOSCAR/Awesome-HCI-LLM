#!/usr/bin/env python3
"""Legacy wrapper for adding arXiv papers.

Prefer the modern CLI:
    paper add <ARXIV_LINK_OR_ID> <TOPIC> [OPTIONS]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from _legacy_cli_bridge import bootstrap_repo_imports, warn_deprecated


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Legacy wrapper of `paper add` for backward compatibility.",
    )
    parser.add_argument("arxiv_link_or_id", help="arXiv URL or ID, e.g. 2312.00752")
    parser.add_argument("topic", help="Topic, e.g. HCI / LLM / Agent")
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
        legacy_script="src/add_arxiv_paper.py",
        modern_command=f"paper add {args.arxiv_link_or_id} {args.topic}",
    )

    bootstrap_repo_imports()
    import typer
    from paper_cli.commands.add import add_paper

    try:
        # Keep legacy behavior: add only, do not auto-sync README or run git operations.
        add_paper(
            link=args.arxiv_link_or_id,
            topic=args.topic,
            no_sync=True,
            no_git=True,
            repo_path=args.repo,
        )
        print()
        print("💡 Legacy mode only added CSV row. Use `paper sync --readme-only` when needed.")
        return 0
    except typer.Exit as exc:
        return int(exc.exit_code)


if __name__ == "__main__":
    sys.exit(main())
