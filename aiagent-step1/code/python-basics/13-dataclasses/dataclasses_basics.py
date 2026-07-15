"""
Day 14: dataclasses — 更简洁的类定义

学习目标：用 dataclasses 替代冗长的 __init__
"""

from dataclasses import dataclass, field, asdict, fields
from typing import List, Optional, Dict, Any
from datetime import datetime
import json


# ================================
# 1. 传统类 vs dataclass
# ================================

# 传统写法（Java 风格）
class PersonOld:
    def __init__(self, name: str, age: int, email: str = ""):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __eq__(self, other):
        if not isinstance(other, PersonOld):
            return False
        return self.name == other.name and self.age == other.age


# dataclass 写法（一行装饰器）
@dataclass
class Person:
    name: str
    age: int
    email: str = ""


print("dataclass 自动生成的方法:")
p1 = Person("张三", 25)
p2 = Person("张三", 25)
p3 = Person("李四", 30)

print(f"  repr: {p1}")
print(f"  eq:   {p1 == p2}")      # True（自动比较所有字段）
print(f"  eq:   {p1 == p3}")      # False


# ================================
# 2. field() 高级配置
# ================================

@dataclass
class AgentConfig:
    model: str = "glm-5.2"
    temperature: float = 0.7
    max_tokens: int = field(default=2048, metadata={"unit": "tokens"})
    tags: List[str] = field(default_factory=list)    # 可变默认值必须用 factory
    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat(),
        init=False,    # 不出现在 __init__ 参数中
        repr=False,    # 不出现在 __repr__ 中
    )
    # field 参数：
    #   default       默认值
    #   default_factory  默认值工厂函数（用于可变对象）
    #   init          是否出现在 __init__ 中
    #   repr          是否出现在 __repr__ 中
    #   compare       是否参与相等比较
    #   metadata      元数据（自定义标签）


config = AgentConfig(temperature=0.8)
print(f"\nAgent 配置: {config}")
print(f"max_tokens metadata: {fields(AgentConfig)[2].metadata}")


# ================================
# 3. 嵌套 dataclass
# ================================

@dataclass
class Tool:
    name: str
    description: str
    parameters: Dict[str, str] = field(default_factory=dict)


@dataclass
class AgentProfile:
    name: str
    role: str
    tools: List[Tool] = field(default_factory=list)


search_tool = Tool("search", "搜索互联网")
calc_tool = Tool("calculator", "数学计算")

agent_profile = AgentProfile(
    name="Assistant",
    role="通用助手",
    tools=[search_tool, calc_tool]
)

print(f"\nAgent 配置: {agent_profile}")


# ================================
# 4. 不可变 dataclass
# ================================

@dataclass(frozen=True)
class FrozenConfig:
    host: str
    port: int


print("\n不可变 dataclass:")
fc = FrozenConfig("localhost", 8080)
# fc.port = 9090  # ❌ FrozenInstanceError: cannot assign to field 'port'


# ================================
# 5. asdict / 序列化
# ================================

@dataclass
class Message:
    role: str
    content: str
    timestamp: str = field(
        default_factory=lambda: datetime.now().isoformat()
    )


msg = Message("user", "今天天气怎么样？")
print(f"\nasdict: {asdict(msg)}")
print(f"JSON:   {json.dumps(asdict(msg), ensure_ascii=False)}")


# ================================
# 6. AI Agent 实战：完整的 Agent 配置
# ================================

@dataclass
class ModelConfig:
    name: str = "glm-5.2"
    temperature: float = 0.7
    max_tokens: int = 2048
    top_p: float = 1.0


@dataclass
class MemoryConfig:
    type: str = "buffer"          # buffer / summary / vector
    max_messages: int = 100
    summary_interval: int = 10


@dataclass
class ToolConfig:
    name: str
    description: str
    enabled: bool = True
    rate_limit: int = 60          # 每分钟最大调用次数


@dataclass
class AgentSettings:
    """Agent 完整配置 — 职业生涯中你会写很多这种类"""
    name: str
    description: str
    model: ModelConfig = field(default_factory=ModelConfig)
    memory: MemoryConfig = field(default_factory=MemoryConfig)
    tools: List[ToolConfig] = field(default_factory=list)
    max_retries: int = 3
    timeout: float = 30.0


