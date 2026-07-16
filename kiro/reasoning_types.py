"""Dependency-free shared types for native reasoning configuration."""

from typing import Final, FrozenSet, Literal


ReasoningEffort = Literal["none", "low", "medium", "high", "xhigh", "max"]

REASONING_EFFORT_VALUES: Final[FrozenSet[ReasoningEffort]] = frozenset(
    {"none", "low", "medium", "high", "xhigh", "max"}
)
