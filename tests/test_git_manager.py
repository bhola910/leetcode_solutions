from leetcode_automation.managers.git_manager import (
    GitManager,
)


def main():
    git = GitManager()

    print("Current Branch:")
    print(git.current_branch())

    print()

    print("Repository Clean:")
    print(git.repository_clean())

    print()

    print("Repository Exists:")
    print(git.repository_exists())

    print()

    print("Has Remote:")
    print(git.has_remote())

    print()

    print("Branch 'main' Exists:")
    print(git.branch_exists("main"))


if __name__ == "__main__":
    main()