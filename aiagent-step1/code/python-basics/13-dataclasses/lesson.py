"""
Day 14: dataclasses — 更简洁的类定义

学习目标：用 dataclasses 替代冗长的 __init__
"""

from dataclasses import dataclass, field, asdict, fields
from typing import List, Optional, Dict, Any
from datetime import datetime
import json


# ================================
# 0. dataclass核心概念 - Java开发者必读
# ================================

"""
【什么是dataclass】
dataclass是Python 3.7+引入的装饰器，用于自动生成类的常用方法。
核心价值：减少样板代码，提高代码可读性。

【dataclass vs Java Lombok对比】

| 特性 | Python @dataclass | Java Lombok @Data |
|-----|-------------------|-------------------|
| 生成方法 | __init__, __repr__, __eq__ | getter, setter, equals, hashCode, toString |
| 生成时机 | 运行时（类定义时） | 编译时（字节码增强） |
| IDE支持 | 原生支持（Python 3.7+） | 需要插件（Lombok Plugin） |
| 依赖 | 标准库 | 第三方库 |
| 不可变 | frozen=True | @Value（final字段） |
| 构建器 | 无内置 | @Builder |
| 验证 | __post_init__ | @Validated + JSR-303 |
| 性能 | 无额外开销 | 编译优化 |

【和Java POJO的详细对比】

Java POJO（Plain Old Java Object）：
public class User {
    private String name;
    private int age;

    // 手写getter/setter
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    // 手写equals/hashCode
    @Override
    public boolean equals(Object o) { ... }

    // 手写toString
    @Override
    public String toString() { ... }
}

Python @dataclass：
@dataclass
class User:
    name: str
    age: int
    # 自动生成__init__, __repr__, __eq__

【核心差异】

1. 生成时机：
   - Python: 运行时（类定义时立即生成）
   - Java Lombok: 编译时（需要编译器插件）
   - Java POJO: 手写（无自动生成）

2. 使用方式：
   Python:
   user = User("张三", 25)  # 直接访问属性
   user.name = "李四"

   Java:
   User user = new User();
   user.setName("张三");  // 通过setter访问
   user.setAge(25);

3. 不可变性：
   Python:
   @dataclass(frozen=True)
   class ImmutableUser:
       name: str
   # user.name = "新名字"  # 报错！

   Java:
   @Value  // Lombok
   public class ImmutableUser {
       String name;
   }

【dataclass的优势】

1. 简洁性：
   - 3行代码 vs Java POJO的30+行
   - 无需手写getter/setter/equals/hashCode

2. 类型安全：
   - 结合类型注解，IDE智能提示
   - 可选的运行时验证（配合Pydantic）

3. 标准库：
   - 无需第三方依赖
   - Python 3.7+原生支持

4. 不可变支持：
   - frozen=True实现不可变对象
   - 线程安全、函数式编程友好

【Java Lombok的优势】

1. 构建器模式：
   @Builder
   public class User {
       String name;
       int age;
   }
   User user = User.builder().name("张三").age(25).build();

2. 更多功能：
   - @Slf4j（日志）
   - @NoArgsConstructor
   - @AllArgsConstructor
   - @Synchronized

3. 编译优化：
   - 无运行时开销
   - IDE深度集成

【使用场景】

✅ 适合用dataclass：
- 数据传输对象（DTO）
- 配置类、参数类
- 简单的数据容器
- API请求/响应模型
- 领域模型（Domain Model）

✅ 适合用Lombok @Data：
- Java项目（标准选择）
- 需要构建器模式
- 企业级应用（Spring Boot集成）

【最佳实践】

1. 默认值：
   @dataclass
   class Config:
       timeout: int = 30  # 默认值
       retry: int = field(default=3)  # field()方式

2. 不可变：
   @dataclass(frozen=True)
   class Point:
       x: float
       y: float

3. 自定义方法：
   @dataclass
   class Rectangle:
       width: float
       height: float

       def area(self) -> float:
           return self.width * self.height

4. 验证：
   @dataclass
   class User:
       age: int

       def __post_init__(self):
           if self.age < 0:
               raise ValueError("年龄不能为负数")

5. 序列化：
   @dataclass
   class User:
       name: str

       def to_dict(self):
           return asdict(self)

【常见陷阱】

1. 默认值是可变对象：
   ❌ 错误：
   @dataclass
   class Config:
       items: list = []  # 所有实例共享同一个list！

   ✅ 正确：
   @dataclass
   class Config:
       items: list = field(default_factory=list)

2. 字段顺序：
   - 无默认值字段必须在有默认值字段之前

3. 继承：
   - 子类会继承父类字段，注意初始化顺序

【Java开发者迁移建议】

Java POJO → Python @dataclass
───────────────────────────────
private字段 + getter/setter → 直接访问属性
equals/hashCode → 自动生成（可重写）
toString → __repr__（自动生成）
构造函数 → __init__（自动生成）
Builder模式 → 无内置（可手写类方法）
"""

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
