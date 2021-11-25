from os import mkdir
from os.path import basename, abspath, join, exists
from jinja2 import Template
import click
import os
from pathlib import Path


PROJECT_NAME = "NEW_PROJECT"
BASE_PATH = PROJECT_NAME
YEAR = 2020


UP_PATH = os.path.join(os.path.dirname(__file__), '..')
CREATE_PATH = os.path.join(UP_PATH, PROJECT_NAME)


def set_variables(name):
    global PROJECT_NAME, CREATE_PATH
    PROJECT_NAME = name
    CREATE_PATH = os.path.join(UP_PATH, PROJECT_NAME)


def create_empty_file(filepath: str):
    with open(filepath, "w+"):
        return


def generate_directory():
    Path(CREATE_PATH).mkdir(parents=True, exist_ok=True)
    print("Created path at " + str(Path(CREATE_PATH)))


# def generate_solution_files():
#     for i in range(1, 26):
#         answers_path = abspath(f'./advent_of_Code/data/answers')
#         day_path = join(answers_path, f"day_{i}")
#         if not exists(day_path):
#             mkdir(day_path)
#         create_empty_file(join(answers_path, f"day_{i}", "part_1.txt"))
#         create_empty_file(join(answers_path, f"day_{i}", "part_2.txt"))


def generate_input_files():
    for i in range(1, 26):
        create_empty_file(abspath(f'./advent_of_Code/data/input/day_{i}'))


def generate_test_files():
    for i in range(1, 26):
        with open(abspath(f"./templates/test.tmpl")) as f:
            template = Template(f.read())
        with open(abspath(f"./advent_of_Code/challenges/tests/test_day_{i}.py"), "w+") as f:
            f.write(template.render(day=i))


def generate_challenge_files():
    template = None
    with open(abspath("./template/aoc/day_{{day}}/__main__.py")) as f:
        template = Template(f.read())

    challenge_directory = os.path.join(CREATE_PATH, "aoc")
    Path(challenge_directory).mkdir(parents=True, exist_ok=True)

    for i in range(1, 26):
        file_location = os.path.join(challenge_directory, f"day_{i}.py")
        with open(file_location, "w+") as f:
            f.write(template.render(day=i))


@click.command()
@click.option('--name', '-n', default="NEW_PROJECT", help='Project Name')
def generate_all(name):
    set_variables(name)
    generate_directory()
    # generate_solution_files()
    # generate_input_files()
    # generate_test_files()
    generate_challenge_files()


if __name__ == "__main__":
    generate_all()