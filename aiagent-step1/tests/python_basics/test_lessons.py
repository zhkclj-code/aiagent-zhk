import ast
import os
from pathlib import Path
import subprocess
import sys

import pytest

from .test_course_structure import COURSE_ROOT, MODULES


@pytest.mark.parametrize("module", MODULES)
@pytest.mark.parametrize("filename", ["lesson.py", "exercises.py"])
def test_course_file_parses(module: str, filename: str) -> None:
    path = COURSE_ROOT / module / filename
    ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


@pytest.mark.parametrize("module", MODULES)
def test_lesson_runs_in_isolated_directory(module: str, tmp_path: Path) -> None:
    lesson = COURSE_ROOT / module / "lesson.py"
    env = os.environ.copy()
    env["RUN_NETWORK_EXAMPLES"] = "0"
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run(
        [sys.executable, str(lesson)],
        cwd=tmp_path,
        env=env,
        capture_output=True,
        text=True,
        timeout=45,
        check=False,
    )
    assert result.returncode == 0, result.stderr
