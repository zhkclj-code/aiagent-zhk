from pathlib import Path


COURSE_ROOT = Path(__file__).parents[2] / "code" / "python-basics"
MODULES = [
    "01-syntax",
    "02-features",
    "03-oop",
    "04-decorators",
    "05-exceptions",
    "06-modules",
    "07-async",
    "08-async-practice",
    "09-type-hints",
    "10-testing",
    "11-project",
    "12-logging",
    "13-dataclasses",
    "14-generators-re",
]


def test_every_foundation_module_has_normalized_files() -> None:
    for module in MODULES:
        module_dir = COURSE_ROOT / module
        assert (module_dir / "lesson.py").is_file(), module
        assert (module_dir / "exercises.py").is_file(), module
