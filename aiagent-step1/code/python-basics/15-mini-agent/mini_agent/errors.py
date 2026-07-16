"""Domain exceptions for the Mini Agent."""


class MiniAgentError(Exception):
    """Base exception for expected Mini Agent failures."""


class ConfigurationError(MiniAgentError):
    """Raised when runtime configuration is invalid."""


class LLMClientError(MiniAgentError):
    """Raised when the model provider cannot complete a request."""


class ToolError(MiniAgentError):
    """Raised when tool input or execution is invalid."""


class AgentLoopError(MiniAgentError):
    """Raised when the Agent exceeds its tool-call round limit."""