settings = AgentSettings(
    name="WeatherAgent",
    description="天气查询助手",
    model=ModelConfig(temperature=0.3),
    tools=[
        ToolConfig("search_weather", "查询城市天气"),
        ToolConfig("search_air_quality", "查询空气质量", rate_limit=30),
    ]
)

print(f"\n完整 Agent 配置:")
print(f"  名称: {settings.name}")
print(f"  模型: {settings.model.name} (T={settings.model.temperature})")
print(f"  工具: {[t.name for t in settings.tools]}")
print(f"  超时: {settings.timeout}s")
print(f"  JSON: {json.dumps(asdict(settings), ensure_ascii=False, indent=2)}")


# ================================
# 7. dataclass vs Pydantic
# ================================

# dataclass：轻量、快速、Python 标准库
# Pydantic：带验证、序列化、JSON Schema

# 什么时候用 dataclass：
#   - 内部数据结构（不对外暴露）
#   - 不需要验证的场景
#   - 需要高性能的场景

# 什么时候用 Pydantic：
#   - API 请求/响应模型
#   - 需要数据验证
#   - 需要 JSON Schema 导出

@dataclass
class InternalState:
    """内部状态（dataclass）"""
    step: int = 0
    reasoning: str = ""
    next_action: str = ""


# 实际使用
from pydantic import BaseModel

class APIResponse(BaseModel):
    """API 响应（Pydantic）"""
    success: bool
    data: str
    error: Optional[str] = None


print("\ndataclass vs Pydantic:")
print("  内部状态用 dataclass（快、轻量）")
print("  外部接口用 Pydantic（验证、安全）")


# ================================
# 8. __post_init__ 后处理
# ================================

@dataclass
class TokenBudget:
    max_tokens: int
    used_tokens: int = 0

    def __post_init__(self):
        """__init__ 之后自动调用"""
        if self.max_tokens <= 0:
            raise ValueError("max_tokens 必须大于 0")
        if self.used_tokens < 0:
            raise ValueError("used_tokens 不能为负")
        self.remaining = self.max_tokens - self.used_tokens


try:
    budget = TokenBudget(max_tokens=4096, used_tokens=500)
    print(f"\nToken 预算: 剩余 {budget.remaining}/{budget.max_tokens}")
except ValueError as e:
    print(f"错误: {e}")


# ================================
# 练习题
# ================================

print("\n" + "=" * 60)
print("练习题")
print("=" * 60)

# 练习 1：定义对话消息 dataclass
@dataclass
class ChatMessage:
    role: str
    content: str
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

messages = [
    ChatMessage("user", "你好"),
    ChatMessage("assistant", "你好！有什么可以帮你的？"),
]
print(f"练习 1 - 消息数: {len(messages)}, 第一条: {messages[0]}")


# 练习 2：带验证的 dataclass
@dataclass
class ScoredItem:
    name: str
    score: float

    def __post_init__(self):
        if not 0 <= self.score <= 100:
            raise ValueError(f"分数必须在 0-100 之间，当前: {self.score}")

item = ScoredItem("测试", 85.5)
print(f"练习 2 - {item.name}: {item.score} 分")


# 练习 3：统计 dataclass 字段
@dataclass
class AgentMetrics:
    total_requests: int = 0
    successful: int = 0
    failed: int = 0
    total_tokens: int = 0
    total_latency: float = 0.0

    def success_rate(self) -> float:
        return self.successful / self.total_requests if self.total_requests else 0

m = AgentMetrics(total_requests=100, successful=95, failed=5)
print(f"练习 3 - 成功率: {m.success_rate():.1%}")


print("\n✅ Day 14 学习完成！")
print("要点总结：")
print("1. @dataclass 自动生成 __init__/__repr__/__eq__")
print("2. field() 控制字段行为（default_factory/init/repr/compare）")
print("3. frozen=True 创建不可变对象")
print("4. asdict() 一键转字典，序列化超方便")
print("5. 嵌套 dataclass 表达复杂结构")
print("6. __post_init__ 做初始化后验证")
print("7. dataclass 用于内部结构，Pydantic 用于外部接口")
