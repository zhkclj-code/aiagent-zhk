# AI Agent 学习项目：第一阶段

本项目面向已有 Java 后端经验、准备学习 AI Agent 开发的工程师。当前阶段先完成
Python 工程基础、LLM API 实验和一个不依赖 Agent 框架的 Mini Agent。

## 当前内容

```text
aiagent-step1/
├── code/
│   ├── 01-hello-llm/       # LLM 基础调用实验
│   └── python-basics/      # 15 个 Python 基础与 Agent 衔接模块
├── docs/                   # 设计与实施计划
├── notes/                  # 学习路径、练习清单和个人笔记
├── resources/              # 环境配置与学习资源
├── tests/                  # 自动化测试
├── learning-path.md        # 12-16 周总体规划
├── pyproject.toml          # 依赖、测试和质量工具配置
└── requirements.txt        # 兼容旧 pip 工作流的安装入口
```

Python 课程的权威索引见
[code/python-basics/README.md](code/python-basics/README.md)。后续 Prompt、单体 Agent、
RAG 和 Multi-Agent 目录属于学习规划，完成对应阶段时再创建。

## 环境准备

```bash
cd aiagent-step1
python3.11 -m venv .venv
.venv/bin/pip install -e ".[dev]"
```

基础阶段不会默认安装 LangChain、LangGraph、Milvus 等重依赖。进入对应阶段后按需
安装：

```bash
.venv/bin/pip install -e ".[agent-frameworks]"
.venv/bin/pip install -e ".[data]"
```

## 运行与测试

```bash
# 运行第一个课程模块
.venv/bin/python code/python-basics/01-syntax/lesson.py

# 运行全部离线测试
.venv/bin/pytest

# 运行默认 Fake LLM 的 Mini Agent
.venv/bin/python -m mini_agent "计算 2 + 2"
```

测试体系不是为了追求数字，而是保证语法、异步流程、工具调用、错误边界和文档
路径可以在每次改动后重复验证。真实 API 测试默认关闭，不会自动产生费用。

## 学习顺序

1. 按模块 01-06 掌握 Python 与 Java 的核心差异。
2. 重点完成模块 07-10 的异步、类型注解和 pytest。
3. 用模块 11-14 补齐工程实践。
4. 完成模块 15，理解 Agent 循环、工具调用和客户端抽象。
5. 再进入 [learning-path.md](learning-path.md) 中的框架与企业级阶段。
