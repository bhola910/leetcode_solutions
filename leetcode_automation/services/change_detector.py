"""
change_detector.py

Detects Git file changes.
"""

from leetcode_automation.managers.git_manager import GitManager
from leetcode_automation.models.change import Change


class ChangeDetector:
    """Detects Git repository changes."""

    def __init__(self) -> None:
        """Initialize the change detector."""

        self._git = GitManager()

    def get_changes(self) -> list[Change]:
        """Return all parsed Git changes."""

        output = self._git.status_porcelain()

        changes: list[Change] = []

        for line in output.splitlines():

            if not line:
                continue

            changes.append(
                Change(
                    status=line[:2].strip(),
                    path=line[3:].strip(),
                )
            )

        return changes

    def get_solution_changes(self) -> list[Change]:
        """Return only LeetCode solution file changes."""

        return [
            change
            for change in self.get_changes()
            if change.path.startswith("solutions/")
        ]