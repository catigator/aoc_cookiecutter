

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

