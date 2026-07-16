"""
Day 12: 综合项目 - Mini Agent

学习目标：综合运用所学知识，实现一个简单的 Agent
"""


# ================================
# 项目：构建一个简单的问答 Agent
# ================================

"""
项目目标：
创建一个能回答问题的简单 Agent，综合运用：
- 异步编程（并发调用 API）
- 类型注解（Pydantic 模型）
- 错误处理（异常捕获）
- 测试（pytest）

---

## 练习 1：设计数据模型

任务：使用 Pydantic 定义数据模型：

class Question(BaseModel):
    '''用户问题'''
    id: int
    content: str
    context: Optional[str] = None

class Answer(BaseModel):
    '''Agent 回答'''
    question_id: int
    content: str
    model: str
    tokens_used: int
    timestamp: str

class AgentConfig(BaseModel):
    '''Agent 配置'''
    model: str = "glm-5.2"
    temperature: float = 0.7
    max_tokens: int = 500
    api_base: str = "http://newapi.raycloud.cn/v1"
"""

# TODO: 在这里实现数据模型




# ================================
# 练习 2：实现异步 LLM 客户端
# ================================

"""
任务：实现异步 LLM API 客户端：

class AsyncLLMClient:
    '''异步 LLM 客户端'''
    
    def __init__(self, config: AgentConfig):
        self.config = config
        self.client = AsyncOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=config.api_base
        )
    
    async def chat(self, prompt: str) -> Answer:
        '''调用 LLM API'''
        # 实现异步调用
        pass
    
    async def batch_chat(self, prompts: List[str]) -> List[Answer]:
        '''并发调用多个请求'''
        # 使用 asyncio.gather
        pass
"""

# TODO: 在这里实现 AsyncLLMClient




# ================================
# 练习 3：实现 Agent 核心
# ================================

"""
任务：实现 Agent 核心逻辑：

class SimpleAgent:
    '''简单问答 Agent'''
    
    def __init__(self, config: AgentConfig):
        self.client = AsyncLLMClient(config)
        self.history: List[Dict] = []
    
    async def answer(self, question: Question) -> Answer:
        '''回答问题'''
        # 1. 检查历史记录
        # 2. 构建 prompt（包含上下文）
        # 3. 调用 LLM
        # 4. 保存历史记录
        # 5. 返回答案
        pass
    
    async def batch_answer(self, questions: List[Question]) -> List[Answer]:
        '''批量回答问题'''
        # 使用 asyncio.gather 并发处理
        pass
    
    def get_history(self) -> List[Dict]:
        '''获取对话历史'''
        return self.history
    
    def clear_history(self) -> None:
        '''清空对话历史'''
        self.history.clear()
"""

# TODO: 在这里实现 SimpleAgent




# ================================
# 练习 4：实现错误处理和重试
# ================================

"""
任务：为 Agent 添加错误处理：

class AgentError(Exception):
    '''Agent 错误'''
    pass

class APIError(AgentError):
    '''API 调用错误'''
    pass

class RateLimitError(APIError):
    '''速率限制错误'''
    pass

增强 SimpleAgent：
async def answer_with_retry(
    self, 
    question: Question,
    max_retries: int = 3,
    delay: float = 1.0
) -> Answer:
    '''带重试的回答'''
    for attempt in range(max_retries):
        try:
            return await self.answer(question)
        except RateLimitError:
            if attempt < max_retries - 1:
                await asyncio.sleep(delay * (attempt + 1))
            else:
                raise
"""

# TODO: 在这里实现错误处理和重试逻辑




# ================================
# 练习 5：实现对话管理
# ================================

"""
任务：实现对话历史管理：

class ConversationManager:
    '''对话管理器'''
    
    def __init__(self, max_history: int = 10):
        self.history: List[Dict] = []
        self.max_history = max_history
    
    def add_message(self, role: str, content: str) -> None:
        '''添加消息到历史'''
        self.history.append({"role": role, "content": content})
        # 如果超过最大历史数，删除旧消息
        if len(self.history) > self.max_history:
            self.history = self.history[-self.max_history:]
    
    def get_context(self) -> str:
        '''获取上下文（历史对话）'''
        # 将历史记录格式化为字符串
        pass
    
    def summarize(self) -> str:
        '''总结对话内容'''
        # 使用 LLM 总结对话
        pass

集成到 SimpleAgent：
class SimpleAgent:
    def __init__(self, config: AgentConfig):
        self.client = AsyncLLMClient(config)
        self.conversation = ConversationManager()
"""

