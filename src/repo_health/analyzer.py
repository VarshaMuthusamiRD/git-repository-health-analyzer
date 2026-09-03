from pathlib import Path

from repo_health.git_checks import (
    check_git_status,
    get_recent_commits,
    get_branches
)

from repo_health.file_checks import (
    find_todo_fixme,
    check_tests,
    check_documentation
)


def is_git_repository(repo_path):
    path = Path(repo_path)

    return (
        path.exists()
        and path.is_dir()
        and (path / ".git").exists()
    )


def analyze_repository(repo_path):
    if not is_git_repository(repo_path):
        return {
            "error": "The provided path is not a valid Git repository."
        }

    return {
        "git_status": check_git_status(repo_path),
        "recent_commits": get_recent_commits(repo_path),
        "branches": get_branches(repo_path),
        "todo_fixme": find_todo_fixme(repo_path),
        "tests_present": check_tests(repo_path),
        "documentation_present": check_documentation(repo_path)
    }