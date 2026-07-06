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

    def status(self) -> str:
        """Return the current Git status."""

        self._logger.info("Running git status...")

        try:
            result = subprocess.run(
                ["git", "status"],
                capture_output=True,
                text=True,
                check=True,
            )

            return result.stdout

        except subprocess.CalledProcessError as error:
            self._logger.error(
                f"Git status failed: {error}"
            )
            raise
    
    def add(self, path: str = ".") -> None:
        """Stage files or directories for commit."""

        self._logger.info(f"Running git add '{path}'...")

        try:
            subprocess.run(
                ["git", "add", path],
                check=True,
                text=True,
            )

        except subprocess.CalledProcessError as error:
            self._logger.error(
                f"Git add failed: {error}"
            )
            raise
        

    def commit(self, message: str) -> None:
        """Create a Git commit."""

        if not message.strip():
            raise ValueError("Commit message cannot be empty.")

        self._logger.info(f"Running git commit: '{message}'")

        try:
            subprocess.run(
                ["git", "commit", "-m", message],
                check=True,
                text=True,
            )

        except subprocess.CalledProcessError as error:
            self._logger.error(
                f"Git commit failed: {error}"
            )
            raise