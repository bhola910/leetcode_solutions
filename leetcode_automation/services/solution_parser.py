"""
solution_parser.py

Parses solution filenames.
"""

from pathlib import Path

from leetcode_automation.models.solution import Solution


class SolutionParser:
    """Parses solution files."""

    def parse(self, path: str) -> Solution:
        """Parse a solution path."""

        file = Path(path)

        file_name = file.stem
        extension = file.suffix

        parts = file_name.split("_", maxsplit=1)

        if len(parts) != 2:
            raise ValueError(
                "Invalid filename. Expected format: "
                "'0001_two_sum.cpp'"
            )

        try:
            number = int(parts[0])
        except ValueError as error:
            raise ValueError(
                "Problem number must be numeric."
            ) from error

        title = parts[1].replace("_", " ").title()

        languages = {
            ".cpp": "C++",
            ".py": "Python",
            ".java": "Java",
        }

        language = languages.get(extension)

        if language is None:
            raise ValueError(
                f"Unsupported file extension: {extension}"
            )

        return Solution(
            number=number,
            title=title,
            language=language,
            path=path,
        )