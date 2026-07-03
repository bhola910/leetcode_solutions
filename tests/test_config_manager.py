from leetcode_automation.managers.config_manager import ConfigManager

config = ConfigManager()

print(config.get("project.name"))
print(config.get("repository.branch"))
print(config.get("watcher.directory"))
print(config.get("logging.level"))