from leetcode_automation.services.readme_manager import (
    ReadmeManager,
)


def main():
    manager = ReadmeManager()

    manager.update()

    print("README updated successfully.")


if __name__ == "__main__":
    main()