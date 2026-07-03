"""
logger.py

Provides logging functionality for the application.
"""

from email.mime import message
import logging
from pathlib import Path


class Logger:
    """Application logger."""

    def __init__(self) -> None:
        """Initialize the logger."""

        log_directory = Path("logs")
        log_directory.mkdir(exist_ok=True)

        log_file = log_directory / "automation.log"

        self._logger = logging.getLogger("LAE")
        self._logger.setLevel(logging.INFO)

        if self._logger.hasHandlers():
            self._logger.handlers.clear()

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(message)s",
            "%Y-%m-%d %H:%M:%S",
        )

        file_handler = logging.FileHandler(
            log_file,
            encoding="utf-8",
        )

        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()

        console_handler.setFormatter(formatter)

        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)

    def info(self, message: str) -> None:
        """Log an informational message."""

        self._logger.info(message)
    
    def warning(self, message: str) -> None:
        """Log a warning message."""

        self._logger.warning(message)

    def error(self, message: str) -> None:
        """Log an error message."""

        self._logger.error(message)

    def debug(self, message: str) -> None:
        """Log a debug message."""

        self._logger.debug(message)
