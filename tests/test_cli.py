import os
import subprocess
import sys


def test_cli_without_repository_path_prints_usage():
    env = dict(os.environ, PYTHONPATH="src")

    result = subprocess.run(
        [sys.executable, "-m", "repo_health"],
        capture_output=True,
        text=True,
        env=env,
    )

    assert "Usage: python -m repo_health <repository-path>" in result.stdout
