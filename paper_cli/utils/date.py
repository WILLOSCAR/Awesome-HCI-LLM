"""Date parsing helpers used across the CLI.

The library stores dates as strings in (ideally) 'YYYY.MM' format, but some
legacy rows may contain extra text. These helpers extract a normalized value
for robust sorting/filtering.
"""

from __future__ import annotations

import re
from typing import Optional, Tuple


_YYYY_MM_RE = re.compile(r"(20\d{2})\.(\d{2})")


def extract_yyyymm(value: str) -> Optional[str]:
    """Extract a normalized 'YYYY.MM' from a string.

    Returns None if no valid pattern is found.
    """
    if not value:
        return None

    m = _YYYY_MM_RE.search(str(value))
    if not m:
        return None

    year = int(m.group(1))
    month = int(m.group(2))
    if month < 1 or month > 12:
        return None

    return f"{year:04d}.{month:02d}"


def date_key(value: str) -> Optional[Tuple[int, int]]:
    """Return (year, month) for comparisons/sorting, or None if invalid."""
    yyyymm = extract_yyyymm(value)
    if not yyyymm:
        return None
    year_s, month_s = yyyymm.split(".")
    return int(year_s), int(month_s)

