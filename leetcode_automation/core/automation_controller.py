"""
automation_controller.py

Coordinates all automation components.
"""

from leetcode_automation.managers.config_manager import ConfigManager
from leetcode_automation.managers.git_manager import GitManager
from leetcode_automation.utils.logger import Logger


class AutomationController:
    """Coordinates the automation workflow."""

    def __init__(self) -> None:
        """Initialize the automation controller."""

        self._logger = Logger()
        self._config = ConfigManager()
        self._git = GitManager()

    def process_solution(self, path: str) -> None:
        """Process a newly detected solution."""

        self._logger.info(
            f"Starting automation for: {path}"
        )