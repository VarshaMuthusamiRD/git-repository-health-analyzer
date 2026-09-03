from repo_health.file_checks import (
    check_documentation,
    check_tests,
    find_todo_fixme,
)


def test_check_documentation_detects_readme(tmp_path):
    (tmp_path / "README.md").write_text("# Project")

    assert check_documentation(str(tmp_path)) is True


def test_check_documentation_missing(tmp_path):
    assert check_documentation(str(tmp_path)) is False


def test_check_tests_detects_tests_directory(tmp_path):
    (tmp_path / "tests").mkdir()

    assert check_tests(str(tmp_path)) is True


def test_check_tests_missing(tmp_path):
    assert check_tests(str(tmp_path)) is False


def test_find_todo_fixme_detects_markers(tmp_path):
    (tmp_path / "app.py").write_text(
        "print('hi')  # TODO: fix this\nprint('bye')  # FIXME: broken\n"
    )

    matches = find_todo_fixme(str(tmp_path))

    assert len(matches) == 2
    assert any("TODO" in match for match in matches)
    assert any("FIXME" in match for match in matches)


def test_find_todo_fixme_no_markers(tmp_path):
    (tmp_path / "app.py").write_text("print('nothing to see here')\n")

    assert find_todo_fixme(str(tmp_path)) == []
