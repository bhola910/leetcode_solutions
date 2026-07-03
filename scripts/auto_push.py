import subprocess
import time
from pathlib import Path

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

REPO = Path(r"C:\Users\bhola\Developer\cplusplus\leetcode_solutions")

last_push = 0


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        global last_push

        if event.is_directory:
            return

        if not event.src_path.endswith(".cpp"):
            return

        if ".git" in event.src_path:
            return

        now = time.time()

        # prevent multiple pushes caused by one save
        if now - last_push < 5:
            return

        last_push = now

        print(f"\nDetected change: {event.src_path}")

        time.sleep(2)

        subprocess.run(["git", "add", "."], cwd=REPO)

        commit = subprocess.run(
            ["git", "commit", "-m", "Update LeetCode Solution"],
            cwd=REPO,
            capture_output=True,
            text=True,
        )

        if "nothing to commit" in commit.stdout.lower():
            print("Nothing to commit.")
            return

        print("Pushing to GitHub...")

        subprocess.run(["git", "push"], cwd=REPO)

        print("Done!")


observer = Observer()
observer.schedule(Handler(), str(REPO), recursive=True)
observer.start()

print("Watching your LeetCode repository...")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()