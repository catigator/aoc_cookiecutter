from os import mkdir, listdir
from os.path import basename, abspath, join, exists, isfile
from jinja2 import Template
import click
import os
from pathlib import Path
from shutil import copy2

from template.utils.downloader.__main__ import leading_zero

PROJECT_NAME = "NEW_PROJECT"
BASE_PATH = PROJECT_NAME
YEAR = 2021
DAYS = 25


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


def copy_file(f, di, day, extra_path):
    # f: "file.txt"
    # di: "c:/jakob/"
    f_new = f.replace("{{day}}", leading_zero(day))
    di_new = di.replace("{{day}}", leading_zero(day))
    extra_path_new = extra_path.replace("{{day}}", leading_zero(day))

    file_path = join(di, f)  # c:/jakob/file.txt
    new_path = join(CREATE_PATH, extra_path_new)  # c:/NEW_PROJECT/day_01/
    new_path_full = join(new_path, f_new)  # c:/NEW_PROJECT/day_01/file.txt

    os.makedirs(new_path, exist_ok=True)

    if ".py" in f or ".yml" in f or ".md" in f:
        with open(file_path) as tf:
            print(file_path)
            template = Template(tf.read())
        with open(new_path_full, "w+") as pf:
            pf.write(template.render({"day": leading_zero(day), "year":YEAR}))
    else:
        copy2(file_path, new_path_full)


def travers_dir(di, day=1, extra_path=""):
    print(f"Traversing {di}, extra_path = {extra_path}")
    all_stuff = listdir(di)
    files = [f for f in all_stuff if isfile(join(di, f))]
    dirs = [f for f in all_stuff if f not in files]
    dirs = [d for d in dirs if "." not in d]
    dirs_abs = [join(di, d) for d in dirs]

    print(files)  # ['__init__.py']
    print(dirs)  # ['day_{{day}}']

    for f in files:
        if ".py" in f and ".pyc" not in f\
                or ".md" in f or ".yml" in f or ".gitignore" in f:
            copy_file(f, di, day, extra_path)

    for d in dirs:
        # join(di, d) = absolut_path
        # d = additional extra path
        if "__pycache__" not in d:
            if "{{day}}" in d:
                for i in range(DAYS):
                    new_d = d.replace("{{day}}", leading_zero(i + 1))
                    travers_dir(join(di, d), i+1, join(extra_path, new_d))
            else:
                travers_dir(join(di, d), day, join(extra_path, d))


@click.command()
@click.option('--name', '-n', default="NEW_PROJECT", help='Project Name')
def generate_all(name):
    set_variables(name)
    generate_directory()
    template_path = join(os.path.dirname(__file__), "template")
    print(f"template_path: {template_path}")
    travers_dir(template_path, 1, "")


if __name__ == "__main__":

    generate_all()
