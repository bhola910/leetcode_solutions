from leetcode_automation.models.change import Change
from leetcode_automation.services.commit_message_generator import (
    CommitMessageGenerator,
)


def main():
    generator = CommitMessageGenerator()

    changes = [
        Change(
            status="??",
            path="solutions/two_sum.cpp",
        ),
        Change(
            status="M",
            path="solutions/binary_search.py",
        ),
        Change(
            status="D",
            path="solutions/merge_intervals.java",
        ),
    ]

    for change in changes:
        print(
            generator.generate(change)
        )


if __name__ == "__main__":
    main()