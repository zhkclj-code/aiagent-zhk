"""Provider-neutral LLM clients for the Mini Agent."""

from collections import deque
from collections.abc import Iterable
from itertools import count
import json
from typing import Any, Protocol

from openai import AsyncOpenAI

from .errors import LLMClientError
from .models import LLMReply, Message, ToolCall


class LLMClient(Protocol):
    """The asynchronous model interface consumed by MiniAgent."""

    async def complete(
        self,
        messages: list[Message],
        tools: list[dict[str, Any]],
    ) -> LLMReply:
        """Return one provider-neutral completion."""


class FakeLLMClient:
    """A deterministic offline client for learning and automated tests."""

    def __init__(self, replies: Iterable[LLMReply] | None = None) -> None:
        self._scripted = deque(replies) if replies is not None else None
        self._call_ids = count(1)

    async def complete(
        self,
        messages: list[Message],
        tools: list[dict[str, Any]],
    ) -> LLMReply:
        del tools
        if self._scripted is not None:
            if not self._scripted:
                raise LLMClientError("Fake LLM 的预设响应已用完")
            return self._scripted.popleft()

        if not messages:
            return LLMReply(content="Fake Agent 已就绪")

        last = messages[-1]
        content = (last.content or "").strip()
        if last.role == "tool":
            return LLMReply(content=f"工具 {last.name} 返回：{content}")
        if content.startswith("计算 "):
            return LLMReply(
                tool_calls=[
                    ToolCall(
                        id=f"fake-{next(self._call_ids)}",
                        name="calculator",
                        arguments={"expression": content.removeprefix("计算 ").strip()},
                    )
                ]
            )
        if "时间" in content:
            return LLMReply(
                tool_calls=[
                    ToolCall(
                        id=f"fake-{next(self._call_ids)}",
                        name="current_time",
                        arguments={},
                    )
                ]
            )
        return LLMReply(content=f"Fake Agent: {content}")


class OpenAICompatibleClient:
    """Adapt an OpenAI-compatible async chat client to LLMClient."""

    def __init__(self, *, raw_client: Any, model: str) -> None:
        self._raw_client = raw_client
        self._model = model

    @classmethod
    def create(
        cls,
        *,
        api_key: str,
        model: str,
        base_url: str | None = None,
    ) -> "OpenAICompatibleClient":
        raw_client = AsyncOpenAI(api_key=api_key, base_url=base_url)
        return cls(raw_client=raw_client, model=model)

    async def complete(
        self,
        messages: list[Message],
        tools: list[dict[str, Any]],
    ) -> LLMReply:
        request: dict[str, Any] = {
            "model": self._model,
            "messages": [self._message_payload(message) for message in messages],
        }
        if tools:
            request["tools"] = tools
            request["tool_choice"] = "auto"

        try:
            response = await self._raw_client.chat.completions.create(**request)
            raw_message = response.choices[0].message
            tool_calls = [self._tool_call(call) for call in (raw_message.tool_calls or [])]
            return LLMReply(content=raw_message.content, tool_calls=tool_calls)
        except LLMClientError:
            raise
        except Exception as error:
            raise LLMClientError(f"模型调用失败: {error}") from error

    @staticmethod
    def _message_payload(message: Message) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "role": message.role,
            "content": message.content,
        }
        if message.role == "assistant" and message.tool_calls:
            payload["tool_calls"] = [
                {
                    "id": call.id,
                    "type": "function",
                    "function": {
                        "name": call.name,
                        "arguments": json.dumps(call.arguments, ensure_ascii=False),
                    },
                }
                for call in message.tool_calls
            ]
        if message.role == "tool":
            payload["tool_call_id"] = message.tool_call_id
        return payload

    @staticmethod
    def _tool_call(raw_call: Any) -> ToolCall:
        arguments = json.loads(raw_call.function.arguments or "{}")
        if not isinstance(arguments, dict):
            raise LLMClientError("工具参数必须是 JSON object")
        return ToolCall(
            id=raw_call.id,
            name=raw_call.function.name,
            arguments=arguments,
        )
