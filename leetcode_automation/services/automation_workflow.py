"""
automation_workflow.py

Runs the complete automation workflow.
"""

from leetcode_automation.managers.git_manager import (
    GitManager,
)
from leetcode_automation.services.change_detector import (
    ChangeDetector,
)
from leetcode_automation.services.commit_message_generator import (
    CommitMessageGenerator,
)
from leetcode_automation.services.readme_manager import (
    ReadmeManager,
)
from leetcode_automation.utils.logger import Logger


class AutomationWorkflow:
    """Runs the complete automation workflow."""

    def __init__(self) -> None:
        """Initialize the automation workflow."""

        self._logger = Logger()
        self._git = GitManager()
        self._change_detector = ChangeDetector()
        self._commit_generator = (
            CommitMessageGenerator()
        )
        self._readme = ReadmeManager()

    def run(self, path: str) -> None:
        """Run the automation workflow."""

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
                    self._commit_generator.generate(
                        change
                    )
                )

                self._logger.info(
                    f"Commit message: {commit_message}"
                )

        self._readme.update()

        self._logger.info(
            "README updated successfully."
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