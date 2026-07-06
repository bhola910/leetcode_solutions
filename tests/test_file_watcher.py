from leetcode_automation.services.file_watcher import FileWatcher


def main():
    watcher = FileWatcher()

    watcher.start()


if __name__ == "__main__":
    main()