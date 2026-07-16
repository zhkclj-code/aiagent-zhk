"""Small, safe tools and their registry."""

import ast
from collections.abc import Callable, Iterable
from datetime import datetime, timezone
import operator
from typing import Any, ClassVar, Protocol

from .errors import ToolError
from .models import ToolCall, ToolResult


class Tool(Protocol):
    """The interface required by the tool registry."""

    name: str
    description: str
    parameters_schema: dict[str, Any]

    def run(self, arguments: dict[str, Any]) -> str:
        """Execute the tool with validated provider arguments."""


class CalculatorTool:
    """Evaluate a deliberately small subset of Python arithmetic."""

    name = "calculator"
    description = "计算只包含数字和基本算术运算符的表达式"
    parameters_schema: ClassVar[dict[str, Any]] = {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "例如 2 + 3 * 4",
            }
        },
        "required": ["expression"],
        "additionalProperties": False,
    }
    _binary_operators: ClassVar[dict[type[ast.operator], Callable[[float, float], float]]] = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
    }
    _unary_operators: ClassVar[dict[type[ast.unaryop], Callable[[float], float]]] = {
        ast.UAdd: operator.pos,
        ast.USub: operator.neg,
    }

    def run(self, arguments: dict[str, Any]) -> str:
        expression = arguments.get("expression")
        if not isinstance(expression, str) or not expression.strip():
            raise ToolError("expression 必须是非空字符串")
        if len(expression) > 200:
            raise ToolError("expression 最长为 200 个字符")

        try:
            parsed = ast.parse(expression, mode="eval")
            result = self._evaluate(parsed.body)
        except (SyntaxError, ArithmeticError, OverflowError) as error:
            raise ToolError(f"无法计算表达式: {error}") from error

        if abs(result) > 1e100:
            raise ToolError("计算结果过大")
        if float(result).is_integer():
            return str(int(result))
        return format(result, ".15g")

    def _evaluate(self, node: ast.expr) -> float:
        if isinstance(node, ast.Constant):
            if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
                raise ToolError("表达式只能包含数字")
            return float(node.value)

        if isinstance(node, ast.UnaryOp):
            operation = self._unary_operators.get(type(node.op))
            if operation is None:
                raise ToolError("不支持该一元运算符")
            return operation(self._evaluate(node.operand))

        if isinstance(node, ast.BinOp):
            operation = self._binary_operators.get(type(node.op))
            if operation is None:
                raise ToolError("不支持该二元运算符")
            left = self._evaluate(node.left)
            right = self._evaluate(node.right)
            if isinstance(node.op, ast.Pow) and abs(right) > 10:
                raise ToolError("指数绝对值不能超过 10")
            return operation(left, right)

        raise ToolError("表达式包含不安全或不支持的语法")


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


class CurrentTimeTool:
    """Return the current UTC time in ISO 8601 format."""

    name = "current_time"
    description = "返回当前 UTC 时间"
    parameters_schema: ClassVar[dict[str, Any]] = {
        "type": "object",
        "properties": {},
        "additionalProperties": False,
    }

    def __init__(self, clock: Callable[[], datetime] = _utc_now) -> None:
        self._clock = clock

    def run(self, arguments: dict[str, Any]) -> str:
        if arguments:
            raise ToolError("current_time 不接受参数")
        return self._clock().isoformat()


class ToolRegistry:
    """Resolve tools, expose provider schemas, and contain tool failures."""

    def __init__(self, tools: Iterable[Tool]) -> None:
        self._tools: dict[str, Tool] = {}
        for tool in tools:
            if tool.name in self._tools:
                raise ToolError(f"工具重复注册: {tool.name}")
            self._tools[tool.name] = tool

    @classmethod
    def default(cls) -> "ToolRegistry":
        return cls([CalculatorTool(), CurrentTimeTool()])

    def schemas(self) -> list[dict[str, Any]]:
        return [
            {
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.parameters_schema,
                },
            }
            for tool in self._tools.values()
        ]

    def execute(self, call: ToolCall) -> ToolResult:
        tool = self._tools.get(call.name)
        if tool is None:
            return self._error_result(call, f"未知工具: {call.name}")

        try:
            content = tool.run(call.arguments)
        except (ToolError, TypeError, ValueError) as error:
            return self._error_result(call, str(error))
        except Exception as error:
            return self._error_result(call, f"工具执行失败: {error}")

        return ToolResult(
            tool_call_id=call.id,
            name=call.name,
            content=content,
        )

    @staticmethod
    def _error_result(call: ToolCall, content: str) -> ToolResult:
        return ToolResult(
            tool_call_id=call.id,
            name=call.name,
            content=content,
            is_error=True,
        )
