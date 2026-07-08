from leetcode_automation.services.stats_manager import (
    StatsManager,
)


def main():
    manager = StatsManager()

    stats = manager.generate()

    print(stats)


if __name__ == "__main__":
    main()