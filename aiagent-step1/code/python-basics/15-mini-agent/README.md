# 模块 15：Mini Agent 综合项目

这个项目不依赖 LangChain 或 LangGraph，用原生 Python 展示 Agent 的核心循环：

```text
用户消息 -> 模型决策 -> 工具调用 -> 工具结果 -> 模型最终回答
```

## 默认离线运行

```bash
cd aiagent-step1
.venv/bin/python -m mini_agent "计算 2 + 2"
.venv/bin/python -m mini_agent "现在是什么时间"
```

Fake LLM 是默认客户端，会确定性地选择计算器或当前时间工具。它不读取 API Key、
不访问网络，也不会产生模型费用。

## 项目结构

- `mini_agent/models.py`：消息、工具调用和响应模型
- `mini_agent/tools.py`：安全计算器、时间工具和工具注册表
- `mini_agent/client.py`：Fake 与 OpenAI 兼容异步客户端
- `mini_agent/agent.py`：有轮次上限的工具调用循环
- `mini_agent/config.py`：环境配置和客户端工厂
- `mini_agent/cli.py`：命令行入口

## 真实客户端

在 `.env` 中设置 `MINI_AGENT_PROVIDER=openai`、`OPENAI_API_KEY`、
`OPENAI_API_BASE` 和 `OPENAI_MODEL_NAME`，然后运行：

```bash
.venv/bin/python -m mini_agent --provider openai "用一句话解释 AI Agent"
```

真实 API 的工具调用能力取决于所选 OpenAI 兼容服务和模型。缺少 Key 时程序会在
发送请求前报错。

## 测试体系

```bash
# 默认离线测试
.venv/bin/pytest tests/mini_agent

# 覆盖率
.venv/bin/pytest --cov=mini_agent --cov-report=term-missing

# 显式真实 API 测试，会产生调用
.venv/bin/pytest -o addopts="" -m integration tests/mini_agent/test_integration.py
```

测试通过依赖注入 Fake 客户端验证普通回答、工具调用、未知工具、模型服务异常和
循环上限。integration 测试默认排除。
