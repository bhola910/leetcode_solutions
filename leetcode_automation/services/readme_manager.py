"""
readme_manager.py

Updates the repository README.
"""

from pathlib import Path

from leetcode_automation.services.stats_manager import (
    StatsManager,
)


class ReadmeManager:
    """Updates README.md."""

    def __init__(self) -> None:
        """Initialize the README manager."""

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

    def update(self) -> None:
        """Update README."""

        stats = self._stats.generate()

        content = self._build_content(stats)

        self._readme.write_text(
            content,
            encoding="utf-8",
        )