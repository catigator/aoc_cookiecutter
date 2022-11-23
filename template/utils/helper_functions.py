

def read_input(filename: str) -> str:

    with open(filename) as f:
        input_str = f.read()

    return input_str


def read_input_lines(filename: str, strip_whitespace=False) -> list:
    lines_list = []

    with open(filename) as f:
        lines_list = f.readlines()

    if strip_whitespace:
        lines_list = [line.strip() for line in lines_list]

    return lines_list


def read_input_int(filename: str) -> list:
    lines_list = read_input_lines(filename)

    numbers = [int(line) for line in lines_list]

    return numbers


def read_input_int_individuals(filename: str) -> list:
    input_line = read_input(filename)

    numbers = [int(number) for number in input_line.split(",")]

    return numbers


def read_input_int_matrix(filename: str) -> list:
    lines = read_input_lines(filename, strip_whitespace=True)
    matrix = []

    for line in lines:
        matrix.append([int(number) for number in line])

    return matrix
