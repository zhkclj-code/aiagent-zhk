"""
Day 13: Python 日志系统

学习目标：掌握 logging 模块，告别 print 调试
"""

import logging
import sys
from datetime import datetime
from pathlib import Path


# ================================
# 0. Python logging vs Java日志框架 - 开发者必读
# ================================

"""
【Python logging vs Java Log4j2/Logback对比】

| 维度 | Python logging | Log4j2/Logback |
|-----|---------------|----------------|
| 核心组件 | Logger, Handler, Formatter, Filter | Logger, Appender, Layout, Filter |
| 层级命名 | 点号分隔（app.module.sub） | 包名继承（com.app.module） |
| 配置方式 | basicConfig() 或 dictConfig | XML/YAML配置文件 |
| 性能 | 简单够用 | 异步Appender、高吞吐 |
| 生态 | 标准库 | 企业级（ELK、Splunk集成） |

【核心概念映射】

Python logging        Java Logback/Log4j2
─────────────────────────────────────────
Logger               Logger
Handler              Appender
Formatter            Layout
Filter               Filter
logging.basicConfig  logback.xml / log4j2.xml
dictConfig           YAML配置

【组件职责】

Logger（记录器）：
- 对应模块/类名（如 "app.service.UserService"）
- 设置日志级别（DEBUG/INFO/WARNING/ERROR/CRITICAL）
- 将日志事件传递给Handler

Handler（处理器）：
- 定义日志输出目标（控制台、文件、网络）
- 每个Logger可以有多个Handler
- 常用Handler：StreamHandler, FileHandler, RotatingFileHandler

Formatter（格式化器）：
- 定义日志格式（时间、级别、消息、位置）
- 示例：'%(asctime)s - %(name)s - %(levelname)s - %(message)s'

Filter（过滤器）：
- 细粒度过滤（按模块、级别、消息内容）

【和Java日志框架的关键差异】

1. 配置方式：
   Python:
   logging.basicConfig(
       level=logging.INFO,
       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
       handlers=[logging.FileHandler('app.log')]
   )

   Java (Logback):
   <appender name="FILE" class="ch.qos.logback.core.FileAppender">
       <file>app.log</file>
       <encoder>
           <pattern>%d{yyyy-MM-dd HH:mm:ss} - %logger{36} - %level - %msg%n</pattern>
       </encoder>
   </appender>

2. 层级命名：
   Python: 点号分隔字符串
   logger = logging.getLogger('app.service.user')

   Java: 包名继承
   Logger logger = LoggerFactory.getLogger(UserService.class);

3. 性能考量：
   Python: 单进程够用，高并发需考虑队列Handler
   Java: 异步Appender，Disruptor高性能队列

【使用场景对比】

✅ Python logging适用：
- 单体应用、微服务
- 标准化日志输出
- 结构化日志（JSON格式）
- 集成到ELK/Loki

✅ Log4j2/Logback优势：
- 高并发场景（异步日志）
- 企业级日志聚合
- 复杂过滤规则
- 性能监控集成

【最佳实践】

1. 日志级别选择：
   DEBUG: 开发调试信息（变量值、执行流程）
   INFO: 关键业务流程（用户登录、订单创建）
   WARNING: 潜在问题（配置缺失、性能下降）
   ERROR: 错误但可恢复（数据库连接失败、API超时）
   CRITICAL: 严重错误（系统崩溃、数据丢失）

2. 结构化日志：
   import json
   import logging

   class JsonFormatter(logging.Formatter):
       def format(self, record):
           return json.dumps({
               'timestamp': self.formatTime(record),
               'level': record.levelname,
               'message': record.getMessage(),
               'module': record.module,
               'line': record.lineno
           })

3. 日志文件管理：
   - 使用RotatingFileHandler自动轮转
   - 使用TimedRotatingFileHandler按时间切割
   - 配置日志保留策略（大小、天数）

4. 敏感信息：
   ❌ 不要记录密码、密钥、个人隐私
   ✅ 用占位符或脱敏处理

【Java开发者迁移建议】

Logback配置 → Python logging.dictConfig:

LOGGING = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': 'INFO'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'app.log',
            'maxBytes': 10485760,  # 10MB
            'backupCount': 5,
            'formatter': 'standard'
        }
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO'
    }
}
"""

