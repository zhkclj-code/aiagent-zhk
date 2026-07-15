"""
Day 13: Python 日志系统

学习目标：掌握 logging 模块，告别 print 调试
"""

import logging
import sys
from datetime import datetime
from pathlib import Path


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
