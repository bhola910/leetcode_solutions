"""
file_watcher.py

Monitors the solutions directory for file changes.
"""
import threading
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from leetcode_automation.managers.config_manager import ConfigManager
from leetcode_automation.utils.logger import Logger


class SolutionEventHandler(FileSystemEventHandler):
    """Handles file system events."""

    def __init__(
        self,
        extensions: list[str],
        debounce_seconds: int,
        callback,
    ) -> None:
        """Initialize the event handler."""

        super().__init__()

        self._logger = Logger()
        self._extensions = tuple(extensions)
        self._debounce = debounce_seconds
        self._timer = None
        self._callback = callback

    def _process_file(self, path: str) -> None:
        """Process the detected solution."""

        self._logger.info(
            f"Processing solution: {path}"
        )
        self._callback(path)

    def on_created(self, event) -> None:
        """Called when a new file is created."""

        if event.is_directory:
            return

        if not event.src_path.endswith(self._extensions):
            return

        self._logger.info(
            f"Detected: {event.src_path}"
        )

        if self._timer is not None:
            self._timer.cancel()

        self._timer = threading.Timer(
            self._debounce,
            self._process_file,
            args=[event.src_path],
        )

        self._timer.start()


class FileWatcher:
    """Watches the solutions directory."""

    def __init__(self, callback) -> None:
        """Initialize the file watcher."""

        self._logger = Logger()
        self._callback = callback
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

        event_handler = SolutionEventHandler(
            self._extensions,
            self._debounce,
            self._callback,
        )

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