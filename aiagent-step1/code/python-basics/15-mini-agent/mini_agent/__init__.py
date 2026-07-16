"""A small, framework-free Agent used by the Python foundation course."""

from .agent import MiniAgent
from .config import AgentSettings, create_client

__all__ = ["AgentSettings", "MiniAgent", "create_client"]
