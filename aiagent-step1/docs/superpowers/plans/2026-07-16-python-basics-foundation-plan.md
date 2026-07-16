# Python 基础课程完善实施计划

> **面向执行者：** 必须逐任务执行本计划，并严格采用测试先行的 Red-Green-Refactor 流程。推荐使用 `superpowers:subagent-driven-development`，也可以在当前会话中逐项执行。

**目标：** 修复 Python 基础课程的语法与运行问题，统一文件名和文档引用，建立可重复运行的 pytest 测试体系，并新增默认离线、可选连接 OpenAI 兼容接口的 Mini Agent 综合项目。

**架构：** 保留现有 14 个模块目录，把每个模块的文件统一为 `lesson.py` 和 `exercises.py`。测试集中放在 `tests/`，新增项目按模型、错误、客户端、工具、Agent、配置和 CLI 拆分，核心通过 `LLMClient` 协议实现依赖反转。

**技术栈：** Python 3.11、Pydantic v2、OpenAI Python SDK、python-dotenv、pytest、pytest-asyncio、pytest-cov、Ruff、mypy。

---

## 文件结构

新增或调整后的关键结构：

```text
aiagent-step1/
├── pyproject.toml
├── requirements.txt
├── code/python-basics/
│   ├── README.md
│   ├── 01-syntax/{lesson.py,exercises.py}
│   ├── ...
│   ├── 14-generators-re/{lesson.py,exercises.py}
│   └── 15-mini-agent/
│       ├── README.md
│       └── mini_agent/
│           ├── __init__.py
│           ├── __main__.py
│           ├── agent.py
│           ├── cli.py
│           ├── client.py
│           ├── config.py
│           ├── errors.py
│           ├── models.py
│           └── tools.py
└── tests/
    ├── python_basics/
    │   ├── __init__.py
    │   ├── test_course_structure.py
    │   ├── test_lessons.py
    │   └── test_documentation.py
    └── mini_agent/
        ├── test_agent.py
        ├── test_cli.py
        ├── test_client.py
        ├── test_config.py
        ├── test_integration.py
        ├── test_models.py
        └── test_tools.py
```

### 任务 1：建立项目与测试配置

**文件：**

- 创建：`aiagent-step1/pyproject.toml`
- 修改：`aiagent-step1/requirements.txt`

- [ ] **步骤 1：写入权威项目配置**

```toml
[build-system]
requires = ["setuptools>=69"]
build-backend = "setuptools.build_meta"

[project]
name = "aiagent-step1-foundations"
version = "0.1.0"
description = "Python foundations for Java developers learning AI Agent development"
requires-python = ">=3.11"
dependencies = [
  "openai>=1.0,<3.0",
  "pydantic[email]>=2.7,<3.0",
  "python-dotenv>=1.0,<2.0",
]

[project.optional-dependencies]
dev = [
  "pytest>=8.0,<10.0",
  "pytest-asyncio>=0.24,<2.0",
  "pytest-cov>=5.0,<8.0",
  "ruff>=0.9,<1.0",
  "mypy>=1.14,<2.0",
]
agent-frameworks = [
  "langchain>=0.3,<2.0",
  "langchain-openai>=0.3,<2.0",
  "langgraph>=0.2,<2.0",
]
data = [
  "pymilvus>=2.3,<3.0",
  "pgvector>=0.2,<1.0",
  "pandas>=2.0,<3.0",
  "numpy>=1.24,<3.0",
]

[project.scripts]
mini-agent = "mini_agent.cli:main"

[tool.setuptools]
package-dir = {"" = "code/python-basics/15-mini-agent"}

[tool.setuptools.packages.find]
where = ["code/python-basics/15-mini-agent"]
include = ["mini_agent*"]

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["code/python-basics/15-mini-agent"]
asyncio_mode = "auto"
addopts = ["-ra", "-m", "not integration"]
markers = ["integration: requires credentials and a real external API"]

[tool.ruff]
target-version = "py311"
line-length = 100

[tool.mypy]
python_version = "3.11"
strict = true
packages = ["mini_agent"]
mypy_path = "code/python-basics/15-mini-agent"
```

- [ ] **步骤 2：将 requirements.txt 改为兼容入口**

```text
# 兼容旧的 pip 工作流；权威依赖配置位于 pyproject.toml。
-e .[dev]
```

