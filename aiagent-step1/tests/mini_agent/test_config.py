import pytest

from mini_agent.client import FakeLLMClient
from mini_agent.config import AgentSettings, create_client
from mini_agent.errors import ConfigurationError


def test_settings_default_to_fake(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("MINI_AGENT_PROVIDER", raising=False)
    assert AgentSettings.from_env().provider == "fake"


def test_real_provider_requires_api_key() -> None:
    settings = AgentSettings(provider="openai", api_key=None)
    with pytest.raises(ConfigurationError, match="OPENAI_API_KEY"):
        create_client(settings)


def test_fake_provider_creates_fake_client() -> None:
    assert isinstance(create_client(AgentSettings()), FakeLLMClient)


def test_settings_reject_unknown_provider() -> None:
    with pytest.raises(ConfigurationError, match="provider"):
        AgentSettings(provider="unknown")

