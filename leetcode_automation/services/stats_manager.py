"""
stats_manager.py

Maintains solution statistics.
"""

import json
from pathlib import Path

from leetcode_automation.services.solution_parser import (
    SolutionParser,
)
from leetcode_automation.utils.logger import Logger


class StatsManager:
    """Manages repository statistics."""

    def __init__(self) -> None:
        """Initialize the stats manager."""

        self._logger = Logger()

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

    def _empty_stats(self) -> dict:
        """Return an empty statistics dictionary."""

        return {
            "total_solutions": 0,
            "cpp": 0,
            "python": 0,
            "java": 0,
            "latest_problem": "",
        }

    def _language_key(
        self,
        language: str,
    ) -> str:
        """Normalize language names."""

        language = language.lower()

        if language == "c++":
            return "cpp"

        return language

    def _update_stats(
        self,
        stats: dict,
        solution,
    ) -> None:
        """Update statistics for one solution."""

        stats["total_solutions"] += 1

        language = self._language_key(
            solution.language
        )

        if language in stats:
            stats[language] += 1

    def generate(self) -> dict:
        """Generate repository statistics."""

        stats = self._empty_stats()

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

            except ValueError as error:

                self._logger.warning(
                    str(error)
                )

                continue

            self._update_stats(
                stats,
                solution,
            )

            latest_solution = solution

        if latest_solution:

            stats["latest_problem"] = (
                latest_solution.title
            )

        self.save(stats)

        self._logger.info(
            "Statistics updated successfully."
        )

        return stats