- [ ] **步骤 3：检查配置可被工具读取**

运行：`cd aiagent-step1 && .venv/bin/python -m pytest --collect-only`

预期：pytest 能读取配置；此时可能显示 `no tests collected`，因为测试文件尚未创建。

- [ ] **步骤 4：提交配置**

```bash
git add aiagent-step1/pyproject.toml aiagent-step1/requirements.txt
git commit -m "build: configure Python foundation project"
```

### 任务 2：用失败测试定义统一课程结构

**文件：**

- 创建：`aiagent-step1/tests/python_basics/__init__.py`
- 创建：`aiagent-step1/tests/python_basics/test_course_structure.py`
- 重命名：`aiagent-step1/code/python-basics/01-syntax/*.py` 至 `14-generators-re/*.py`

- [ ] **步骤 1：编写结构测试**

先创建空的 `tests/python_basics/__init__.py`，使课程测试可以稳定使用包内相对导入。

```python
from pathlib import Path


COURSE_ROOT = Path(__file__).parents[2] / "code" / "python-basics"
MODULES = [
    "01-syntax",
    "02-features",
    "03-oop",
    "04-decorators",
    "05-exceptions",
    "06-modules",
    "07-async",
    "08-async-practice",
    "09-type-hints",
    "10-testing",
    "11-project",
    "12-logging",
    "13-dataclasses",
    "14-generators-re",
]


def test_every_foundation_module_has_normalized_files() -> None:
    for module in MODULES:
        module_dir = COURSE_ROOT / module
        assert (module_dir / "lesson.py").is_file(), module
        assert (module_dir / "exercises.py").is_file(), module
```

- [ ] **步骤 2：运行测试并确认失败**

运行：`cd aiagent-step1 && .venv/bin/pytest tests/python_basics/test_course_structure.py -q`

预期：FAIL，首先报告 `01-syntax/lesson.py` 不存在。

- [ ] **步骤 3：执行完整重命名矩阵**

```text
01-syntax/python_vs_java.py                 -> 01-syntax/lesson.py
01-syntax/practice_day1.py                  -> 01-syntax/exercises.py
02-features/pythonic_syntax.py              -> 02-features/lesson.py
02-features/practice_day2.py                -> 02-features/exercises.py
03-oop/oop.py                               -> 03-oop/lesson.py
03-oop/practice_day3.py                     -> 03-oop/exercises.py
04-decorators/decorators.py                 -> 04-decorators/lesson.py
04-decorators/practice_day4.py              -> 04-decorators/exercises.py
05-exceptions/exceptions_and_files.py        -> 05-exceptions/lesson.py
05-exceptions/practice_day5.py               -> 05-exceptions/exercises.py
06-modules/modules_and_packages.py           -> 06-modules/lesson.py
06-modules/practice_day6.py                  -> 06-modules/exercises.py
07-async/async_basics.py                     -> 07-async/lesson.py
07-async/practice_day7.py                    -> 07-async/exercises.py
08-async-practice/async_practice.py          -> 08-async-practice/lesson.py
08-async-practice/practice_day8.py           -> 08-async-practice/exercises.py
09-type-hints/type_hints.py                  -> 09-type-hints/lesson.py
09-type-hints/practice_day10.py              -> 09-type-hints/exercises.py
10-testing/pytest_basics.py                  -> 10-testing/lesson.py
10-testing/practice_day11.py                 -> 10-testing/exercises.py
11-project/comprehensive_project.py          -> 11-project/lesson.py
11-project/practice_day12.py                 -> 11-project/exercises.py
12-logging/logging_basics.py                 -> 12-logging/lesson.py
12-logging/practice_day13.py                 -> 12-logging/exercises.py
13-dataclasses/dataclasses_basics.py         -> 13-dataclasses/lesson.py
13-dataclasses/practice_day14.py             -> 13-dataclasses/exercises.py
14-generators-re/generators.py               -> 14-generators-re/lesson.py
14-generators-re/practice_day15.py           -> 14-generators-re/exercises.py
```

- [ ] **步骤 4：运行结构测试并确认通过**

运行：`cd aiagent-step1 && .venv/bin/pytest tests/python_basics/test_course_structure.py -q`

预期：`1 passed`。

- [ ] **步骤 5：提交结构规范化**

```bash
git add aiagent-step1/code/python-basics aiagent-step1/tests/python_basics/test_course_structure.py
git commit -m "refactor: normalize Python course filenames"
```

