from enum import Enum
from json import dumps
from typing import Any

from rich.console import Console
from rich.table import Table
from typer import Typer

from .api import solve_problem

console = Console()


def pretty_bool(condition: bool) -> str:
    return ":white_check_mark:" if condition else ":cross_mark:"


def print_table(problems: list[dict[str, Any]]):
    table = Table(*("Problem", "Solution", "Status"), title="Project Euler")

    for problem in problems:
        table.add_row(problem['problem'], problem['solution'], pretty_bool(problem['status']))

    console.print(table)


app = Typer()


class OutputType(str, Enum):
    TABLE = "table"
    JSON = "json"


@app.command()
def run(problem: int = 1, amount: int = 1, output: OutputType = OutputType.TABLE):
    problems = []

    for problem_number in range(problem, problem + amount):
        prompt, solution, status = solve_problem(problem_number)
        problems.append({
            'problem': str(problem_number),
            'prompt': prompt,
            'solution': solution,
            'status': status
        })

    if output == OutputType.TABLE:
        print_table(problems)
    else:
        print(dumps(problems))


def main():
    app()
