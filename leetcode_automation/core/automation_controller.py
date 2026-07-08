"""
automation_controller.py

Coordinates all automation components.
"""

from leetcode_automation.managers.config_manager import ConfigManager
from leetcode_automation.managers.git_manager import GitManager
from leetcode_automation.services.change_detector import ChangeDetector
from leetcode_automation.services.commit_message_generator import (
    CommitMessageGenerator,
)
from leetcode_automation.utils.logger import Logger


class AutomationController:
    """Coordinates the automation workflow."""

    def __init__(self) -> None:
        """Initialize the automation controller."""

        self._logger = Logger()
        self._config = ConfigManager()
        self._git = GitManager()
        self._change_detector = ChangeDetector()
        self._commit_generator = CommitMessageGenerator()

    def process_solution(self, path: str) -> None:
        """Process a newly detected solution."""

        try:
            self._logger.info(
                f"Starting automation for: {path}"
            )

            if self._git.repository_clean():
                self._logger.info(
                    "Repository is already clean."
                )
                return

            solution_changes = (
                self._change_detector.get_solution_changes()
            )

            if not solution_changes:
                self._logger.warning(
                    "No solution changes detected."
                )
                return

            commit_message = None

            for change in solution_changes:

                self._logger.info(
                    f"{change.status} -> {change.path}"
                )

                if commit_message is None:
                    commit_message = (
                        self._commit_generator.generate(change)
                    )

                    self._logger.info(
                        f"Commit message: {commit_message}"
                    )

            self._git.add()

            self._logger.info(
                "Files staged successfully."
            )

            if commit_message:

                self._git.commit(commit_message)

                self._logger.info(
                    "Commit created successfully."
                )

        except Exception as error:
            self._logger.error(
                f"Automation failed: {error}"
            )