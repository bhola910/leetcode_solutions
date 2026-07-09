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
from leetcode_automation.services.solution_parser import (
    SolutionParser,
)
from leetcode_automation.utils.logger import Logger


class AutomationWorkflow:
    """Runs the complete automation workflow."""

    def __init__(self) -> None:
        """Initialize the automation workflow."""

        self._logger = Logger()
        self._git = GitManager()
        self._parser = SolutionParser()
        self._readme = ReadmeManager()
        self._change_detector = ChangeDetector()
        self._commit_generator = CommitMessageGenerator()

    def _parse_solution(self, path: str):
        """Parse the solution file."""

        try:
            return self._parser.parse(path)

        except ValueError as error:
            self._logger.error(str(error))
            return None

    def _log_changes(self) -> bool:
        """Log detected Git changes."""

        changes = (
            self._change_detector.get_solution_changes()
        )

        if not changes:

            self._logger.warning(
                "No solution changes detected."
            )

            return False

        self._logger.info(
            f"Detected {len(changes)} Git change(s):"
        )

        for change in changes:

            self._logger.info(
                f"{change.status} -> {change.path}"
            )

        return True

    def _update_repository(
        self,
        commit_message: str,
    ) -> None:
        """Update the repository."""

        self._readme.update()

        self._logger.info(
            "README updated successfully."
        )

        self._git.add()

        self._logger.info(
            "Files staged successfully."
        )

        self._git.commit(commit_message)

        self._logger.info(
            "Commit created successfully."
        )

    def run(self, path: str) -> None:
        """Run the automation workflow."""

        self._logger.info(
            f"Starting automation for: {path}"
        )

        solution = self._parse_solution(path)

        if solution is None:
            return

        commit_message = (
            self._commit_generator.generate(
                solution
            )
        )

        self._logger.info(
            f"Commit message: {commit_message}"
        )

        if self._git.repository_clean():

            self._logger.info(
                "Repository is already clean."
            )

            return

        if not self._log_changes():
            return

        try:

            self._update_repository(
                commit_message
            )

        except Exception as error:

            self._logger.error(
                f"Automation failed: {error}"
            )