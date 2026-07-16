import pytest
from pydantic import ValidationError

from mini_agent.models import LLMReply, Message, ToolCall, ToolResult


def test_llm_reply_requires_content_or_tool_call() -> None:
    with pytest.raises(ValidationError):
        LLMReply()


def test_tool_result_converts_to_tool_message() -> None:
    result = ToolResult(tool_call_id="call-1", name="calculator", content="4")
    assert result.to_message() == Message(
        role="tool",
        content="4",
        name="calculator",
        tool_call_id="call-1",
    )


def test_assistant_message_retains_tool_calls() -> None:
    call = ToolCall(id="call-1", name="calculator", arguments={"expression": "2+2"})
    message = Message(role="assistant", content=None, tool_calls=[call])
    assert message.tool_calls == [call]
