# Git Repository Health Analyzer — Specification

## 1. Problem

Developers often need to quickly understand the health of a Git repository before starting work, reviewing a project, or handing it over to someone else. Important information such as uncommitted changes, recent commits, branches, TODO/FIXME comments, tests, and documentation may require checking manually.

The **Git Repository Health Analyzer** provides a quick health assessment of a local Git repository through a command-line interface (CLI). It analyzes the repository and produces a simple terminal report showing the repository's current health.

The tool is intended to provide a quick overview rather than perform detailed code-quality or security analysis.

---

## 2. Users

The primary users are:

* Developers who want to quickly inspect the health of a local Git repository.
* Students working on software projects who need a simple repository health check.
* Teams reviewing or handing over a project and wanting a quick repository overview.

---

## 3. In Scope

The first version of the Git Repository Health Analyzer will:

1. Accept a path to a local Git repository.
2. Validate whether the provided path is a valid Git repository.
3. Check the Git working-tree status.
4. Display information about recent commits.
5. Display branch information.
6. Search the repository for `TODO` and `FIXME` comments.
7. Check whether tests are present in the repository.
8. Check whether basic documentation, such as a `README` file, is present.
9. Generate a simple health report in the terminal.
10. Provide clear error messages for invalid repository paths or non-Git directories.
11. Analyze the repository without modifying its files or Git history.

---

## 4. Out of Scope

The following features are intentionally excluded from the first version:

1. Automatic fixing of repository issues.
2. GitHub or GitLab integration.
3. AI-powered code review.
4. Automatic modification of source-code files.
5. Automatic creation, modification, or deletion of Git commits.
6. Automatic creation or deletion of branches.
7. Advanced code-quality analysis.
8. Security vulnerability scanning.
9. Continuous monitoring of repositories.
10. Web-based or graphical user interface.
11. Database or external storage for repository results.

These features may be considered in future versions but are not part of the MVP.

---

## 5. Stack

The initial implementation will use:

* **Language:** Python
* **Interface:** Command-Line Interface (CLI)
* **Git interaction:** Git commands through Python
* **Testing:** pytest
* **Storage:** None
* **Repository scope:** Local Git repositories only

The project will use a modular structure so that repository-analysis logic and the CLI interface can be developed and tested separately.

---

## 6. Success Criteria

The MVP will be considered successful when:

1. A user can provide a local repository path to the CLI.
2. The tool correctly identifies whether the path is a valid Git repository.
3. The tool reports the repository's Git status.
4. The tool reports recent commit information.
5. The tool reports branch information.
6. The tool detects `TODO` and `FIXME` comments.
7. The tool detects whether tests are present.
8. The tool detects whether basic documentation is present.
9. The tool displays the results as a readable terminal health report.
10. The tool gives a clear error when an invalid or non-Git repository path is provided.
11. The analyzer does not modify the repository being analyzed.
12. The core user flow works end-to-end from providing a repository path to receiving the health report.
13. The project can be installed, run, and tested using the commands documented in the project documentation.

---

## 7. Core Principle

The MVP should prioritize **reliable repository analysis and a clear health report** over advanced features.

The initial version should remain small, local, and easy to run. Additional functionality will only be considered after the core flow works reliably.
