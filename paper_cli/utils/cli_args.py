"""Helpers for safely calling Typer command functions as plain Python."""

from __future__ import annotations

from typing import Any, TypeVar, cast

from typer.models import ArgumentInfo, OptionInfo

T = TypeVar("T")


def resolve_cli_value(value: T) -> T:
    """Resolve Typer's ArgumentInfo/OptionInfo placeholders to concrete defaults.

    Typer commands can be called as plain functions in tests or wrappers. In that
    case, omitted arguments may still be `ArgumentInfo`/`OptionInfo` objects.
    """
    if isinstance(value, (ArgumentInfo, OptionInfo)):
        return cast(T, value.default)
    return cast(T, value)


def resolve_cli_values(*values: Any) -> tuple[Any, ...]:
    """Vectorized variant of `resolve_cli_value`."""
    return tuple(resolve_cli_value(v) for v in values)
