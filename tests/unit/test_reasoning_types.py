"""Tests for shared native reasoning types."""

import importlib
import importlib.util


def test_reasoning_effort_values_are_centralized_and_immutable():
    """The dependency-free module exposes the complete immutable value set."""
    module_spec = importlib.util.find_spec("kiro.reasoning_types")

    assert module_spec is not None

    reasoning_types = importlib.import_module("kiro.reasoning_types")

    assert isinstance(reasoning_types.REASONING_EFFORT_VALUES, frozenset)
    assert reasoning_types.REASONING_EFFORT_VALUES == frozenset(
        {"none", "low", "medium", "high", "xhigh", "max"}
    )
