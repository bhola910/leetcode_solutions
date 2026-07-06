from leetcode_automation.managers.git_manager import GitManager


def main():
    git = GitManager()

    git.add()

    git.commit("Test commit from GitManager")


if __name__ == "__main__":
    main()

class GitManager:
    """Provides Git-related operations."""

    def __init__(self) -> None:
        """Initialize the Git manager."""

        self._logger = Logger()

    def status(self) -> str:
        """Return the current Git status."""

        self._logger.info("Running git status...")

        result = subprocess.run(
            ["git", "status"],
            capture_output=True,
            text=True,
            check=True,
        )

        return result.stdout