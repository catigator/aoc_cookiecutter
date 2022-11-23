from typing import List


def read_input(filename: str) -> str:
    """

    :param filename: Path of file from working directory (e.g. INPUT_FILENAME)
    :return: the contents of the file as a string
    """

    with open(filename) as f:
        input_str = f.read()

    return input_str


def read_input_lines(filename: str, strip_whitespace: bool=False) -> List[str]:
    """

    :param filename:
    :param strip_whitespace:
    :return: A list of all of the lines in file contents as strings

    Output examples:

    ["I am not stripped of my whitespace."]
    ["I", "am", "stripped", "of", "my", "whitespace."]
    """
    lines_list = []

    with open(filename) as f:
        lines_list = f.readlines()

    if strip_whitespace:
        lines_list = [line.strip() for line in lines_list]

    return lines_list


def read_input_int(filename: str) -> List[int]:
    """

    :param filename: Path of file from working directory
    :return: Each line in file converted to an int and added to a list

    Input example:

    123
    456
    789

    Output example:

    [123, 456, 789]

    """
    lines_list = read_input_lines(filename)

    numbers = [int(line) for line in lines_list]

    return numbers


def read_input_int_individuals(filename: str) -> list:
    """
    Reads a file and returns all numbers in file as separated by commas

    :param filename: Path of file from working directory
    :return: List of all numbers in file

    Input example:

    123,456,789

    Output example:

    [123, 456, 789]
    """
    input_line = read_input(filename)

    numbers = [int(number) for number in input_line.split(",")]

    return numbers


def read_input_int_matrix(filename: str) -> List[List[int]]:
    """
    Reads a file and returns all numbers in file as if it was a matrix

    :param filename:
    :return: "Matrix" (List[List[int]]) of input

    Input example:

    123
    456
    789

    Output example:

    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    """
    lines = read_input_lines(filename, strip_whitespace=True)
    matrix = []

    for line in lines:
        matrix.append([int(number) for number in line])

    return matrix