# ================================
# 1. print vs logging
# ================================

# print 的问题：
# - 无法控制输出级别
# - 无法同时输出到文件和控制台
# - 无法添加时间戳、行号等上下文
# - 在生产环境要么全删，要么全留

# logging 的优势：
# - 按级别过滤（DEBUG < INFO < WARNING < ERROR < CRITICAL）
# - 同时输出到多个目标（控制台 + 文件）
# - 自动添加时间戳、模块名、行号
# - 运行时动态调整级别

print("=== print 方式 ===")
print("这条调试信息在线上怎么关？")

print("\n=== logging 方式 ===")
logging.basicConfig(level=logging.INFO)
logging.debug("DEBUG: 不会被显示（级别不够）")
logging.info("INFO: 这条会显示")
logging.warning("WARNING: 这条也会显示")


# ================================
# 2. 日志级别
# ================================

# 五个级别，数值越大越严重
# DEBUG(10) < INFO(20) < WARNING(30) < ERROR(40) < CRITICAL(50)

def demo_log_levels():
    logger = logging.getLogger("level_demo")
    logger.setLevel(logging.DEBUG)

    logger.debug("调试信息 - 变量值、中间状态")
    logger.info("一般信息 - 请求开始、任务完成")
    logger.warning("警告 - 重试中、降级处理")
    logger.error("错误 - 捕获异常、操作失败")
    logger.critical("严重错误 - 系统崩溃、数据丢失")


print("\n日志级别演示:")
demo_log_levels()


# ================================
# 3. Logger 基本配置
# ================================

# 方式 1：basicConfig（简单场景）
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)

logger = logging.getLogger("my_app")
logger.info("basicConfig 配置完成")


# 方式 2：编程式配置（推荐）
def create_logger(name: str, log_file: str = None) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)-7s] [%(name)s] %(message)s",
        datefmt="%H:%M:%S"
    )

    # 控制台 Handler
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)
    logger.addHandler(console)

    # 文件 Handler（可选）
    if log_file:
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


print("\n编程式配置:")
custom_logger = create_logger("custom", "/tmp/agent.log")
custom_logger.info("同时输出到控制台和文件")


# ================================
# 4. Agent 场景实战
# ================================

