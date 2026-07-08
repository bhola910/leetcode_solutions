from leetcode_automation.services.solution_parser import (
    SolutionParser,
)


def main():
    parser = SolutionParser()

    solution = parser.parse(
        "solutions/0001_two_sum.cpp"
    )

    print(solution)


if __name__ == "__main__":
    main()