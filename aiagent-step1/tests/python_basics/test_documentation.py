import re

from .test_course_structure import COURSE_ROOT, MODULES


PROJECT_ROOT = COURSE_ROOT.parents[1]
COURSE_DOCS = [
    PROJECT_ROOT / "README.md",
    PROJECT_ROOT / "notes" / "01-基础准备" / "Python学习路径.md",
    PROJECT_ROOT / "notes" / "01-基础准备" / "练习文件清单.md",
    COURSE_ROOT / "README.md",
]


def test_course_docs_do_not_reference_stale_filenames() -> None:
    stale_names = (
        "practice_day",
        "_exercises.py",
        "python_vs_java.py",
        "pythonic_syntax.py",
        "oop.py",
        "decorators.py",
        "exceptions_and_files.py",
        "modules_and_packages.py",
        "async_basics.py",
        "async_practice.py",
        "type_hints.py",
        "pytest_basics.py",
        "comprehensive_project.py",
        "logging_basics.py",
        "dataclasses_basics.py",
        "generators.py",
    )
    for document in COURSE_DOCS:
        content = document.read_text(encoding="utf-8")
        assert not any(name in content for name in stale_names), document


def test_course_index_references_every_module_file() -> None:
    content = (COURSE_ROOT / "README.md").read_text(encoding="utf-8")
    for module in MODULES:
        assert f"{module}/lesson.py" in content
        assert f"{module}/exercises.py" in content
    assert "15-mini-agent/README.md" in content


def test_backticked_course_paths_exist() -> None:
    pattern = re.compile(r"`(code/python-basics/[^`]+)`")
    for document in COURSE_DOCS:
        for relative_path in pattern.findall(document.read_text(encoding="utf-8")):
            assert (PROJECT_ROOT / relative_path).exists(), f"{document}: {relative_path}"
