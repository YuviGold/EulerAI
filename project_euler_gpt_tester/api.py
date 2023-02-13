import os
import re

import openai
import requests
from bs4 import BeautifulSoup

openai.api_key = os.getenv("OPENAI_API_KEY")

GPT_MODELS = ["text-davinci-002", "text-davinci-003"]


def get_problem(problem_number: int) -> str | None:
    url = f"https://projecteuler.net/minimal={problem_number}"
    response = requests.get(url)
    response.raise_for_status()
    if response.status_code == 200:
        return response.text
    return None


def parse_problem(problem_text: str) -> str:
    t = problem_text

    # replace x<x>th\st\nd\rd</x> with xth\st\nd\rd
    t = re.sub(r"<\w+>(th|st|nd|rd)</\w+>", r"\1", t)

    # replace <sup> and <sub> with ^ and _
    t = t.replace("<sup>", "^").replace("</sup>", "")
    t = t.replace("<sub>", "_").replace("</sub>", "")

    t = t.replace("$", "")  # dollar signs used for math
    t = t.replace("\\lt", "<")
    t = t.replace("\\gt", ">")
    t = t.replace("\\le", "≤")
    t = t.replace("\\ge", "≥")
    t = t.replace("\\ne", "≠")
    t = t.replace("\\pm", "±")

    # add newlines
    t = t.replace("<p>", "").replace("</p>", "\n")
    t = t.replace("<blockquote>", "").replace("</blockquote>", "\n")

    # remove all other tags
    soup = BeautifulSoup(t, "html.parser")
    return soup.text.strip()


def openai_request(prompt: str, gpt_model: str, temperature: float) -> str:
    response = openai.Completion.create(
        model=gpt_model,
        prompt=prompt,
        temperature=temperature,
    )
    return re.search(r"\d+", response.choices[0].text).group(0).strip()


def submit_response(problem_number: int, solution: str) -> bool:
    url = f"https://euler.haku.dev/api?q={problem_number}&a={solution}"
    response = requests.post(url)
    response.raise_for_status()

    return response.text == "1"


def solve_problem(number: int, temperature: float) -> tuple[str, str, bool]:
    prompt = "For the following problem, return only the solution as a number without any other text:\n\n"
    prompt += parse_problem(get_problem(number))

    for gpt_model in GPT_MODELS:
        solution = openai_request(prompt, gpt_model, temperature).strip()
        status = submit_response(number, solution)
        if status:
            break

    return prompt, solution, status
