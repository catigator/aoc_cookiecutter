from utils.decorators import time_it


INPUT_FILENAME = "aoc/day_{{day}}/INPUT.txt"
EXAMPLE_FILENAME = "aoc/day_{{day}}/EXAMPLE_01.txt"


@time_it
def solve_part_1():
    print("Day {{day}} - Part 1")


@time_it
def solve_part_2():
    print("Day {{day}} - Part 2")


if __name__ == "__main__":
    solve_part_1()
    # solve_part_2()
