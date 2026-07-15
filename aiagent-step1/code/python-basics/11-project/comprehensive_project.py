"""
Day 12: 综合项目

学习目标：将所学知识应用到实际项目
"""

import asyncio
import json
from datetime import datetime
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from pydantic import BaseModel, Field
import random


# ================================
# 1. 项目需求：构建简单的 LLM Agent
# ================================

"""
项目目标：
1. 创建一个能回答问题的 Agent
2. 支持多轮对话
3. 记录对话历史
4. 异步调用 API
5. 数据验证和序列化
"""


# ================================
# 2. 数据模型设计
# ================================

class Message(BaseModel):
    """消息模型"""
    
    role: str = Field(..., description="角色：user/assistant")
    content: str = Field(..., description="消息内容")
    timestamp: str = Field(
        default_factory=lambda: datetime.now().isoformat(),
        description="时间戳"
    )


class Conversation(BaseModel):
    """对话模型"""
    
    conversation_id: str = Field(..., description="对话ID")
    messages: List[Message] = Field(default_factory=list, description="消息列表")
    created_at: str = Field(
        default_factory=lambda: datetime.now().isoformat(),
        description="创建时间"
    )
    
    def add_message(self, role: str, content: str) -> Message:
        """添加消息"""
        message = Message(role=role, content=content)
        self.messages.append(message)
        return message
    
    def get_history(self, limit: int = 10) -> List[Message]:
        """获取历史消息"""
        return self.messages[-limit:]


class AgentResponse(BaseModel):
    """Agent 响应模型"""
    
    success: bool = Field(..., description="是否成功")
    content: Optional[str] = Field(None, description="响应内容")
    error: Optional[str] = Field(None, description="错误信息")
    tokens_used: int = Field(0, description="使用的 Token 数")


# ================================
# 3. Agent 核心类
# ================================

