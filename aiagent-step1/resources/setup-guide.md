# 环境配置指南

## Python 环境

要求 Python 3.11 或更高版本：

```bash
python3 --version
cd aiagent-step1
python3.11 -m venv .venv
.venv/bin/pip install -e ".[dev]"
```

`pyproject.toml` 是依赖和工具配置的权威来源。`requirements.txt` 只保留为兼容入口，
以下命令效果等价：

```bash
.venv/bin/pip install -r requirements.txt
```

基础阶段只安装 OpenAI SDK、Pydantic、python-dotenv 和测试工具。后续阶段按需安装：

```bash
.venv/bin/pip install -e ".[agent-frameworks]"
.venv/bin/pip install -e ".[data]"
```

## 验证环境

```bash
.venv/bin/python --version
.venv/bin/pytest
.venv/bin/ruff --version
.venv/bin/mypy --version
```

## Mini Agent 运行模式

默认 Fake 模式无需 `.env`、API Key 或网络：

```bash
.venv/bin/python -m mini_agent "计算 2 + 2"
```

需要连接 OpenAI 兼容服务时，在项目根目录的 `.env` 中配置：

```bash
MINI_AGENT_PROVIDER=openai
OPENAI_API_KEY=replace_with_your_key
OPENAI_API_BASE=https://api.openai.com/v1
OPENAI_MODEL_NAME=replace_with_available_model
MINI_AGENT_MAX_TOOL_ROUNDS=3
```

`.env` 必须在 `.gitignore` 中，不得提交真实密钥。普通 `.venv/bin/pytest` 会排除
integration 测试，因此不会调用真实服务。

显式运行真实 API 测试：

```bash
.venv/bin/pytest -o addopts="" -m integration tests/mini_agent/test_integration.py
```

## 常用命令

```bash
# 运行课程讲解
.venv/bin/python code/python-basics/07-async/lesson.py

# 运行全部离线测试
.venv/bin/pytest

# 查看 Mini Agent 覆盖率
.venv/bin/pytest --cov=mini_agent --cov-report=term-missing

# 检查新项目代码质量
.venv/bin/ruff check code/python-basics/15-mini-agent/mini_agent tests
.venv/bin/mypy code/python-basics/15-mini-agent/mini_agent
```

## 常见问题

### pytest 没有发现测试

确认当前目录是 `aiagent-step1`，测试文件放在 `tests/`，名称以 `test_` 开头。

### `EmailStr` 提示缺少 email-validator

重新执行 `.venv/bin/pip install -e ".[dev]"`。项目依赖使用
`pydantic[email]` 声明了该扩展。

### 真实客户端提示缺少 API Key

确认 `.env` 位于 `aiagent-step1` 根目录，变量名为 `OPENAI_API_KEY`。只学习离线
流程时不要选择 `openai` provider。
