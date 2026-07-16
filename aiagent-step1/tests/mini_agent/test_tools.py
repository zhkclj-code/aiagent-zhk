from datetime import datetime, timezone

import pytest

from mini_agent.errors import ToolError
from mini_agent.models import ToolCall
from mini_agent.tools import CalculatorTool, CurrentTimeTool, ToolRegistry


def test_calculator_evaluates_allowed_arithmetic() -> None:
    assert CalculatorTool().run({"expression": "2 + 3 * 4"}) == "14"


def test_calculator_rejects_unexpected_arguments() -> None:
    with pytest.raises(ToolError, match="不支持的参数"):
        CalculatorTool().run({"expression": "2 + 2", "unexpected": True})


@pytest.mark.parametrize("expression", ["__import__('os')", "2 ** 100", "name + 1"])
def test_calculator_rejects_unsafe_expressions(expression: str) -> None:
    with pytest.raises(ToolError):
        CalculatorTool().run({"expression": expression})


def test_current_time_uses_injected_clock() -> None:
    fixed = datetime(2026, 7, 16, 8, 0, tzinfo=timezone.utc)
    tool = CurrentTimeTool(clock=lambda: fixed)
    assert tool.run({}) == "2026-07-16T08:00:00+00:00"


def test_registry_returns_structured_error_for_unknown_tool() -> None:
    result = ToolRegistry.default().execute(ToolCall(id="x", name="missing", arguments={}))
    assert result.is_error is True
    assert "未知工具" in result.content