### 任务 3：用语法和运行测试复现课程故障

**文件：**

- 创建：`aiagent-step1/tests/python_basics/test_lessons.py`
- 修改：五个已知故障课程文件及异步网络示例

- [ ] **步骤 1：编写 AST 与隔离运行测试**

```python
import ast
import os
from pathlib import Path
import subprocess
import sys

import pytest

from .test_course_structure import COURSE_ROOT, MODULES


@pytest.mark.parametrize("module", MODULES)
@pytest.mark.parametrize("filename", ["lesson.py", "exercises.py"])
def test_course_file_parses(module: str, filename: str) -> None:
    path = COURSE_ROOT / module / filename
    ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


@pytest.mark.parametrize("module", MODULES)
def test_lesson_runs_in_isolated_directory(module: str, tmp_path: Path) -> None:
    lesson = COURSE_ROOT / module / "lesson.py"
    env = os.environ.copy()
    env["RUN_NETWORK_EXAMPLES"] = "0"
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run(
        [sys.executable, str(lesson)],
        cwd=tmp_path,
        env=env,
        capture_output=True,
        text=True,
        timeout=45,
        check=False,
    )
    assert result.returncode == 0, result.stderr
```

- [ ] **步骤 2：运行测试并确认出现已知失败**

运行：`cd aiagent-step1 && .venv/bin/pytest tests/python_basics/test_lessons.py -q -x`

预期：先在 `11-project/exercises.py` 得到 SyntaxError；修复语法后会依次暴露缺少
`test.txt`、硬编码 `python`、缺少邮箱验证依赖和 `sys` 未导入等错误。

- [ ] **步骤 3：修复综合练习字符串边界**

保留每个外层任务说明的 `"""`，把说明内部示例类和方法的 docstring 改为
`'''说明文字'''`，使 `11-project/exercises.py` 中所有代码示例仍位于说明字符串内，
同时避免三引号互相提前闭合。

- [ ] **步骤 4：修复基础语法文件输入依赖**

将固定读取 `test.txt` 的示例替换为自包含临时文件：

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_dir:
    sample_file = Path(temp_dir) / "test.txt"
    sample_file.write_text("Python 文件操作示例", encoding="utf-8")
    content = sample_file.read_text(encoding="utf-8")
    print(content)
```

- [ ] **步骤 5：修复模块课程的解释器选择**

在启动子进程前导入 `sys`，并把命令改为：

```python
result = subprocess.run(
    [sys.executable, "executable.py"],
    capture_output=True,
    text=True,
    cwd=temp_dir,
    check=False,
)
```

- [ ] **步骤 6：修复 Pydantic v2 配置**

```python
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserPydantic(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "张三",
                "age": 25,
                "email": "zhangsan@example.com",
                "tags": ["Python", "AI"],
            }
        }
    )

    name: str = Field(..., min_length=1, max_length=50)
    age: int = Field(..., ge=0, le=150)
    email: EmailStr
    tags: list[str] = Field(default_factory=list)
```

- [ ] **步骤 7：修复测试课程导入和 patch 目标**

在文件导入区加入 `import sys`，并把字符串形式的 `__main__` patch 改成：

```python
@patch.object(sys.modules[__name__], "get_user_name")
def test_with_patch(mock_get_user: MagicMock) -> None:
    mock_get_user.return_value = "Patched User"
    result = get_user_name(1)
    assert result == "Patched User"
```

- [ ] **步骤 8：让网络示例默认关闭**

在 `07-async/lesson.py` 中使用以下入口保护异步 HTTP 示例：

```python
import os

if os.getenv("RUN_NETWORK_EXAMPLES") == "1":
    try:
        import aiohttp
    except ImportError:
        print("未安装 aiohttp，跳过 HTTP 请求示例")
    else:
        asyncio.run(async_http_request())
else:
    print("网络示例默认关闭；设置 RUN_NETWORK_EXAMPLES=1 后运行")
