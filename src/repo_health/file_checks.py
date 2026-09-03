from pathlib import Path


def find_todo_fixme(repo_path):
    matches = []

    for path in Path(repo_path).rglob("*"):
        if not path.is_file():
            continue

        if ".git" in path.parts:
            continue

        try:
            content = path.read_text(
                encoding="utf-8",
                errors="ignore"
            )
        except Exception:
            continue

        for line_number, line in enumerate(content.splitlines(), 1):
            if "TODO" in line or "FIXME" in line:
                matches.append(
                    f"{path}:{line_number}: {line.strip()}"
                )

    return matches

def check_tests(repo_path):
    path = Path(repo_path)

    test_directories = [
        "tests",
        "test"
    ]

    for directory in test_directories:
        if (path / directory).exists():
            return True

    for file in path.rglob("test_*.py"):
        if ".git" not in file.parts:
            return True

    return False

def check_documentation(repo_path):
    path = Path(repo_path)

    return (
        (path / "README.md").exists()
        or (path / "README").exists()
        or (path / "README.txt").exists()
    )