"""Environment-backed configuration and client construction."""

from dataclasses import dataclass
import os

from dotenv import load_dotenv

from .client import FakeLLMClient, LLMClient, OpenAICompatibleClient
from .errors import ConfigurationError


@dataclass(frozen=True)
class AgentSettings:
    """Runtime settings with offline-safe defaults."""

    provider: str = "fake"
    api_key: str | None = None
    base_url: str | None = None
    model: str = "glm-5.2"
    max_tool_rounds: int = 3

    def __post_init__(self) -> None:
        if self.provider not in {"fake", "openai"}:
            raise ConfigurationError(f"不支持的 provider: {self.provider}")
        if self.max_tool_rounds < 1:
            raise ConfigurationError("MINI_AGENT_MAX_TOOL_ROUNDS 必须大于 0")
        if not self.model.strip():
            raise ConfigurationError("model 不能为空")

    @classmethod
    def from_env(cls, provider_override: str | None = None) -> "AgentSettings":
        load_dotenv()
        raw_rounds = os.getenv("MINI_AGENT_MAX_TOOL_ROUNDS", "3")
        try:
            max_tool_rounds = int(raw_rounds)
        except ValueError as error:
            raise ConfigurationError(
                "MINI_AGENT_MAX_TOOL_ROUNDS 必须是整数"
            ) from error

        provider = provider_override or os.getenv("MINI_AGENT_PROVIDER") or "fake"
        return cls(
            provider=provider.strip().lower(),
            api_key=os.getenv("OPENAI_API_KEY") or None,
            base_url=os.getenv("OPENAI_API_BASE") or None,
            model=os.getenv("OPENAI_MODEL_NAME", "glm-5.2"),
            max_tool_rounds=max_tool_rounds,
        )


def create_client(settings: AgentSettings) -> LLMClient:
    """Create the selected client after validating provider requirements."""

    if settings.provider == "fake":
        return FakeLLMClient()
    if not settings.api_key or not settings.api_key.strip():
        raise ConfigurationError("使用 openai provider 时必须设置 OPENAI_API_KEY")
    return OpenAICompatibleClient.create(
        api_key=settings.api_key.strip(),
        base_url=settings.base_url,
        model=settings.model,
    )