```

- [ ] **步骤 9：安装项目开发依赖并运行测试**

运行：`cd aiagent-step1 && .venv/bin/pip install -e ".[dev]"`

运行：`cd aiagent-step1 && .venv/bin/pytest tests/python_basics/test_lessons.py -q`

预期：28 个解析用例和 14 个隔离运行用例全部通过。

- [ ] **步骤 10：提交运行修复**

```bash
git add aiagent-step1/code/python-basics aiagent-step1/tests/python_basics/test_lessons.py
git commit -m "fix: make Python foundation lessons runnable"
```

### 任务 4：建立 Mini Agent 数据契约

**文件：**

- 创建：`aiagent-step1/tests/mini_agent/test_models.py`
- 创建：`aiagent-step1/code/python-basics/15-mini-agent/mini_agent/{__init__.py,errors.py,models.py}`

- [ ] **步骤 1：编写失败的数据模型测试**

```python
import pytest
from pydantic import ValidationError

from mini_agent.models import LLMReply, Message, ToolCall, ToolResult


def test_llm_reply_requires_content_or_tool_call() -> None:
    with pytest.raises(ValidationError):
        LLMReply()


def test_tool_result_converts_to_tool_message() -> None:
    result = ToolResult(tool_call_id="call-1", name="calculator", content="4")
    assert result.to_message() == Message(
        role="tool",
        content="4",
        name="calculator",
        tool_call_id="call-1",
    )


def test_assistant_message_retains_tool_calls() -> None:
    call = ToolCall(id="call-1", name="calculator", arguments={"expression": "2+2"})
    message = Message(role="assistant", content=None, tool_calls=[call])
    assert message.tool_calls == [call]
```

- [ ] **步骤 2：运行测试并确认失败**

运行：`cd aiagent-step1 && .venv/bin/pytest tests/mini_agent/test_models.py -q`

预期：ERROR，`mini_agent` 尚不存在。

- [ ] **步骤 3：实现错误类型与模型**

`errors.py` 定义：

```python
class MiniAgentError(Exception):
    """Mini Agent 基础异常。"""


class ConfigurationError(MiniAgentError):
    """配置无效。"""


class LLMClientError(MiniAgentError):
    """模型客户端调用失败。"""


class ToolError(MiniAgentError):
    """工具输入或执行失败。"""


class AgentLoopError(MiniAgentError):
    """Agent 超过工具调用轮数上限。"""
```

`models.py` 定义 `ToolCall`、`Message`、`LLMReply`、`ToolResult` 和
`AgentResponse`。使用 `model_validator(mode="after")` 保证 `LLMReply` 至少包含
非空文本或一个工具调用。`ToolResult.to_message()` 返回 role 为 `tool` 的消息。

- [ ] **步骤 4：运行模型测试并确认通过**

运行：`cd aiagent-step1 && .venv/bin/pytest tests/mini_agent/test_models.py -q`

预期：`3 passed`。

- [ ] **步骤 5：提交数据契约**

```bash
git add aiagent-step1/code/python-basics/15-mini-agent aiagent-step1/tests/mini_agent/test_models.py
git commit -m "feat: define Mini Agent data contracts"
```

### 任务 5：实现安全工具与注册表

**文件：**

- 创建：`aiagent-step1/tests/mini_agent/test_tools.py`
- 创建：`aiagent-step1/code/python-basics/15-mini-agent/mini_agent/tools.py`

- [ ] **步骤 1：编写失败的工具行为测试**

```python
from datetime import datetime, timezone

import pytest

from mini_agent.errors import ToolError
from mini_agent.models import ToolCall
from mini_agent.tools import CalculatorTool, CurrentTimeTool, ToolRegistry


def test_calculator_evaluates_allowed_arithmetic() -> None:
    assert CalculatorTool().run({"expression": "2 + 3 * 4"}) == "14"


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
```

- [ ] **步骤 2：运行测试并确认失败**

运行：`cd aiagent-step1 && .venv/bin/pytest tests/mini_agent/test_tools.py -q`

预期：ERROR，`mini_agent.tools` 尚不存在。

- [ ] **步骤 3：实现工具边界**

创建 `Tool` Protocol，要求 `name`、`description`、`parameters_schema` 和
`run(arguments)`。计算器使用 `ast.parse(..., mode="eval")` 递归计算，只允许数字、
加减乘除、整除、取模、有限指数和一元正负号；指数绝对值不得超过 10，表达式最长
200 字符。`ToolRegistry.execute()` 捕获 `ToolError`、Pydantic 参数错误和意外异常，
统一返回 `ToolResult`，不把工具错误传播到 Agent 主循环。

- [ ] **步骤 4：运行工具测试并确认通过**

运行：`cd aiagent-step1 && .venv/bin/pytest tests/mini_agent/test_tools.py -q`

预期：全部通过。

- [ ] **步骤 5：提交工具系统**

```bash
git add aiagent-step1/code/python-basics/15-mini-agent/mini_agent/tools.py aiagent-step1/tests/mini_agent/test_tools.py
git commit -m "feat: add safe Mini Agent tools"
```

### 任务 6：实现客户端协议、Fake 客户端和 OpenAI 适配器

**文件：**

- 创建：`aiagent-step1/tests/mini_agent/test_client.py`
- 创建：`aiagent-step1/code/python-basics/15-mini-agent/mini_agent/client.py`

- [ ] **步骤 1：编写失败的异步客户端测试**

```python
from types import SimpleNamespace

