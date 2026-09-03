def generate_report(results):
    if "error" in results:
        return f"Error: {results['error']}"

    status = "Clean" if not results["git_status"] else "Changes detected"

    report = []

    report.append("=== Git Repository Health Report ===")
    report.append("")
    report.append(f"Git Status: {status}")
    report.append(
        f"Recent Commits: {len(results['recent_commits'])}"
    )
    report.append(
        f"Branches: {len(results['branches'])}"
    )
    report.append(
        f"TODO/FIXME: {len(results['todo_fixme'])}"
    )
    report.append(
        f"Tests Present: {'Yes' if results['tests_present'] else 'No'}"
    )
    report.append(
        f"Documentation: "
        f"{'Yes' if results['documentation_present'] else 'No'}"
    )

    return "\n".join(report)