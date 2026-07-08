from leetcode_automation.services.change_detector import ChangeDetector


def main():
    detector = ChangeDetector()

    changes = detector.get_changes()

    if not changes:
        print("No changes detected.")
        return

    print("Git Changes:")

    for change in changes:
        print(change.status, "->", change.path)


if __name__ == "__main__":
    main()