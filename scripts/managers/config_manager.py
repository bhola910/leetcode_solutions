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