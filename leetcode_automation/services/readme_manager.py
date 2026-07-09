"""
readme_manager.py

Updates the repository README.
"""

from pathlib import Path

from leetcode_automation.services.stats_manager import (
    StatsManager,
)
from leetcode_automation.utils.logger import Logger


class ReadmeManager:
    """Updates the repository README."""

    def __init__(self) -> None:
        """Initialize the README manager."""

        self._logger = Logger()

        self._stats = StatsManager()

        self._readme = Path("README.md")

    def _build_content(
        self,
        stats: dict,
    ) -> str:
        """Build README content."""

        return f"""# LeetCode Solutions

## 📊 Statistics

- Total Solutions: {stats["total_solutions"]}
- C++: {stats["cpp"]}
- Python: {stats["python"]}
- Java: {stats["java"]}

## 🆕 Latest Solution

- {stats["latest_problem"]}
"""

    def _write(
        self,
        content: str,
    ) -> None:
        """Write content to README."""

        self._readme.write_text(
            content,
            encoding="utf-8",
        )

    def update(self) -> None:
        """Update the repository README."""

        stats = self._stats.generate()

        content = self._build_content(
            stats
        )

        self._write(content)

        self._logger.info(
            "README updated successfully."
        )