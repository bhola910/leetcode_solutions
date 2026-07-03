from leetcode_automation.managers.config_manager import ConfigManager


def main():
    config = ConfigManager()

    print(config.get("project.name"))
    print(config.get("repository.branch"))
    print(config.get("watcher.directory"))
    print(config.get("logging.level"))

    config.reload()

    print("Configuration reloaded successfully.")


if __name__ == "__main__":
    main()