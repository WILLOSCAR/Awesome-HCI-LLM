#!/usr/bin/env python3
"""Helpers for lightweight legacy-script wrappers."""

from __future__ import annotations

import warnings
from pathlib import Path
import sys


def bootstrap_repo_imports() -> None:
    """Ensure repository root is importable when running scripts under src/."""
    repo_root = Path(__file__).resolve().parents[1]
    repo_root_s = str(repo_root)
    if repo_root_s not in sys.path:
        sys.path.insert(0, repo_root_s)


def warn_deprecated(*, legacy_script: str, modern_command: str) -> None:
    """Emit a short deprecation warning for legacy entrypoints."""
    message = (
        f"{legacy_script} is deprecated. "
        f"Please use: {modern_command}"
    )
    warnings.warn(message, DeprecationWarning, stacklevel=2)
    print(f"⚠️  {message}")
