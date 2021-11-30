ADVENT OF CODE {{year}}

# Installation

1. Install conda
2. Create conda environment with `conda create --name aoc_{{year}} python=3.9`
3. Install conda environment with `conda env update`
4. Activate conda environment with `conda activate aoc_{{year}}`
5. Install `browser-cookie3` with `pip install browser-cookie3`

# Testing

Run with e.g. `python -m pytest` or `pytest aoc/day_01`

# Download

Download the input, puzzle description and examples for a specific day with:

```commandline
python -m utils.downloader <day: int>
```

and they will be downloaded to `aoc/day_{day}/` as `INPUT.md`, `PUZZLE.md` and `EXAMPLE_X.md`.

# Instructions


Run with e.g. `python -m aoc.day_04` from root folder after activating the conda environment