import pytest

from mini_agent.client import FakeLLMClient, OpenAICompatibleClient
from mini_agent.errors import LLMClientError
from mini_agent.models import Message


async def test_fake_client_requests_calculator_for_calculation_prompt() -> None:
    reply = await FakeLLMClient().complete(
        [Message(role="user", content="计算 2 + 2")],
        tools=[],
    )
    assert reply.tool_calls[0].name == "calculator"
    assert reply.tool_calls[0].arguments == {"expression": "2 + 2"}


async def test_fake_client_turns_tool_result_into_final_answer() -> None:
    reply = await FakeLLMClient().complete(
        [Message(role="tool", content="4", name="calculator", tool_call_id="x")],
        tools=[],
    )
    assert reply.content == "工具 calculator 返回：4"


async def test_openai_adapter_normalizes_provider_errors() -> None:
    class BrokenCompletions:
        async def create(self, **kwargs: object) -> object:
            raise RuntimeError("provider down")

    raw_client = SimpleNamespace(
        chat=SimpleNamespace(completions=BrokenCompletions())
    )
    client = OpenAICompatibleClient(raw_client=raw_client, model="demo")

    with pytest.raises(LLMClientError, match="provider down"):
        await client.complete([Message(role="user", content="hello")], tools=[])
```

- [ ] **步骤 2：运行测试并确认失败**

运行：`cd aiagent-step1 && .venv/bin/pytest tests/mini_agent/test_client.py -q`

预期：ERROR，客户端模块尚不存在。

- [ ] **步骤 3：实现客户端协议与映射**

`LLMClient` 是带 `complete(messages, tools) -> LLMReply` 异步方法的 Protocol。
`FakeLLMClient` 支持可选预设回复队列；无预设时按以下确定性规则运行：

- 用户消息以“计算 ”开头时请求 `calculator`
- 用户消息包含“时间”时请求 `current_time`
- 最后一条是工具结果时生成最终文本
- 其他输入返回 `Fake Agent: <输入>`

`OpenAICompatibleClient` 把 `Message` 转换成 OpenAI 消息字典，把工具定义传给
`chat.completions.create`，并将普通响应或 `tool_calls` 转换成 `LLMReply`。所有服务
异常包装为 `LLMClientError` 并使用 `raise ... from error` 保留原因链。

- [ ] **步骤 4：运行客户端测试并确认通过**

运行：`cd aiagent-step1 && .venv/bin/pytest tests/mini_agent/test_client.py -q`

预期：全部通过。

- [ ] **步骤 5：提交客户端实现**

```bash
git add aiagent-step1/code/python-basics/15-mini-agent/mini_agent/client.py aiagent-step1/tests/mini_agent/test_client.py
git commit -m "feat: add fake and OpenAI Agent clients"
```

### 任务 7：实现有边界的 Agent 循环

**文件：**

- 创建：`aiagent-step1/tests/mini_agent/test_agent.py`
- 创建：`aiagent-step1/code/python-basics/15-mini-agent/mini_agent/agent.py`

- [ ] **步骤 1：编写失败的 Agent 行为测试**

```python
import pytest

from mini_agent.agent import MiniAgent
from mini_agent.client import FakeLLMClient
from mini_agent.errors import AgentLoopError
from mini_agent.models import LLMReply, ToolCall
from mini_agent.tools import ToolRegistry


async def test_agent_returns_normal_reply() -> None:
    client = FakeLLMClient(replies=[LLMReply(content="你好")])
    response = await MiniAgent(client, ToolRegistry.default()).run("hello")
    assert response.content == "你好"
    assert response.tool_rounds == 0


