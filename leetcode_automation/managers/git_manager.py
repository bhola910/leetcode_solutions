"""
git_manager.py

Handles Git operations for the project.
"""

import subprocess

from leetcode_automation.utils.logger import Logger


class GitManager:
    """Provides Git-related operations."""

    def __init__(self) -> None:
        """Initialize the Git manager."""

        self._logger = Logger()

    def _run_git_command(self, command: list[str]) -> str:
        """Execute a Git command and return its output."""

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True,
            )

            return result.stdout if result.stdout else result.stderr

        except subprocess.CalledProcessError as error:
            self._logger.error(f"Git command failed: {error}")
            raise

    def status(self) -> str:
        """Return the current Git status."""

        self._logger.info("Running git status...")

        return self._run_git_command(
            ["git", "status"]
        )

    def add(self, path: str = ".") -> None:
        """Stage files or directories for commit."""

        self._logger.info(f"Running git add '{path}'...")

        self._run_git_command(
            ["git", "add", path]
        )

    def commit(self, message: str) -> None:
        """Create a Git commit."""

        if not message.strip():
            raise ValueError("Commit message cannot be empty.")

        self._logger.info(f"Running git commit: '{message}'")

        self._run_git_command(
            ["git", "commit", "-m", message]
        )

    def push(
        self,
        remote: str = "origin",
        branch: str = "main",
    ) -> str:
        """Push commits to the remote repository."""

        self._logger.info(
            f"Running git push {remote} {branch}..."
        )

        return self._run_git_command(
            ["git", "push", remote, branch]
        )
    

    def pull(
        self,
        remote: str = "origin",
        branch: str = "main",
    ) -> str:
        """Pull changes from the remote repository."""

        self._logger.info(
            f"Running git pull {remote} {branch}..."
        )

        return self._run_git_command(
            ["git", "pull", remote, branch]
        )
    

    def current_branch(self) -> str:
        """Return the current Git branch."""

        self._logger.info(
            "Getting current Git branch..."
        )

        return self._run_git_command(
            ["git", "branch", "--show-current"]
        ).strip()
    
    def repository_clean(self) -> bool:
        """Return True if the repository has no changes."""

        status = self.status()

        return "nothing to commit" in status.lower()