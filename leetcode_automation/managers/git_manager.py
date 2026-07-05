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

    def status(self) -> None:
        """Display the current Git status."""

        self._logger.info("Running git status...")

        subprocess.run(
            ["git", "status"],
            check=True,
            text=True,
        )