async def test_agent_executes_tool_and_returns_final_reply() -> None:
    client = FakeLLMClient(
        replies=[
            LLMReply(
                tool_calls=[
                    ToolCall(id="c1", name="calculator", arguments={"expression": "2+2"})
                ]
            ),
            LLMReply(content="答案是 4"),
        ]
    )
    response = await MiniAgent(client, ToolRegistry.default()).run("计算 2+2")
    assert response.content == "答案是 4"
    assert response.tool_rounds == 1
    assert any(message.role == "tool" and message.content == "4" for message in response.messages)


async def test_agent_exposes_unknown_tool_error_to_model() -> None:
    client = FakeLLMClient(
        replies=[
            LLMReply(tool_calls=[ToolCall(id="c1", name="missing", arguments={})]),
            LLMReply(content="工具不可用"),
        ]
    )
    response = await MiniAgent(client, ToolRegistry.default()).run("调用未知工具")
    tool_message = next(message for message in response.messages if message.role == "tool")
    assert "未知工具" in (tool_message.content or "")


async def test_agent_stops_after_tool_round_limit() -> None:
    calls = [
        LLMReply(tool_calls=[ToolCall(id=f"c{i}", name="current_time", arguments={})])
        for i in range(2)
    ]
    agent = MiniAgent(FakeLLMClient(replies=calls), ToolRegistry.default(), max_tool_rounds=1)
    with pytest.raises(AgentLoopError):
        await agent.run("不断调用工具")
```

- [ ] **步骤 2：运行测试并确认失败**

运行：`cd aiagent-step1 && .venv/bin/pytest tests/mini_agent/test_agent.py -q`

预期：ERROR，Agent 模块尚不存在。

- [ ] **步骤 3：实现 Agent 循环**

`MiniAgent.run()` 追加用户消息，调用客户端，记录 assistant 消息；没有工具调用时
返回 `AgentResponse`。有工具调用时先检查轮次上限，再逐个调用注册表并追加 tool
消息。历史在实例内保留，`clear_history()` 可以显式清空。默认最多三轮工具调用。

- [ ] **步骤 4：运行 Agent 测试并确认通过**

运行：`cd aiagent-step1 && .venv/bin/pytest tests/mini_agent/test_agent.py -q`

预期：`4 passed`。

- [ ] **步骤 5：提交 Agent 核心**

```bash
git add aiagent-step1/code/python-basics/15-mini-agent/mini_agent/agent.py aiagent-step1/tests/mini_agent/test_agent.py
git commit -m "feat: implement bounded Mini Agent loop"
```

### 任务 8：实现配置、客户端工厂和 CLI

**文件：**

- 创建：`aiagent-step1/tests/mini_agent/test_config.py`
- 创建：`aiagent-step1/tests/mini_agent/test_cli.py`
- 创建：`aiagent-step1/tests/mini_agent/test_integration.py`
- 创建：`aiagent-step1/code/python-basics/15-mini-agent/mini_agent/{config.py,cli.py,__main__.py}`

- [ ] **步骤 1：编写失败的配置与 CLI 测试**

```python
import pytest

from mini_agent.client import FakeLLMClient
from mini_agent.config import AgentSettings, create_client
from mini_agent.errors import ConfigurationError


