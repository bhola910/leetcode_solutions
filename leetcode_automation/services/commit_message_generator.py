"""
commit_message_generator.py

Generates Git commit messages.
"""

from pathlib import Path

from leetcode_automation.models.change import Change


class CommitMessageGenerator:
    """Generates commit messages."""

    def generate(self, change: Change) -> str:
        """Generate a commit message."""

        solution_name = (
            Path(change.path)
            .stem
            .replace("_", " ")
            .title()
        )

        if change.status == "??":
            action = "add"

        elif change.status == "M":
            action = "update"

        elif change.status == "D":
            action = "remove"

        else:
            action = "update"

        return (
            f"feat(leetcode): "
            f"{action} {solution_name} solution"
        )