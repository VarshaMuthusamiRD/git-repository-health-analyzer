import sys

from repo_health.analyzer import analyze_repository


def main():
    if len(sys.argv) != 2:
        print("Usage: python -m repo_health <repository-path>")
        return

    repo_path = sys.argv[1]

    results = analyze_repository(repo_path)

    print(results)


if __name__ == "__main__":
    main()