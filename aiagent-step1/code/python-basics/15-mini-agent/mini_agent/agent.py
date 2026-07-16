"""The bounded Agent execution loop."""

from .client import LLMClient
from .errors import AgentLoopError
from .models import AgentResponse, Message
from .tools import ToolRegistry


class MiniAgent:
    """Run model replies and tool calls without depending on an Agent framework."""

    def __init__(
        self,
        client: LLMClient,
        tools: ToolRegistry,
        *,
        max_tool_rounds: int = 3,
    ) -> None:
        if max_tool_rounds < 1:
            raise ValueError("max_tool_rounds 必须大于 0")
        self._client = client
        self._tools = tools
        self._max_tool_rounds = max_tool_rounds
        self._history: list[Message] = []

    @property
    def history(self) -> list[Message]:
        return list(self._history)

    def clear_history(self) -> None:
        self._history.clear()

    async def run(self, user_input: str) -> AgentResponse:
        self._history.append(Message(role="user", content=user_input))
        tool_rounds = 0

        while True:
            reply = await self._client.complete(self.history, self._tools.schemas())
            self._history.append(
                Message(
                    role="assistant",
                    content=reply.content,
                    tool_calls=reply.tool_calls,
                )
            )

            if not reply.tool_calls:
                return AgentResponse(
                    content=reply.content or "",
                    messages=self.history,
                    tool_rounds=tool_rounds,
                )

            if tool_rounds >= self._max_tool_rounds:
                raise AgentLoopError(
                    f"工具调用超过 {self._max_tool_rounds} 轮上限"
                )

            for call in reply.tool_calls:
                result = self._tools.execute(call)
                self._history.append(result.to_message())
            tool_rounds += 1
