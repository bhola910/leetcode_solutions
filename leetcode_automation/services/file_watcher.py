"""
file_watcher.py

Monitors the solutions directory for file changes.
"""

from leetcode_automation.utils.logger import Logger


class FileWatcher:
    """Watches the solutions directory."""

    def __init__(self) -> None:
        """Initialize the file watcher."""

        self._logger = Logger()