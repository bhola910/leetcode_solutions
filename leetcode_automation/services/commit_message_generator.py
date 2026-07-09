"""
commit_message_generator.py

Generates Git commit messages.
"""

from leetcode_automation.models.solution import (
    Solution,
)


class CommitMessageGenerator:
    """Generates commit messages."""

    def generate(
        self,
        solution: Solution,
    ) -> str:
        """Generate a commit message."""

        language = solution.language.lower()

        if language == "c++":
            language = "cpp"

        return (
            f"feat({language}): "
            f"solve {solution.title} "
            f"(#{solution.number})"
        )