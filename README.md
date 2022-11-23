# Advent of Code Cookiecutter template

This creates a template structure for writing your Advent of Code for the year. It includes:

* Easy way to run specific days
* Easy way to add tests
* A decorator to time your solutions (did you _really_ solve a day if your solution takes more than 10 milliseconds to run??)
* A CLI to download the input, puzzle description and examples for a specific day to local files
* Some helper functions to read files in different formats etc.

# Installation

1. Install conda
2. Create conda environment with `conda create --name aoc_cookiecutter python=3.11 --channel conda-forge`
3. Install conda environment with `conda env update`
4. Activate conda environment with `conda activate aoc_cookiecutter`

# How to run

run:

```commandline
python generate.py -n <project_name: str> -y <year: int>
```

e.g.

```commandline
python generate.py -n advent_of_code_2022 -y 2022
```

This will generate a project one folder up from this directory with the specified project name.

# Notes on project structure

* General information on how to install, run and test the project can be found in the `README.md` in the root directory
  of the created project

* Initially I set up fancy logging for this, but it was generally much slower than printing and messed up the execution
time calculation fairly easily