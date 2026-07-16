"""Pydantic models shared by clients, tools, and the Agent loop."""

from typing import Any, Literal, Self

from pydantic import BaseModel, Field, model_validator


class ToolCall(BaseModel):
    """A model request to invoke one registered tool."""

    id: str
    name: str
    arguments: dict[str, Any] = Field(default_factory=dict)


class Message(BaseModel):
    """One provider-neutral conversation message."""

    role: Literal["system", "user", "assistant", "tool"]
    content: str | None = None
    name: str | None = None
    tool_call_id: str | None = None
    tool_calls: list[ToolCall] = Field(default_factory=list)


class LLMReply(BaseModel):
    """A provider-neutral model reply."""

    content: str | None = None
    tool_calls: list[ToolCall] = Field(default_factory=list)

    @model_validator(mode="after")
    def require_output(self) -> Self:
        if not (self.content and self.content.strip()) and not self.tool_calls:
            raise ValueError("LLM reply must contain content or at least one tool call")
        return self


class ToolResult(BaseModel):
    """The structured result of executing one tool call."""

    tool_call_id: str
    name: str
    content: str
    is_error: bool = False

    def to_message(self) -> Message:
        return Message(
            role="tool",
            content=self.content,
            name=self.name,
            tool_call_id=self.tool_call_id,
        )


class AgentResponse(BaseModel):
    """The final response plus the conversation state that produced it."""

    content: str
    messages: list[Message]
    tool_rounds: int = Field(ge=0)
