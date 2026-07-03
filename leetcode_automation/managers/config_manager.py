"""
config_manager.py

Handles loading and accessing the application's configuration.
"""

import json
from pathlib import Path


class ConfigManager:
    """Loads and provides access to configuration settings."""

    def __init__(self) -> None:
        """Initialize the configuration manager."""

        self._config_path = Path("config/config.json")
        self._config = {}

        self.load()
        self.validate()

    def load(self) -> None:
        """Load configuration from the JSON file."""

        try:
            with self._config_path.open("r", encoding="utf-8") as file:
                self._config = json.load(file)

        except FileNotFoundError:
            print("Configuration file not found.")

        except json.JSONDecodeError:
            print("Configuration file contains invalid JSON.")

        except Exception as error:
            print(f"Unexpected error: {error}")

    def validate(self) -> None:
        """Validate required configuration sections."""

        required_sections = [
            "project",
            "repository",
            "watcher",
            "logging",
        ]

        for section in required_sections:
            if section not in self._config:
                raise KeyError(
                    f"Missing required configuration section: '{section}'"
                )
            
    def get(self, key: str):
        """Return a configuration value using dot notation."""

        current = self._config
        parts = key.split(".")

        for part in parts:
            current = current[part]

        return current