import os
import re

import openai
import requests
from bs4 import BeautifulSoup
from openai.error import RateLimitError
from retry import retry

openai.api_key = os.getenv("OPENAI_API_KEY")

GPT_CHAT_MODELS = ["gpt-3.5-turbo"]
GPT_MODELS = ["text-davinci-002", "text-davinci-003"]

Answer = tuple[str, float, str]


def get_problem(problem_number: int) -> str:
    url = f"https://projecteuler.net/minimal={problem_number}"
    response = requests.get(url)
    response.raise_for_status()
    if response.status_code == 200:
        return response.text
    return ''


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


@retry(exceptions=RateLimitError, tries=2, delay=60)
def openai_request(prompt: str, gpt_model: str, temperature: float) -> str:
    if gpt_model in GPT_CHAT_MODELS:
        response = openai.ChatCompletion.create(
            model=gpt_model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
        )
        return re.search(r"\d+", response.choices[0].message.content).group(0).strip()

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


def solve_problem(number: int, temperature: float) -> tuple[str, str, bool, list[Answer]]:
    prompt = "For the following problem, return only the solution as a number without any other text:\n\n"
    prompt += parse_problem(get_problem(number))

    status = False
    answers: list[Answer] = []

    for gpt_model in [*GPT_CHAT_MODELS, *GPT_MODELS]:
        solution = openai_request(prompt, gpt_model, temperature).strip()
        if solution not in list(map(lambda answer: answer[2], answers)):
            status = submit_response(number, solution)

        answers.append((gpt_model, temperature, solution))
        if status:
            break

    if not status:
        solution = "?"

    return prompt, solution, status, answers
