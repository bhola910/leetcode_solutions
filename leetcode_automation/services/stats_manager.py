"""
stats_manager.py

Maintains solution statistics.
"""

import json
from pathlib import Path

from leetcode_automation.services.solution_parser import (
    SolutionParser,
)


class StatsManager:
    """Manages repository statistics."""

    def __init__(self) -> None:
        """Initialize the stats manager."""

        self._stats_file = Path(
            "leetcode_automation/data/stats.json"
        )

        self._solutions_directory = Path(
            "solutions"
        )

        self._parser = SolutionParser()

    def load(self) -> dict:
        """Load statistics."""

        with self._stats_file.open(
            "r",
            encoding="utf-8",
        ) as file:
            return json.load(file)

    def save(self, stats: dict) -> None:
        """Save statistics."""

        with self._stats_file.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                stats,
                file,
                indent=4,
            )

    def generate(self) -> dict:
        """Generate repository statistics."""

        stats = {
            "total_solutions": 0,
            "cpp": 0,
            "python": 0,
            "java": 0,
            "latest_problem": "",
        }

        latest_solution = None

        for file in sorted(
            self._solutions_directory.iterdir()
        ):

            if not file.is_file():
                continue

            try:
                solution = self._parser.parse(
                    str(file)
                )

            except ValueError:
                continue

            stats["total_solutions"] += 1

            language = solution.language.lower()

            if language == "c++":
                language = "cpp"

            stats[language] += 1

            latest_solution = solution

        if latest_solution:

            stats["latest_problem"] = (
                latest_solution.title
            )

        self.save(stats)

        return stats