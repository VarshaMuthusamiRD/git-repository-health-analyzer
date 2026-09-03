from repo_health.analyzer import is_git_repository


def test_current_directory_is_git_repository():
    assert is_git_repository(".") is True


def test_invalid_directory_is_not_git_repository(tmp_path):
    assert is_git_repository(str(tmp_path)) is False