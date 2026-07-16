"""
Day 13 练习：日志系统

说明：本文件只有练习题，没有答案。
      请参考 logging_basics.py 查看示例和答案。
"""

import logging
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any


# ================================
# 练习 1：配置基础 Logger
# ================================

# TODO: 创建 Logger 对象，名为 "agent"
# TODO: 设置日志级别为 DEBUG
# TODO: 添加 StreamHandler，输出到控制台
# TODO: 设置 Formatter：显示时间、级别、消息内容
# TODO: 用 info 级别输出 "Agent 启动成功"

# 完成后去掉下面 pass
pass


# ================================
# 练习 2：为 Agent 方法添加日志
# ================================

class Agent:
    """待完善的 Agent 类"""

    def __init__(self, name: str):
        self.name = name
        # TODO: 创建 Logger，名为 f"Agent.{name}"
        # TODO: 设置 DEBUG 级别，添加控制台 Handler

    def think(self, query: str) -> str:
        # TODO: info 级别输出 "开始思考: {query[:30]}"
        # TODO: debug 级别输出完整思考内容
        thought = f"分析问题: {query}"
        return thought

    def use_tool(self, tool_name: str, args: Dict[str, Any]) -> str:
        # TODO: info 级别输出 "调用工具: {tool_name}({args})"
        #       提示: json.dumps(args, ensure_ascii=False) 格式化参数
        result = f"{tool_name} 执行成功"
        # TODO: info 级别输出 "工具返回: {result}"
        return result

    def respond(self, answer: str):
        # TODO: info 级别输出 "最终回答: {answer[:50]}"
        pass


# TODO: 创建 Agent("Helper") 实例
# TODO: 依次调用 think、use_tool、respond，观察日志输出


# ================================
# 练习 3：结构化日志（JSON 格式）
# ================================

# TODO: 创建函数 log_json(logger, event, **kwargs)
#       组装字典: {"event": event, "time": datetime.now().isoformat(), **kwargs}
#       用 json.dumps 转字符串，logger.info 输出

# TODO: 创建 Logger，添加控制台 Handler
# TODO: 调用 log_json 记录一次 LLM 调用（model="glm-5.2", latency=0.35, tokens=420）


# ================================
# 练习 4：按日期写入文件日志
# ================================

# TODO: 创建日志目录 "./logs"（Path.mkdir(exist_ok=True)）
# TODO: 获取当天日期串 datetime.now().strftime("%Y%m%d")
# TODO: 创建 FileHandler，文件路径 f"logs/agent_{today}.log"
# TODO: Formatter: "[%(asctime)s] %(levelname)s %(message)s"
# TODO: 创建 Logger 并添加 FileHandler
# TODO: info 输出 "每日日志测试"


# ================================
# 练习 5：自定义 Handler——统计日志数量
# ================================

# TODO: 创建 CountingHandler，继承 logging.Handler
#       步骤：
#       1. __init__ 中 self.counts = {"DEBUG":0, "INFO":0, "WARNING":0, "ERROR":0}
#       2. emit(self, record) 方法中：
#          如果 record.levelname in self.counts，计数 +1

# TODO: 创建 Logger，添加 CountingHandler
# TODO: 记录 3 条 info、2 条 warning、1 条 error
# TODO: 打印 counter.counts


print("\n✅ Day 13 练习完成！")
