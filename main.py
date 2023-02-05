#!/usr/bin/env python

import os
import re

import openai
import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
from typer import Typer

console = Console()
openai.api_key = os.getenv("OPENAI_API_KEY")

GPT_MODELS = ["text-davinci-002", "text-davinci-003"]
TEMPERATURE = 0.0


def get_problem(problem_number: int):
    url = f"https://projecteuler.net/minimal={problem_number}"
    response = requests.get(url)
    response.raise_for_status()
    if response.status_code == 200:
        return response.text
    return None


def parse_problem(problem_text: str) -> str:
    t = problem_text

    # replace <sup> and <sub> with ^ and _
    t = problem_text.replace("<sup>", "^").replace("</sup>", "")
    t.replace("<sub>", "_").replace("</sub>", "")

    t = t.replace("$", "")  # dollar signs used for math

    t = t.replace("\lt", "<")
    t = t.replace("\gt", ">")
    t = t.replace("\le", "≤")
    t = t.replace("\ge", "≥")
    t = t.replace("\\ne", "≠")
    t = t.replace("\pm", "±")

    # add newlines
    t = t.replace("<p>", "").replace("</p>", "\n").replace("<br />", "\n")

    # remove all other tags
    soup = BeautifulSoup(t, "html.parser")
    return soup.text.strip()


def pretty_bool(condition: bool) -> str:
    return ":white_check_mark:" if condition else ":cross_mark:"


def openai_request(prompt: str, gpt_model: str):
    response = openai.Completion.create(
        model=gpt_model,
        prompt=prompt,
        temperature=TEMPERATURE,
    )
    return re.search(r"\d+", response.choices[0].text).group(0).strip()


def submit_response(problem_number: int, solution: str):
    url = f"https://euler.haku.dev/api?q={problem_number}&a={solution}"
    response = requests.post(url)
    response.raise_for_status()

    return response.text == "1"


def solve_problem(number: int) -> tuple[str, str, bool]:
    problem_text = get_problem(number)
    prompt = f"For the following problem, return only the solution as a number without any other text:\n\n{problem_text}"

    for gpt_model in GPT_MODELS:
        solution = openai_request(prompt, gpt_model).strip()
        status = submit_response(number, solution)
        if status:
            break

    return prompt, solution, status


app = Typer()


@app.command()
def run(problem: int = 1, amount: int = 1, verbose: bool = False):
    table = Table(*("Problem", "Solution", "Status"), title="Project Euler")

    if verbose:
        table.add_column("Prompt")

    for problem_number in range(problem, problem + amount):
        prompt, solution, status = solve_problem(problem_number)

        if not verbose:
            table.add_row(str(problem_number), solution, pretty_bool(status))
        else:
            table.add_row(str(problem_number), solution, pretty_bool(status), prompt)

    console.print(table)


def main():
    app()


if __name__ == "__main__":
    main()
