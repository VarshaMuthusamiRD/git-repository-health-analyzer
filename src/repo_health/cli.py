import sys

from repo_health.analyzer import analyze_repository
from repo_health.report import generate_report


def main():
    if len(sys.argv) != 2:
        print("Usage: python -m repo_health <repository-path>")
        return

    repo_path = sys.argv[1]

    results = analyze_repository(repo_path)

    print(generate_report(results))


if __name__ == "__main__":
    main()