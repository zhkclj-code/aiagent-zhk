import pytest

from mini_agent.agent import MiniAgent
from mini_agent.client import FakeLLMClient
from mini_agent.errors import AgentLoopError
from mini_agent.models import LLMReply, ToolCall
from mini_agent.tools import ToolRegistry


async def test_agent_returns_normal_reply() -> None:
    client = FakeLLMClient(replies=[LLMReply(content="你好")])
    response = await MiniAgent(client, ToolRegistry.default()).run("hello")
    assert response.content == "你好"
    assert response.tool_rounds == 0


async def test_agent_executes_tool_and_returns_final_reply() -> None:
    client = FakeLLMClient(
        replies=[
            LLMReply(
                tool_calls=[
                    ToolCall(id="c1", name="calculator", arguments={"expression": "2+2"})
                ]
            ),
            LLMReply(content="答案是 4"),
        ]
    )
    response = await MiniAgent(client, ToolRegistry.default()).run("计算 2+2")
    assert response.content == "答案是 4"
    assert response.tool_rounds == 1
    assert any(
        message.role == "tool" and message.content == "4" for message in response.messages
    )


async def test_agent_exposes_unknown_tool_error_to_model() -> None:
    client = FakeLLMClient(
        replies=[
            LLMReply(tool_calls=[ToolCall(id="c1", name="missing", arguments={})]),
            LLMReply(content="工具不可用"),
        ]
    )
    response = await MiniAgent(client, ToolRegistry.default()).run("调用未知工具")
    tool_message = next(message for message in response.messages if message.role == "tool")
    assert "未知工具" in (tool_message.content or "")


async def test_agent_stops_after_tool_round_limit() -> None:
    calls = [
        LLMReply(tool_calls=[ToolCall(id=f"c{i}", name="current_time", arguments={})])
        for i in range(2)
    ]
    agent = MiniAgent(
        FakeLLMClient(replies=calls),
        ToolRegistry.default(),
        max_tool_rounds=1,
    )
    with pytest.raises(AgentLoopError):
        await agent.run("不断调用工具")


async def test_agent_keeps_history_until_cleared() -> None:
    client = FakeLLMClient(replies=[LLMReply(content="第一轮"), LLMReply(content="第二轮")])
    agent = MiniAgent(client, ToolRegistry.default())
    await agent.run("one")
    response = await agent.run("two")
    assert [message.content for message in response.messages if message.role == "user"] == [
        "one",
        "two",
    ]

    agent.clear_history()

    assert agent.history == []
