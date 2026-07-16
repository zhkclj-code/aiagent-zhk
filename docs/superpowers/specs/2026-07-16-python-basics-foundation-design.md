# Python Basics Foundation Design

## Goal

Turn `aiagent-step1/code/python-basics` into a consistent, runnable Python
foundation course for a Java developer preparing for AI Agent development.
Repair the known syntax and runtime failures, establish a real automated test
system, normalize course names and references, and add an offline-first Mini
Agent capstone with an optional OpenAI-compatible client.

## Scope

This change covers the Python foundation course and its direct documentation.
It does not implement LangChain, LangGraph, RAG, vector databases, or a
production deployment platform. Those remain later learning stages.

## Course Structure

The course uses module numbers rather than inconsistent day numbers. Existing
module directories remain numbered `01` through `14`; a new capstone becomes
module `15`.

Every existing module uses the same filenames:

- `lesson.py`: runnable reference material and examples
- `exercises.py`: learner exercises, which must at least parse successfully

The old topic-specific lesson filenames and `practice_day*.py` filenames are
renamed. Documentation references only paths that exist after the rename.

The course index records these modules:

1. Syntax and Java comparison
2. Pythonic language features
3. Object-oriented Python
4. Decorators and context managers
5. Exceptions and files
6. Modules and packages
7. Async fundamentals
8. Async patterns and practice
9. Type hints and Pydantic
10. Testing with pytest
11. Comprehensive Python project
12. Logging
13. Dataclasses
14. Generators, regular expressions, and pathlib
15. Mini Agent capstone

## Existing Runtime Repairs

The implementation repairs the reproduced failures at their causes:

- `01-syntax/lesson.py` creates or supplies its own demonstration input rather
  than assuming `test.txt` exists in the caller's working directory.
- `06-modules/lesson.py` uses `sys.executable` for child Python processes.
- `09-type-hints/lesson.py` uses current Pydantic v2 configuration and declares
  the email validation dependency used by `EmailStr`.
- `10-testing/lesson.py` imports `sys` and patches the module that actually owns
  the target function.
- `11-project/exercises.py` uses valid string boundaries and parses normally.
- Network examples are opt-in so normal lesson runs are deterministic and do
  not depend on internet access.

## Mini Agent Architecture

The capstone is a small package under
`code/python-basics/15-mini-agent/mini_agent/`. Each module has one purpose:

- `models.py`: messages, tool calls, tool results, and agent response models
- `errors.py`: configuration, client, tool, and loop-limit exceptions
- `client.py`: `LLMClient` protocol, deterministic `FakeLLMClient`, and
  OpenAI-compatible async adapter
- `tools.py`: tool protocol, registry, safe calculator, and current-time tool
- `agent.py`: bounded Agent execution loop and conversation history
- `config.py`: environment-backed configuration and client selection
- `cli.py`: async command-line entry point

The core flow is:

1. The CLI loads configuration and creates a Fake or OpenAI client.
2. `MiniAgent` sends the conversation and available tool schemas to the client.
3. A normal model message ends the turn.
4. A tool call is validated and executed by `ToolRegistry`.
5. The tool result is appended to the conversation and sent back to the model.
6. The loop stops after at most three tool rounds.

The Fake client is the default and follows deterministic scripted responses.
Setting the documented environment variables enables the real client without
changing application code.

## Error Handling

- Selecting the real client without an API key raises a clear
  `ConfigurationError` before any request is made.
- Provider failures are normalized as `LLMClientError` while preserving the
  original exception as the cause.
- Unknown tools and invalid tool arguments become structured tool-error results
  that the model can observe; they do not terminate the process.
- Unsafe or unsupported calculator expressions are rejected without `eval`.
- More than the configured tool-call rounds raises `AgentLoopError`.
- CLI failures produce a concise message and a non-zero exit status.

## Test System

`pytest` is the single test entry point. `pyproject.toml` defines discovery,
markers, asyncio behavior, and development dependencies.

The suite contains:

- course structure tests that verify normalized names and documentation paths
- AST parsing tests for all `lesson.py` and `exercises.py` files
- subprocess smoke tests that run every lesson in an isolated temporary working
  directory with network examples disabled
- focused regression tests for each reproduced runtime failure
- unit tests for models, tools, registry, configuration, and Agent behavior
- async tests for normal replies, successful tool use, tool errors, provider
  errors, and the loop limit
- an `integration` marker for optional real API tests, excluded by default

`pytest-asyncio` is required because Agent and client behavior is asynchronous.
`pytest-cov` is available for coverage reporting, but coverage percentage is a
diagnostic rather than a substitute for behavioral assertions.

## Dependencies And Tooling

`aiagent-step1/pyproject.toml` becomes the authoritative foundation-project
configuration. Runtime dependencies remain minimal: OpenAI SDK, Pydantic with
email support, and python-dotenv. Test and quality tools are development extras:
pytest, pytest-asyncio, pytest-cov, Ruff, and mypy.

Agent frameworks and data-platform dependencies are optional extras for later
stages. Existing setup documentation is updated to use the new installation and
test commands.

## Documentation Normalization

The following documentation is reconciled with the filesystem:

- root README directory tree and current progress
- Python learning path and module numbering
- exercise file checklist
- setup guide and test commands
- references to lesson and exercise filenames

Statements claiming Python has no interfaces, no generics, or that asyncio is
the equivalent of all Java multithreading are corrected. The comparison instead
distinguishes structural protocols, typed generics, threads, processes, and
async I/O concurrency.

## Acceptance Criteria

- Every Python file parses under Python 3.11.
- All fourteen existing lesson scripts run successfully from isolated working
  directories without network access.
- `pytest` discovers tests with a normal command and exits successfully.
- No documentation link or referenced course file is missing.
- Fake Mini Agent runs without credentials and demonstrates at least one tool
  call.
- Real-client configuration is optional and validated before use.
- Agent tests make no network calls and consume no API quota.
- The Git worktree contains no generated logs, caches, or lesson output files
  after verification.