# TODO: 在这里实现 ConversationManager




# ================================
# 练习 6：编写测试
# ================================

"""
任务：为 Agent 编写测试：

test_agent.py：

import pytest
from unittest.mock import AsyncMock, patch

@pytest.fixture
def agent_config():
    return AgentConfig(model="glm-5.2")

@pytest.fixture
def mock_llm_client():
    client = AsyncMock(spec=AsyncLLMClient)
    client.chat.return_value = Answer(
        question_id=1,
        content="这是一个测试回答",
        model="glm-5.2",
        tokens_used=100,
        timestamp="2024-01-13T10:00:00"
    )
    return client

@pytest.mark.asyncio
async def test_agent_answer(agent_config, mock_llm_client):
    agent = SimpleAgent(agent_config)
    agent.client = mock_llm_client
    
    question = Question(id=1, content="测试问题")
    answer = await agent.answer(question)
    
    assert answer.question_id == 1
    assert "测试回答" in answer.content

@pytest.mark.asyncio
async def test_agent_batch_answer(agent_config, mock_llm_client):
    agent = SimpleAgent(agent_config)
    agent.client = mock_llm_client
    
    questions = [
        Question(id=1, content="问题1"),
        Question(id=2, content="问题2")
    ]
    
    answers = await agent.batch_answer(questions)
    assert len(answers) == 2

运行：pytest test_agent.py
"""

# TODO: 在这里编写测试文件 test_agent.py




# ================================
# 练习 7：创建命令行工具
# ================================

"""
任务：创建命令行交互界面：

agent_cli.py：

import asyncio
import argparse

async def main():
    parser = argparse.ArgumentParser(description="Mini Agent CLI")
    parser.add_argument("--model", default="glm-5.2", help="模型名称")
    parser.add_argument("--temperature", type=float, default=0.7)
    args = parser.parse_args()
    
    config = AgentConfig(
        model=args.model,
        temperature=args.temperature
    )
    
    agent = SimpleAgent(config)
    
    print("🤖 Mini Agent 已启动！输入 'quit' 退出")
    
    question_id = 1
    while True:
        user_input = input("\\n你: ").strip()
        
        if user_input.lower() == "quit":
            print("再见！")
            break
        
        question = Question(id=question_id, content=user_input)
        answer = await agent.answer(question)
        
        print(f"\\nAgent: {answer.content}")
        question_id += 1

if __name__ == "__main__":
    asyncio.run(main())

运行：python agent_cli.py
"""

# TODO: 在这里创建命令行工具 agent_cli.py




# ================================
# 验证你的实现
# ================================

if __name__ == "__main__":
    print("=" * 60)
    print("Day 12 综合项目 - Mini Agent")
    print("=" * 60)
    
    print("\n项目结构：")
    print("mini_agent/")
    print("├── models.py          # 数据模型")
    print("├── llm_client.py      # LLM 客户端")
    print("├── agent.py           # Agent 核心")
    print("├── conversation.py    # 对话管理")
    print("├── test_agent.py      # 测试文件")
    print("└── agent_cli.py       # 命令行工具")
    
    print("\n实现步骤：")
    print("1. 实现数据模型（models.py）")
    print("2. 实现 LLM 客户端（llm_client.py）")
    print("3. 实现 Agent 核心（agent.py）")
    print("4. 实现对话管理（conversation.py）")
    print("5. 编写测试（test_agent.py）")
    print("6. 创建 CLI（agent_cli.py）")
    print("7. 运行测试：pytest test_agent.py")
    print("8. 运行 CLI：python agent_cli.py")
    
    print("\n✅ Day 12 综合项目完成！")
    print("恭喜！你已经掌握了 Python 核心知识，可以开始学习 Agent 开发了！")
