# Python 学习路径（Java 开发者版）

## 学习目标

这套课程不是让 Java 开发者重新学习变量和循环，而是集中掌握 Python 特有语法、
异步 I/O、类型系统和工程化能力，最终能独立阅读和开发 AI Agent 项目。

## 模块顺序

| 模块 | 主题 | Agent 开发中的用途 |
|---|---|---|
| 01 | 基础语法与 Java 对比 | 快速建立语法映射 |
| 02 | Pythonic 语法 | 简化数据转换和消息处理 |
| 03 | 面向对象 | 组织客户端、工具和 Agent |
| 04 | 装饰器与上下文管理器 | 中间件、追踪、资源释放 |
| 05 | 异常与文件 | 配置、持久化和错误边界 |
| 06 | 模块与包 | 建立可维护的项目结构 |
| 07 | 异步基础 | 并发调用模型和外部工具 |
| 08 | 异步实践 | 限流、队列、重试和任务协作 |
| 09 | 类型注解与 Pydantic | 工具参数和结构化输出校验 |
| 10 | pytest | 自动验证异步流程和异常分支 |
| 11 | Python 综合练习 | 汇总前述工程能力 |
| 12 | logging | 记录模型请求和工具执行过程 |
| 13 | dataclasses | 表达内部状态和不可变记录 |
| 14 | 生成器、正则、pathlib | 流式输出、文本处理和路径操作 |
| 15 | Mini Agent | 串联客户端、工具、循环和测试 |

完整文件索引见 `code/python-basics/README.md`。

## 建议节奏

- 模块 01-06：3-5 天。Java 已掌握的概念快速过，重点记录差异。
- 模块 07-10：5-7 天。需要实际编写异步代码和测试，不能只阅读。
- 模块 11-14：3-4 天。形成日志、数据模型和流式处理习惯。
- 模块 15：2-3 天。先使用 Fake LLM，再选择是否连接真实 API。

每天建议执行：

```bash
.venv/bin/python code/python-basics/01-syntax/lesson.py
.venv/bin/python code/python-basics/01-syntax/exercises.py
.venv/bin/pytest
```

## Python 与 Java 的准确对比

| 特性 | Java | Python |
|---|---|---|
| 类型检查 | 编译期静态类型 | 运行时动态类型，可用类型注解做静态检查 |
| 接口 | `interface` | `Protocol`、ABC、鸭子类型 |
| 泛型 | `<T>` | `TypeVar`、`Generic`、内置泛型语法 |
| I/O 并发 | 线程、虚拟线程、`CompletableFuture` | `asyncio` 协程，也支持线程 |
| CPU 并行 | 多线程 | 多进程或原生扩展，需要理解 GIL 影响 |
| 资源管理 | `try-with-resources` | `with`、同步与异步上下文管理器 |
| 包与构建 | Maven、Gradle | `pyproject.toml`、pip、uv 等工具 |
| 数据校验 | Bean Validation、Jackson | Pydantic、dataclasses |

`asyncio` 不是 Python 多线程的别名。它主要解决 I/O 等待期间的并发调度；CPU 密集
任务通常需要多进程、原生扩展或外部计算服务。

## 基础阶段验收

- 能解释协程、线程和进程的区别。
- 能用 `asyncio.gather`、超时和并发限制处理多个 I/O 任务。
- 能用 Pydantic 定义并校验工具参数。
- 能用 pytest、pytest-asyncio 和 Mock 测试异步代码。
- 能运行 `python -m mini_agent "计算 2 + 2"` 并解释完整工具调用流程。
- 不依赖 LangChain 也能说明 Agent 的“模型决策、工具执行、结果回传”循环。
