# Python 基础课程索引

每个基础模块使用统一文件名：`lesson.py` 是可运行讲解，`exercises.py` 是练习。

| 模块 | 主题 | 讲解 | 练习 |
|---|---|---|---|
| 01 | 基础语法与 Java 对比 | `01-syntax/lesson.py` | `01-syntax/exercises.py` |
| 02 | Pythonic 语法 | `02-features/lesson.py` | `02-features/exercises.py` |
| 03 | 面向对象 | `03-oop/lesson.py` | `03-oop/exercises.py` |
| 04 | 装饰器与上下文管理器 | `04-decorators/lesson.py` | `04-decorators/exercises.py` |
| 05 | 异常与文件 | `05-exceptions/lesson.py` | `05-exceptions/exercises.py` |
| 06 | 模块与包 | `06-modules/lesson.py` | `06-modules/exercises.py` |
| 07 | 异步基础 | `07-async/lesson.py` | `07-async/exercises.py` |
| 08 | 异步实践 | `08-async-practice/lesson.py` | `08-async-practice/exercises.py` |
| 09 | 类型注解与 Pydantic | `09-type-hints/lesson.py` | `09-type-hints/exercises.py` |
| 10 | pytest | `10-testing/lesson.py` | `10-testing/exercises.py` |
| 11 | Python 综合练习 | `11-project/lesson.py` | `11-project/exercises.py` |
| 12 | 日志 | `12-logging/lesson.py` | `12-logging/exercises.py` |
| 13 | Dataclasses | `13-dataclasses/lesson.py` | `13-dataclasses/exercises.py` |
| 14 | 生成器、正则与 pathlib | `14-generators-re/lesson.py` | `14-generators-re/exercises.py` |
| 15 | Mini Agent 综合项目 | `15-mini-agent/README.md` | 项目测试驱动练习 |

## 运行方式

从 `aiagent-step1` 目录执行：

```bash
.venv/bin/python code/python-basics/01-syntax/lesson.py
.venv/bin/python code/python-basics/01-syntax/exercises.py
.venv/bin/pytest
```

讲解脚本默认不访问外部网络。模块 07 的网络示例需要显式设置
`RUN_NETWORK_EXAMPLES=1`。
