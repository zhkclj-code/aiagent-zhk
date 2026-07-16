import pytest

from mini_agent.cli import run_cli


@pytest.fixture(autouse=True)
def isolate_agent_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("mini_agent.config.load_dotenv", lambda: False)
    for name in (
        "MINI_AGENT_PROVIDER",
        "MINI_AGENT_MAX_TOOL_ROUNDS",
        "OPENAI_API_KEY",
        "OPENAI_API_BASE",
        "OPENAI_MODEL_NAME",
    ):
        monkeypatch.delenv(name, raising=False)


async def test_cli_runs_offline_calculator(capsys) -> None:
    exit_code = await run_cli(["--provider", "fake", "计算 2 + 2"])
    output = capsys.readouterr().out
    assert exit_code == 0
    assert "4" in output


async def test_cli_reports_expected_configuration_error(capsys, monkeypatch) -> None:
    exit_code = await run_cli(["--provider", "openai", "hello"])
    output = capsys.readouterr().err
    assert exit_code == 2
    assert "OPENAI_API_KEY" in output
