import subprocess


def check_git_status(repo_path):
    result = subprocess.run(
        ["git", "-C", repo_path, "status", "--short"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return None

    return result.stdout.strip()

def get_recent_commits(repo_path):
    result = subprocess.run(
        [
            "git",
            "-C",
            repo_path,
            "log",
            "-5",
            "--oneline"
        ],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return []

    return result.stdout.strip().splitlines()

def get_branches(repo_path):
    result = subprocess.run(
        [
            "git",
            "-C",
            repo_path,
            "branch",
            "--list"
        ],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return []

    return result.stdout.strip().splitlines()