def test_settings_default_to_fake(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("MINI_AGENT_PROVIDER", raising=False)
    assert AgentSettings.from_env().provider == "fake"


def test_real_provider_requires_api_key() -> None:
    settings = AgentSettings(provider="openai", api_key=None)
    with pytest.raises(ConfigurationError, match="OPENAI_API_KEY"):
        create_client(settings)


def test_fake_provider_creates_fake_client() -> None:
    assert isinstance(create_client(AgentSettings()), FakeLLMClient)
```

`test_cli.py`：

```python
from mini_agent.cli import run_cli


async def test_cli_runs_offline_calculator(capsys) -> None:
    exit_code = await run_cli(["计算 2 + 2"])
    output = capsys.readouterr().out
    assert exit_code == 0
    assert "4" in output
```

`test_integration.py` 只在显式选择 integration marker 且已配置 API Key 时调用真实
服务：

```python
import os

import pytest

from mini_agent.config import AgentSettings, create_client
from mini_agent.models import Message


@pytest.mark.integration
async def test_real_openai_compatible_client() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        pytest.skip("OPENAI_API_KEY 未配置")
    settings = AgentSettings.from_env(provider_override="openai")
    client = create_client(settings)
    reply = await client.complete([Message(role="user", content="只回复 ok")], tools=[])
    assert reply.content
```

- [ ] **步骤 2：运行测试并确认失败**

运行：`cd aiagent-step1 && .venv/bin/pytest tests/mini_agent/test_config.py tests/mini_agent/test_cli.py -q`

预期：ERROR，配置和 CLI 模块尚不存在。

- [ ] **步骤 3：实现环境配置与客户端工厂**

`AgentSettings` 使用冻结 dataclass，字段为 provider、api_key、base_url、model 和
max_tool_rounds。`from_env(provider_override=None)` 读取 `MINI_AGENT_PROVIDER`、`OPENAI_API_KEY`、
`OPENAI_API_BASE`、`OPENAI_MODEL_NAME` 和 `MINI_AGENT_MAX_TOOL_ROUNDS`。
传入 provider_override 时优先使用它。provider 只允许 `fake` 与 `openai`；真实
provider 必须有 API Key。

- [ ] **步骤 4：实现 CLI**

`run_cli(argv)` 使用 argparse 接收一个问题和可选 `--provider`。未传问题时进入
交互循环，输入 `quit` 或 `exit` 结束。`main()` 使用 `asyncio.run()` 并将返回值
交给 `SystemExit`。`__main__.py` 调用 `main()`，支持：

```bash
python -m mini_agent "计算 2 + 2"
```

- [ ] **步骤 5：运行配置与 CLI 测试并确认通过**

运行：`cd aiagent-step1 && .venv/bin/pytest tests/mini_agent/test_config.py tests/mini_agent/test_cli.py -q`

预期：全部通过，且不访问网络。

- [ ] **步骤 6：提交配置与入口**

```bash
git add aiagent-step1/code/python-basics/15-mini-agent/mini_agent aiagent-step1/tests/mini_agent
git commit -m "feat: add Mini Agent configuration and CLI"
```

### 任务 9：规范文档名称与引用

**文件：**

- 创建：`aiagent-step1/code/python-basics/README.md`
- 创建：`aiagent-step1/code/python-basics/15-mini-agent/README.md`
- 创建：`aiagent-step1/tests/python_basics/test_documentation.py`
- 修改：`aiagent-step1/README.md`
- 修改：`aiagent-step1/notes/01-基础准备/Python学习路径.md`
- 修改：`aiagent-step1/notes/01-基础准备/练习文件清单.md`
- 修改：`aiagent-step1/resources/setup-guide.md`

- [ ] **步骤 1：编写失败的文档一致性测试**

```python
import re
from pathlib import Path

from .test_course_structure import COURSE_ROOT, MODULES


PROJECT_ROOT = COURSE_ROOT.parents[1]
COURSE_DOCS = [
    PROJECT_ROOT / "README.md",
    PROJECT_ROOT / "notes" / "01-基础准备" / "Python学习路径.md",
    PROJECT_ROOT / "notes" / "01-基础准备" / "练习文件清单.md",
    COURSE_ROOT / "README.md",
]


def test_course_docs_do_not_reference_stale_filenames() -> None:
    stale_names = (
        "practice_day",
        "_exercises.py",
        "python_vs_java.py",
        "pythonic_syntax.py",
        "oop.py",
        "decorators.py",
        "exceptions_and_files.py",
        "modules_and_packages.py",
        "async_basics.py",
        "async_practice.py",
        "type_hints.py",
        "pytest_basics.py",
        "comprehensive_project.py",
        "logging_basics.py",
        "dataclasses_basics.py",
        "generators.py",
    )
    for document in COURSE_DOCS:
        content = document.read_text(encoding="utf-8")
        assert not any(name in content for name in stale_names), document


def test_course_index_references_every_module_file() -> None:
    content = (COURSE_ROOT / "README.md").read_text(encoding="utf-8")
    for module in MODULES:
        assert f"{module}/lesson.py" in content
        assert f"{module}/exercises.py" in content
    assert "15-mini-agent/README.md" in content


def test_backticked_course_paths_exist() -> None:
    pattern = re.compile(r"`(code/python-basics/[^`]+)`")
    for document in COURSE_DOCS:
        for relative_path in pattern.findall(document.read_text(encoding="utf-8")):
            assert (PROJECT_ROOT / relative_path).exists(), f"{document}: {relative_path}"
```

- [ ] **步骤 2：运行测试并确认失败**

运行：`cd aiagent-step1 && .venv/bin/pytest tests/python_basics/test_documentation.py -q`

预期：FAIL，旧文件名仍存在，课程索引尚未创建。

- [ ] **步骤 3：创建完整课程索引**

`code/python-basics/README.md` 使用 15 行表格，逐行列出模块编号、主题、
`<目录>/lesson.py`、`<目录>/exercises.py`；模块 15 指向
`15-mini-agent/README.md`。文档说明统一执行方式：

```bash
cd aiagent-step1
.venv/bin/python code/python-basics/01-syntax/lesson.py
.venv/bin/pytest
```

- [ ] **步骤 4：更新学习路径和练习清单**

把 Day 1-15 改为模块 01-15，删除不存在的 `oop_exercises.py`、
`async_llm_exercises.py`、`mini_agent_exercises.py` 等引用，统一指向
`lesson.py` 与 `exercises.py`。修正 Java 对比表：

```markdown
| 特性 | Java | Python |
|---|---|---|
| 接口 | `interface` | `Protocol`、ABC、鸭子类型 |
| 泛型 | `<T>` | `TypeVar`、`Generic`、内置泛型语法 |
| I/O 并发 | 线程、虚拟线程、CompletableFuture | `asyncio` 协程 |
| CPU 并行 | 多线程 | 多进程、原生扩展；需理解 GIL 影响 |
| 包管理 | Maven、Gradle | `pyproject.toml`、pip、uv 等 |
```

- [ ] **步骤 5：更新项目 README 与安装说明**

README 的目录树只展示真实存在目录，增加 `python-basics` 和测试入口。安装说明改为：

```bash
cd aiagent-step1
python3.11 -m venv .venv
.venv/bin/pip install -e ".[dev]"
.venv/bin/pytest
```

框架扩展安装使用 `.[agent-frameworks]`，数据扩展使用 `.[data]`。

- [ ] **步骤 6：编写 Mini Agent 使用文档**

记录默认离线命令、真实客户端环境变量、可用工具、错误行为和可选 integration
测试。文档不得出现真实 Key、Cookie 或内部认证信息。

- [ ] **步骤 7：运行文档测试并确认通过**

运行：`cd aiagent-step1 && .venv/bin/pytest tests/python_basics/test_documentation.py -q`

预期：`3 passed`。

- [ ] **步骤 8：提交文档规范化**

```bash
git add aiagent-step1/README.md aiagent-step1/code/python-basics aiagent-step1/notes aiagent-step1/resources aiagent-step1/tests/python_basics/test_documentation.py
git commit -m "docs: normalize Python foundation references"
```

### 任务 10：完成全量验证与质量收尾

**文件：**

- 修改：仅修改验证暴露出的本任务范围内文件

- [ ] **步骤 1：运行完整测试套件**

运行：`cd aiagent-step1 && .venv/bin/pytest`

预期：全部通过；输出中没有未注册 marker、弃用警告或网络请求错误。

- [ ] **步骤 2：运行覆盖率报告**

运行：`cd aiagent-step1 && .venv/bin/pytest --cov=mini_agent --cov-report=term-missing`

预期：核心分支均被执行；重点检查 Agent 循环、工具错误和配置校验，不以单一百分比
代替缺失行为检查。

- [ ] **步骤 3：运行新项目静态检查**

运行：`cd aiagent-step1 && .venv/bin/ruff check code/python-basics/15-mini-agent/mini_agent tests/mini_agent tests/python_basics`

运行：`cd aiagent-step1 && .venv/bin/mypy code/python-basics/15-mini-agent/mini_agent`

预期：两条命令均成功退出。

- [ ] **步骤 4：验证离线 CLI**

运行：`cd aiagent-step1 && .venv/bin/python -m mini_agent "计算 2 + 2"`

预期：输出包含 `4`，不需要 API Key，不访问网络。

- [ ] **步骤 5：检查工作区卫生**

运行：`git status --short`

预期：只包含计划内源代码、测试和文档；没有 `__pycache__`、`.pytest_cache`、日志、
临时输出或密钥文件。

- [ ] **步骤 6：提交最终收尾**

```bash
git add aiagent-step1
git commit -m "test: verify Python Agent foundations"
```
