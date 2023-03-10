from enum import Enum
from json import dumps
from typing import Any, Optional

from rich.console import Console
from rich.table import Table
from typer import Typer, Option

from .api import solve_problem

console = Console()


def pretty_bool(condition: bool) -> str:
    return ":white_check_mark:" if condition else ":cross_mark:"


def print_table(problems: list[dict[str, Any]]):
    table = Table(*("Problem", "Solution", "Status", "Answers"), title="Project Euler")

    for problem in problems:
        table.add_row(
            problem["problem"],
            problem["solution"],
            pretty_bool(problem["status"]),
            str(problem["answers"])
        )

    console.print(table)


def get_temperature(temperature: float | None, tries: int, max_tries: int) -> float:
    if temperature is not None:
        return temperature

    # avoid devision by zero
    if max_tries == 1 or tries == 0:
        return 0

    # gradually increase temperature as we try more
    return tries / (max_tries - 1)


app = Typer()


class OutputType(str, Enum):
    TABLE = "table"
    JSON = "json"
    PRETTY_JSON = "pretty-json"


@app.command()
def run(
    problem: int = Option(1, min=1),
    amount: int = Option(1, min=1),
    output: OutputType = OutputType.TABLE,
    max_tries: int = Option(1, min=1),
    temperature: Optional[float] = Option(None, min=0, max=1),
):
    problems = []

    for problem_number in range(problem, problem + amount):
        tries = 0
        status = False
        answers = []
        while not status and tries < max_tries:
            prompt, solution, status, try_answers = solve_problem(
                problem_number, get_temperature(temperature, tries, max_tries)
            )
            answers += try_answers
            tries += 1

        problems.append(
            {
                "problem": str(problem_number),
                "prompt": prompt,
                "solution": solution,
                "answers": answers,
                "status": status,
                "tries": tries,
            }
        )

    if output == OutputType.TABLE:
        print_table(problems)
    elif output == OutputType.JSON:
        print(dumps(problems))
    elif output == OutputType.PRETTY_JSON:
        indent = 4
        nest_level = 3
        print(dumps(problems, indent=indent).replace("\\n", f"\n{' ' * indent * nest_level}"))


def main():
    app()
