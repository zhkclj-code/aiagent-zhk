from types import SimpleNamespace

import pytest

from mini_agent.client import FakeLLMClient, OpenAICompatibleClient
from mini_agent.errors import LLMClientError
from mini_agent.models import Message, ToolCall


async def test_fake_client_requests_calculator_for_calculation_prompt() -> None:
    reply = await FakeLLMClient().complete(
        [Message(role="user", content="计算 2 + 2")],
        tools=[],
    )
    assert reply.tool_calls[0].name == "calculator"
    assert reply.tool_calls[0].arguments == {"expression": "2 + 2"}


async def test_fake_client_uses_deterministic_tool_call_ids() -> None:
    client = FakeLLMClient()
    first = await client.complete([Message(role="user", content="计算 1 + 1")], tools=[])
    second = await client.complete([Message(role="user", content="现在是什么时间")], tools=[])
    assert [first.tool_calls[0].id, second.tool_calls[0].id] == ["fake-1", "fake-2"]


async def test_fake_client_turns_tool_result_into_final_answer() -> None:
    reply = await FakeLLMClient().complete(
        [Message(role="tool", content="4", name="calculator", tool_call_id="x")],
        tools=[],
    )
    assert reply.content == "工具 calculator 返回：4"


async def test_openai_adapter_maps_tool_calls() -> None:
    raw_tool_call = SimpleNamespace(
        id="call-1",
        function=SimpleNamespace(name="calculator", arguments='{"expression":"2+2"}'),
    )
    raw_message = SimpleNamespace(content=None, tool_calls=[raw_tool_call])
    completions = SimpleNamespace(
        create=_AsyncResult(SimpleNamespace(choices=[SimpleNamespace(message=raw_message)]))
    )
    raw_client = SimpleNamespace(chat=SimpleNamespace(completions=completions))
    client = OpenAICompatibleClient(raw_client=raw_client, model="demo")

    reply = await client.complete([Message(role="user", content="计算 2+2")], tools=[])

    assert reply.tool_calls[0].arguments == {"expression": "2+2"}


async def test_openai_adapter_serializes_complete_tool_conversation() -> None:
    response = SimpleNamespace(
        choices=[SimpleNamespace(message=SimpleNamespace(content="完成", tool_calls=[]))]
    )
    completions = _RecordingCompletions(response)
    client = OpenAICompatibleClient(
        raw_client=SimpleNamespace(chat=SimpleNamespace(completions=completions)),
        model="demo",
    )
    messages = [
        Message(role="user", content="计算 2+2"),
        Message(
            role="assistant",
            content=None,
            tool_calls=[
                ToolCall(id="call-1", name="calculator", arguments={"expression": "2+2"})
            ],
        ),
        Message(role="tool", content="4", name="calculator", tool_call_id="call-1"),
    ]
    tools = [{"type": "function", "function": {"name": "calculator"}}]

    await client.complete(messages, tools)

    assert completions.request == {
        "model": "demo",
        "messages": [
            {"role": "user", "content": "计算 2+2"},
            {
                "role": "assistant",
                "content": None,
                "tool_calls": [
                    {
                        "id": "call-1",
                        "type": "function",
                        "function": {
                            "name": "calculator",
                            "arguments": '{"expression": "2+2"}',
                        },
                    }
                ],
            },
            {"role": "tool", "content": "4", "tool_call_id": "call-1"},
        ],
        "tools": tools,
        "tool_choice": "auto",
    }


async def test_openai_adapter_normalizes_provider_errors() -> None:
    class BrokenCompletions:
        async def create(self, **kwargs: object) -> object:
            raise RuntimeError("provider down")

    raw_client = SimpleNamespace(chat=SimpleNamespace(completions=BrokenCompletions()))
    client = OpenAICompatibleClient(raw_client=raw_client, model="demo")

    with pytest.raises(LLMClientError, match="provider down"):
        await client.complete([Message(role="user", content="hello")], tools=[])


class _AsyncResult:
    def __init__(self, value: object) -> None:
        self._value = value

    async def __call__(self, **kwargs: object) -> object:
        return self._value


class _RecordingCompletions:
    def __init__(self, response: object) -> None:
        self._response = response
        self.request: dict[str, object] | None = None

    async def create(self, **kwargs: object) -> object:
        self.request = kwargs
        return self._response
