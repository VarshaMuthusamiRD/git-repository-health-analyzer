# CLAUDE.md

## Purpose

Git Repository Health Analyzer is a Python CLI tool that analyzes a local Git repository and produces a quick health report.

The MVP checks:

* Git working-tree status
* Recent commits
* Branch information
* TODO/FIXME comments
* Test presence
* Basic documentation presence

The analyzer must inspect the repository without modifying its files or Git history.

---

## Commands

### Check Python Version

```bash
python --version
```

### Check Git Version

```bash
git --version
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment — Windows

```bash
.venv\Scripts\activate
```

### Activate Virtual Environment — macOS/Linux

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

> Add `requirements.txt` when project dependencies are defined.

### Run the Application

```bash
python -m repo_health <repository-path>
```

> Verify and update this command when the CLI entry point is implemented.

### Run Tests

```bash
pytest
```

---

## Structure

```text
src/
└── repo_health/
    ├── __init__.py
    ├── cli.py
    ├── analyzer.py
    ├── git_checks.py
    ├── file_checks.py
    └── report.py

tests/
└── __init__.py
```

### Module Responsibilities

**`cli.py`**

* Handles command-line input.
* Accepts the repository path.
* Calls the analyzer.
* Displays the final report.

**`analyzer.py`**

* Coordinates repository analysis.
* Combines the individual checks.

**`git_checks.py`**

* Git status check.
* Recent commits check.
* Branch check.

**`file_checks.py`**

* TODO/FIXME detection.
* Test detection.
* Documentation detection.

**`report.py`**

* Formats analysis results.
* Produces the terminal health report.

---

## Conventions

* Keep the CLI and analysis logic separate.
* Keep individual repository checks small and focused.
* Do not add features outside the MVP without updating `SPEC.md` and `TASKS.md`.
* Use clear error messages for invalid repository paths.
* Do not modify the repository being analyzed.
* Keep changes focused on the assigned task.

---

## Testing

Run all tests with:

```bash
pytest
```

Before opening a pull request:

1. Run the test suite.
2. Confirm the application still runs.
3. Confirm no unrelated files or functionality were changed.

---

## Do Not

Do not:

* Modify the analyzed repository.
* Create, modify, or delete Git commits automatically.
* Create or delete branches automatically.
* Add GitHub/GitLab integration.
* Add AI-powered code review.
* Add automatic fixing.
* Add features outside the approved MVP scope without agreement.

---

## Development Workflow

* Do not push directly to `main`.
* Create a branch for changes.
* Commit focused changes.
* Open a pull request.
* Review the pull request before merging.
* Keep `main` in a working state.

---

## Before Considering Work Complete

Verify:

```bash
python --version
git --version
pytest
```

Also verify that the documented application run command works against a test Git repository.

If any command in this document does not work, update the documentation rather than leaving an unverified command.
