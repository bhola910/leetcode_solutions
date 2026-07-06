"""
file_watcher.py

Monitors the solutions directory for file changes.
"""

import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from leetcode_automation.managers.config_manager import ConfigManager
from leetcode_automation.utils.logger import Logger


class SolutionEventHandler(FileSystemEventHandler):
    """Handles file system events."""

    def __init__(self):
        self._logger = Logger()

    def on_created(self, event):
        """Called when a new file is created."""

        if event.is_directory:
            return

        self._logger.info(
            f"New file detected: {event.src_path}"
        )

class FileWatcher:
    """Watches the solutions directory."""

    def __init__(self) -> None:
        """Initialize the file watcher."""

        self._logger = Logger()

        self._config = ConfigManager()

        self._watch_directory = self._config.get(
            "watcher.directory"
        )

        self._extensions = self._config.get(
            "watcher.extensions"
        )

        self._debounce = self._config.get(
            "watcher.debounce_seconds"
        )
    def start(self) -> None:
        """Start watching the solutions directory."""

        event_handler = SolutionEventHandler()

        observer = Observer()

        observer.schedule(
            event_handler,
            self._watch_directory,
            recursive=True,
        )

        observer.start()

        self._logger.info(
            f"Watching '{self._watch_directory}'..."
        )

        try:
            while True:
                time.sleep(1)

        except KeyboardInterrupt:
            observer.stop()

        observer.join()