class SimpleAgent:
    """简单的 LLM Agent"""
    
    def __init__(self, name: str = "AI Assistant"):
        self.name: str = name
        self.conversation: Optional[Conversation] = None
        self.total_tokens: int = 0
    
    def start_conversation(self, conversation_id: str) -> None:
        """开始对话"""
        self.conversation = Conversation(conversation_id=conversation_id)
    
    async def call_llm_api(self, prompt: str) -> str:
        """模拟异步 LLM API 调用"""
        await asyncio.sleep(random.uniform(0.5, 1.5))
        
        # 模拟响应
        responses = [
            f"收到你的问题：'{prompt[:30]}...'，我来帮你解答。",
            f"关于 '{prompt[:30]}...'，这是一个很好的问题。",
            f"让我思考一下 '{prompt[:30]}...' 这个问题。"
        ]
        
        return random.choice(responses)
    
    async def chat(self, user_message: str) -> AgentResponse:
        """聊天"""
        if not self.conversation:
            return AgentResponse(
                success=False,
                error="请先开始对话"
            )
        
        try:
            # 记录用户消息
            self.conversation.add_message("user", user_message)
            
            # 调用 LLM API
            response = await self.call_llm_api(user_message)
            
            # 记录助手消息
            self.conversation.add_message("assistant", response)
            
            # 更新 Token 统计
            tokens_used = len(user_message) + len(response)
            self.total_tokens += tokens_used
            
            return AgentResponse(
                success=True,
                content=response,
                tokens_used=tokens_used
            )
        
        except Exception as e:
            return AgentResponse(
                success=False,
                error=str(e)
            )
    
    def get_conversation_history(self) -> List[Dict[str, Any]]:
        """获取对话历史"""
        if not self.conversation:
            return []
        
        return [
            {
                "role": msg.role,
                "content": msg.content,
                "timestamp": msg.timestamp
            }
            for msg in self.conversation.messages
        ]
    
    def save_conversation(self, filename: str) -> bool:
        """保存对话"""
        if not self.conversation:
            return False
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(
                    self.conversation.model_dump(),
                    f,
                    ensure_ascii=False,
                    indent=2
                )
            return True
        except Exception as e:
            print(f"保存失败: {e}")
            return False
    
    def load_conversation(self, filename: str) -> bool:
        """加载对话"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.conversation = Conversation(**data)
            return True
        except Exception as e:
            print(f"加载失败: {e}")
            return False


# ================================
# 4. 异步任务管理器
# ================================

class AsyncTaskManager:
    """异步任务管理器"""
    
    def __init__(self, max_concurrent: int = 5):
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.tasks: Dict[str, asyncio.Task] = {}
    
    async def run_task(self, task_id: str, coro) -> Any:
        """运行任务"""
        async with self.semaphore:
            task = asyncio.create_task(coro)
            self.tasks[task_id] = task
            
            try:
                result = await task
                return result
            finally:
                self.tasks.pop(task_id, None)
    
    async def cancel_task(self, task_id: str) -> bool:
        """取消任务"""
        task = self.tasks.get(task_id)
        if task:
            task.cancel()
            return True
        return False
    
    async def wait_all(self) -> None:
        """等待所有任务"""
        if self.tasks:
            await asyncio.gather(*self.tasks.values(), return_exceptions=True)


# ================================
# 5. 多 Agent 协作（简单示例）
# ================================

class MultiAgentSystem:
    """多 Agent 系统"""
    
    def __init__(self):
        self.agents: Dict[str, SimpleAgent] = {}
    
    def add_agent(self, name: str) -> SimpleAgent:
        """添加 Agent"""
        agent = SimpleAgent(name)
        self.agents[name] = agent
        return agent
    
    async def broadcast(self, message: str) -> Dict[str, AgentResponse]:
        """广播消息给所有 Agent"""
        results = {}
        
        async def ask_agent(name: str, agent: SimpleAgent) -> tuple:
            agent.start_conversation(f"conv_{name}")
            response = await agent.chat(message)
            return name, response
        
        responses = await asyncio.gather(
            *[ask_agent(name, agent) for name, agent in self.agents.items()]
        )
        
        for name, response in responses:
            results[name] = response
        
        return results


# ================================
# 6. 运行示例
# ================================

async def run_example():
    """运行示例"""
    print("=" * 60)
    print("LLM Agent 综合示例")
    print("=" * 60)
    
    # 创建 Agent
    agent = SimpleAgent("Python Agent")
    
    # 开始对话
    agent.start_conversation("conv_001")
    
    # 多轮对话
    questions = [
        "什么是 Python？",
        "Python 有哪些特性？",
        "如何学习 Python？"
    ]
    
    for question in questions:
        print(f"\n用户: {question}")
        
        response = await agent.chat(question)
        
        if response.success:
            print(f"助手: {response.content}")
            print(f"Token: {response.tokens_used}")
        else:
            print(f"错误: {response.error}")
    
    # 查看对话历史
    print("\n" + "=" * 60)
    print("对话历史")
    print("=" * 60)
    
    history = agent.get_conversation_history()
    for msg in history:
        role = "用户" if msg["role"] == "user" else "助手"
        print(f"{role}: {msg['content'][:50]}...")
    
    # 保存对话
    print("\n保存对话...")
    agent.save_conversation("conversation.json")
    print("对话已保存")
    
    # 统计信息
    print(f"\n总 Token 消耗: {agent.total_tokens}")


asyncio.run(run_example())


# ================================
# 7. 多 Agent 协作示例
# ================================

async def run_multi_agent_example():
    """多 Agent 协作示例"""
    print("\n" + "=" * 60)
    print("多 Agent 协作示例")
    print("=" * 60)
    
    # 创建多 Agent 系统
    system = MultiAgentSystem()
    
    # 添加多个 Agent
    system.add_agent("Python Agent")
    system.add_agent("Java Agent")
    system.add_agent("AI Agent")
    
    # 广播消息
    print("\n广播问题: '什么是编程？'")
    
    results = await system.broadcast("什么是编程？")
    
    for name, response in results.items():
        print(f"\n{name}:")
        if response.success:
            print(f"  {response.content}")
        else:
            print(f"  错误: {response.error}")


asyncio.run(run_multi_agent_example())


# ================================
# 练习题
# ================================

print("\n" + "=" * 60)
print("练习题")
print("=" * 60)


# 练习 1：创建一个有状态管理的 Agent
class StatefulAgent(SimpleAgent):
    """有状态的 Agent"""
    
    def __init__(self, name: str = "Stateful Agent"):
        super().__init__(name)
        self.state: Dict[str, Any] = {}
    
    def set_state(self, key: str, value: Any) -> None:
        """设置状态"""
        self.state[key] = value
    
    def get_state(self, key: str) -> Any:
        """获取状态"""
        return self.state.get(key)


async def exercise1():
    """练习 1"""
    print("\n练习 1 - 有状态 Agent:")
    
    agent = StatefulAgent()
    agent.start_conversation("conv_ex1")
    agent.set_state("language", "Python")
    
    print(f"状态: language = {agent.get_state('language')}")


asyncio.run(exercise1())


# 练习 2：实现对话持久化
class PersistentAgent(SimpleAgent):
    """持久化 Agent"""
    
    def __init__(self, storage_path: str = "./conversations"):
        super().__init__()
        self.storage_path = storage_path
        import os
        os.makedirs(storage_path, exist_ok=True)
    
    def auto_save(self) -> None:
        """自动保存"""
        if self.conversation:
            filename = f"{self.storage_path}/{self.conversation.conversation_id}.json"
            self.save_conversation(filename)


async def exercise2():
    """练习 2"""
    print("\n练习 2 - 持久化 Agent:")
    
    agent = PersistentAgent()
    agent.start_conversation("conv_persistent")
    
    await agent.chat("测试消息")
    agent.auto_save()
    
    print("对话已自动保存")


asyncio.run(exercise2())


# 练习 3：实现 Agent 池
class AgentPool:
    """Agent 池"""
    
    def __init__(self, size: int = 3):
        self.agents = [SimpleAgent(f"Agent_{i}") for i in range(size)]
        self.current = 0
    
    def get_agent(self) -> SimpleAgent:
        """获取 Agent（轮询）"""
        agent = self.agents[self.current]
        self.current = (self.current + 1) % len(self.agents)
        return agent


async def exercise3():
    """练习 3"""
    print("\n练习 3 - Agent 池:")
    
    pool = AgentPool(size=3)
    
    for i in range(5):
        agent = pool.get_agent()
        print(f"请求 {i+1}: 使用 {agent.name}")


asyncio.run(exercise3())


# 练习 4：实现异步任务队列
async def exercise4():
    """练习 4"""
    print("\n练习 4 - 异步任务队列:")
    
    manager = AsyncTaskManager(max_concurrent=2)
    
    async def task(n: int):
        await asyncio.sleep(0.5)
        return f"任务 {n} 完成"
    
    # 并发运行任务
    results = await asyncio.gather(
        manager.run_task("task_1", task(1)),
        manager.run_task("task_2", task(2)),
        manager.run_task("task_3", task(3))
    )
    
    for result in results:
        print(f"  {result}")


asyncio.run(exercise4())


# 练习 5：实现 Agent 监控
class MonitoredAgent(SimpleAgent):
    """监控 Agent"""
    
    def __init__(self, name: str = "Monitored Agent"):
        super().__init__(name)
        self.metrics = {
            "total_requests": 0,
            "successful_requests": 0,
            "failed_requests": 0,
            "total_tokens": 0
        }
    
    async def chat(self, user_message: str) -> AgentResponse:
        """聊天（带监控）"""
        self.metrics["total_requests"] += 1
        
        response = await super().chat(user_message)
        
        if response.success:
            self.metrics["successful_requests"] += 1
            self.metrics["total_tokens"] += response.tokens_used
        else:
            self.metrics["failed_requests"] += 1
        
        return response
    
    def get_metrics(self) -> Dict[str, int]:
        """获取监控指标"""
        return self.metrics.copy()


async def exercise5():
    """练习 5"""
    print("\n练习 5 - Agent 监控:")
    
    agent = MonitoredAgent()
    agent.start_conversation("conv_monitored")
    
    await agent.chat("问题 1")
    await agent.chat("问题 2")
    
    metrics = agent.get_metrics()
    print(f"监控指标: {metrics}")


asyncio.run(exercise5())


print("\n✅ Day 12 学习完成！")
print("要点总结：")
print("1. 数据模型：Pydantic 验证和序列化")
print("2. Agent 设计：状态管理、API 调用")
print("3. 异步编程：asyncio 并发调用")
print("4. 对话管理：历史记录、持久化")
print("5. 多 Agent 系统：协作、广播")
print("6. 任务管理：队列、并发限制")
print("7. 监控：指标统计、性能分析")
print("8. 工程化：类型注解、测试、文档")


# 清理临时文件
import os
if os.path.exists("conversation.json"):
    os.remove("conversation.json")