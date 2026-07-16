"""Command-line entry point for the Mini Agent capstone."""

import argparse
import asyncio
from collections.abc import Sequence
import sys
from typing import NoReturn

from .agent import MiniAgent
from .config import AgentSettings, create_client
from .errors import MiniAgentError
from .tools import ToolRegistry


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="运行 Mini Agent 综合项目")
    parser.add_argument("question", nargs="?", help="要交给 Agent 的问题")
    parser.add_argument(
        "--provider",
        choices=["fake", "openai"],
        help="默认读取 MINI_AGENT_PROVIDER，未配置时使用 fake",
    )
    return parser


async def run_cli(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        settings = AgentSettings.from_env(provider_override=args.provider)
        agent = MiniAgent(
            create_client(settings),
            ToolRegistry.default(),
            max_tool_rounds=settings.max_tool_rounds,
        )
        if args.question:
            response = await agent.run(args.question)
            print(response.content)
            return 0
        return await _interactive(agent)
    except MiniAgentError as error:
        print(f"Mini Agent 错误: {error}", file=sys.stderr)
        return 2


async def _interactive(agent: MiniAgent) -> int:
    print("Mini Agent 已启动；输入 quit 或 exit 退出。")
    while True:
        try:
            question = input("你: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
        if question.lower() in {"quit", "exit"}:
            return 0
        if not question:
            continue
        response = await agent.run(question)
        print(f"Agent: {response.content}")


def main() -> NoReturn:
    raise SystemExit(asyncio.run(run_cli()))