class AgentLogger:
    """AI Agent 专用日志器"""

    def __init__(self, name: str, log_dir: str = "./logs"):
        Path(log_dir).mkdir(exist_ok=True)

        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter(
            "[%(asctime)s] [%(levelname)-5s] %(message)s",
            datefmt="%H:%M:%S"
        )

        # 控制台：只显示 INFO 以上
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(fmt)
        self.logger.addHandler(console)

        # 文件：记录所有级别
        today = datetime.now().strftime("%Y%m%d")
        file_handler = logging.FileHandler(
            f"{log_dir}/{name}_{today}.log", encoding="utf-8"
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(fmt)
        self.logger.addHandler(file_handler)

    def task_start(self, task_id: str, task_name: str):
        self.logger.info("▶ 任务开始 [%s] %s", task_id, task_name)

    def task_end(self, task_id: str, result: str):
        self.logger.info("✓ 任务完成 [%s] → %s", task_id, result)

    def llm_call(self, model: str, tokens: int, latency: float):
        self.logger.debug(
            "LLM 调用 | model=%s tokens=%d latency=%.2fs",
            model, tokens, latency
        )

    def retry(self, attempt: int, error: str):
        self.logger.warning("↻ 重试 %d/3: %s", attempt, error)

    def error(self, task_id: str, exception: Exception):
        self.logger.error(
            "✗ 任务失败 [%s] %s: %s",
            task_id, type(exception).__name__, str(exception)
        )


print("\nAgent 日志器演示:")
agent_log = AgentLogger("MyAgent")
agent_log.task_start("001", "解析用户意图")
agent_log.llm_call("glm-5.2", 350, 0.85)
agent_log.retry(1, "timeout")
agent_log.task_end("001", "意图: 查询天气")
agent_log.error("002", ValueError("城市名称为空"))


# ================================
# 5. 异常日志记录
# ================================

def risky_operation(value: str):
    logger = logging.getLogger("risky")
    try:
        result = int(value)
        logger.info("转换成功: %s → %d", value, result)
        return result
    except ValueError as e:
        logger.exception("转换失败: %s", value)    # 自动附加堆栈
    except Exception as e:
        logger.error("未知错误: %s", e, exc_info=True)  # 手动附加堆栈


print("\n异常日志:")
risky_operation("123")
risky_operation("abc")


# ================================
# 6. 日志分级策略
# ================================

# 线上 Agent 部署时：
# - 开发环境：DEBUG（全量日志）
# - 测试环境：INFO（关键流程）
# - 生产环境：WARNING（只记录异常）

import os

env = os.getenv("ENV", "development")

level_map = {
    "development": logging.DEBUG,
    "staging": logging.INFO,
    "production": logging.WARNING,
}

env_logger = logging.getLogger("env_demo")
env_logger.setLevel(level_map.get(env, logging.INFO))
env_logger.addHandler(logging.StreamHandler())

env_logger.debug("当前环境: %s (级别: DEBUG)", env)
print(f"\n环境 '{env}' → 日志级别: {logging.getLevelName(env_logger.level)}")


# ================================
# 7. 结构化日志
# ================================

import json

def log_structured(logger: logging.Logger, event: str, **kwargs):
    """结构化日志（方便后续分析）"""
    data = {"event": event, "timestamp": datetime.now().isoformat(), **kwargs}
    logger.info(json.dumps(data, ensure_ascii=False))


print("\n结构化日志:")
sl = logging.getLogger("structured")
sl.setLevel(logging.INFO)
sl.addHandler(logging.StreamHandler())

log_structured(sl, "llm_request",
    model="glm-5.2", prompt_tokens=120, latency=0.85)
log_structured(sl, "tool_call",
    tool="search_weather", city="北京", success=True)
log_structured(sl, "agent_error",
    agent="WeatherAgent", error="timeout", retry_count=2)


# ================================
# 练习题
# ================================

print("\n" + "=" * 60)
print("练习题")
print("=" * 60)

# 练习 1：创建带时间戳的文件日志
def exercise1():
    log_dir = Path("./logs")
    log_dir.mkdir(exist_ok=True)

    logger = logging.getLogger("exercise1")
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(
        log_dir / f"practice_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log",
        encoding="utf-8"
    )
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)-5s %(message)s"))
    logger.addHandler(fh)

    logger.info("练习 1 日志写入成功")
    print("练习 1 - 查看日志文件: ls -la ./logs/")

exercise1()


# 练习 2：不同模块使用独立 Logger
class UserModule:
    def __init__(self):
        self.logger = logging.getLogger("Agent.User")
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())

    def login(self, user: str):
        self.logger.info("用户登录: %s", user)


class ToolModule:
    def __init__(self):
        self.logger = logging.getLogger("Agent.Tool")
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())

    def execute(self, tool: str):
        self.logger.info("工具调用: %s", tool)

print("\n练习 2 - 模块独立日志:")
UserModule().login("张三")
ToolModule().execute("search")


# 练习 3：统计日志中的错误数量
class ErrorCounter(logging.Handler):
    def __init__(self):
        super().__init__()
        self.error_count = 0

    def emit(self, record):
        if record.levelno >= logging.ERROR:
            self.error_count += 1


counter = ErrorCounter()
test_logger = logging.getLogger("error_test")
test_logger.addHandler(counter)

test_logger.info("这是一个 info")
test_logger.error("错误 1")
test_logger.error("错误 2")
test_logger.warning("这是 warning")

print(f"\n练习 3 - 捕获到 {counter.error_count} 个错误")


print("\n✅ Day 13 学习完成！")
print("要点总结：")
print("1. 五级日志：DEBUG → INFO → WARNING → ERROR → CRITICAL")
print("2. Handler：控制台、文件、自定义（可多个同时使用）")
print("3. Formatter：控制输出格式和时间格式")
print("4. agent_log.exception() 自动记录堆栈")
print("5. 环境分级：开发 DEBUG / 测试 INFO / 生产 WARNING")
print("6. 结构化日志：JSON 格式，方便后续分析")
print("7. 不同模块独立 Logger，用点号分隔命名空间")
