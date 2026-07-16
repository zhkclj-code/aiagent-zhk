import os

import pytest

from mini_agent.config import AgentSettings, create_client
from mini_agent.models import Message


@pytest.mark.integration
async def test_real_openai_compatible_client() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        pytest.skip("OPENAI_API_KEY 未配置")
    settings = AgentSettings.from_env(provider_override="openai")
    client = create_client(settings)
    reply = await client.complete([Message(role="user", content="只回复 ok")], tools=[])
    assert reply.content
