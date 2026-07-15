"""
Day 14 练习：dataclasses

说明：本文件只有练习题，没有答案。
      请参考 dataclasses_basics.py 查看示例和答案。
"""

from dataclasses import dataclass, field, asdict
from typing import List, Optional
from datetime import datetime
import json


# ================================
# 练习 1：定义工具注册表
# ================================

# TODO: @dataclass 创建 ToolDef 类
#       name: str（工具名）
#       description: str（描述）
#       params: Dict[str, str]（参数名→描述），默认空字典，用 field(default_factory=dict)

# TODO: @dataclass 创建 ToolRegistry 类
#       tools: List[ToolDef]，默认空列表
#       方法 add(tool: ToolDef): 添加工具
#       方法 find(name: str) -> Optional[ToolDef]: 按名称查找
#       方法 list_names() -> List[str]: 返回所有工具名

# TODO: 创建 ToolRegistry，注册 weather、search 两个工具
# TODO: 打印工具列表，查找 weather 工具


# ================================
# 练习 2：对话历史
# ================================

# TODO: @dataclass 创建 DialogTurn，字段 user、assistant、timestamp
#       timestamp 默认用 datetime.now().isoformat()（用 field(default_factory=...)）

# TODO: @dataclass 创建 DialogHistory
#       turns: List[DialogTurn]，默认空列表
#       方法 add(user_msg, assistant_msg): 添加一轮
#       方法 last_n(n) -> List[DialogTurn]: 返回最近 n 轮
#       方法 export_json() -> str: json.dumps 导出，ensure_ascii=False, indent=2

# TODO: 创建 DialogHistory，添加 2 轮对话
# TODO: 打印总轮数，最近一轮


# ================================
# 练习 3：__post_init__ 后验证
# ================================

# TODO: @dataclass 创建 TokenBudget
#       max_tokens: int, used_tokens: int = 0
#       实现 __post_init__:
#       - 验证 max_tokens > 0，否则 raise ValueError
#       - 计算 self.remaining = max_tokens - used_tokens
#       - 计算 self.usage_pct = round(used_tokens / max_tokens * 100, 1)
#       方法 can_use(tokens_needed: int) -> bool

# TODO: 创建 TokenBudget(4096, 1024)
# TODO: 打印 remaining, usage_pct，测试 can_use(2000), can_use(5000)


# ================================
# 练习 4：嵌套 dataclass
# ================================

# TODO: @dataclass 创建 LLMConfig
#       provider: str, model: str, api_key: str = field(repr=False)
#       temperature: float = 0.7, max_tokens: int = 2048, cost_per_1k: float = 0.0

# TODO: @dataclass 创建 ModelPool
#       models: List[LLMConfig]，默认空列表
#       方法 add: 添加模型
#       方法 get_by_provider(provider) -> Optional[LLMConfig]: 按 provider 查找
#       方法 cheapest() -> Optional[LLMConfig]: 返回 cost_per_1k 最小的

# TODO: 创建 ModelPool，注册 3 个不同 provider 的模型（不同 cost）
# TODO: 查找 glm，打印最便宜的模型


# ================================
# 练习 5：frozen 不可变记录
# ================================

# TODO: @dataclass(frozen=True) 创建 TaskRecord
#       task_id: str, status: str, tokens_used: int, latency: float
#       timestamp: str（默认 datetime.now().isoformat()）
#       方法 is_success() -> bool: status == "success" 返回 True

# TODO: 创建 3 条记录（2 成功 1 失败）
# TODO: 统计：成功数、总 token 数


print("\n✅ Day 14 练习完成！")
