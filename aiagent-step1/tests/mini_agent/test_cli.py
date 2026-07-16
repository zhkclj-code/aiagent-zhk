from mini_agent.cli import run_cli


async def test_cli_runs_offline_calculator(capsys) -> None:
    exit_code = await run_cli(["计算 2 + 2"])
    output = capsys.readouterr().out
    assert exit_code == 0
    assert "4" in output


async def test_cli_reports_expected_configuration_error(capsys, monkeypatch) -> None:
    monkeypatch.setattr("mini_agent.config.load_dotenv", lambda: False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    exit_code = await run_cli(["--provider", "openai", "hello"])
    output = capsys.readouterr().err
    assert exit_code == 2
    assert "OPENAI_API_KEY" in output
