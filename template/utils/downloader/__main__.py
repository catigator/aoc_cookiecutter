import click
import requests
import browser_cookie3
from bs4 import BeautifulSoup

YEAR = "2020"


def save_to_file(text, filename):
    with open(filename, "w") as f:
        f.write(text)


def leading_zero(number):
    return "{:02d}".format(number)


def download_puzzle():
    day = 1
    input_url = f"https://adventofcode.com/2020/day/{day}"
    cookies = browser_cookie3.chrome(domain_name='adventofcode.com')
    r = requests.get(input_url, cookies=cookies)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, 'html.parser')
    puzzle = soup.find(class_="day-desc").text
    save_to_file(puzzle, f"aoc/day_{leading_zero(day)}/PUZZLE.md")
    return puzzle


def download_examples():
    day = 1
    input_url = f"https://adventofcode.com/2020/day/{day}"
    cookies = browser_cookie3.chrome(domain_name='adventofcode.com')
    r = requests.get(input_url, cookies=cookies)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, 'html.parser')
    examples = soup.find_all("pre")
    for i, example in enumerate(examples):
        save_to_file(example.text, f"aoc/day_{leading_zero(day)}/EXAMPLE_{leading_zero(i+1)}.md")
    return examples


def download_input():
    day = 1
    input_url = f"https://adventofcode.com/2020/day/{day}/input"
    cookies = browser_cookie3.chrome(domain_name='adventofcode.com')
    r = requests.get(input_url, cookies=cookies)
    r.raise_for_status()
    # print(r.text)
    save_to_file(r.text, f"aoc/day_{leading_zero(day)}/INPUT.md")
    return r.text


if __name__ == "__main__":
    download_input()
    download_puzzle()
    download_examples()
