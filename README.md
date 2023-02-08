# Project Euler GPT-3 Tester

Well, just following this question [Twitter Question](https://twitter.com/Arbel2025/status/1622223633853603841)
Can ChatGPT answer [Project Euler](https://projecteuler.net/) questions?

This is a Python script, scraping Project Euler questions, and send them to [OpenAI GPT-3](https://platform.openai.com/docs/models/gpt-3) model.
Then, submitting the answers to [euler.haku.dev](https://euler.haku.dev/) that returns whether those answers were correct or not.


What do you say?
Would ChatGPT answer all the questions correct?

## Setup

This project is running with Python and [Poetry](https://python-poetry.org/docs/#installation)


1. Initialize environment
    ```shell
    poetry install
    ```

2. Signup to OpenAI, and retrieve an [API token](https://platform.openai.com/docs/quickstart/build-your-application)
    ```shell
    export OPENAI_API_KEY=<API_TOKEN>
    ```

## How to use?
1. Run the follwing command
    ```shell
    poetry run ./main.py --problem 1 --amount 20
    ```
    This will run the script for problems 1 to 20, and output the results in a table as below.

```bash
$ poetry run ./main.py --problem 1 --amount 20

           Project Euler           
┏━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Problem ┃ Solution     ┃ Status ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━┩
│ 1       │ 233168       │ ✅     │
│ 2       │ 4613732      │ ✅     │
│ 3       │ 6857         │ ✅     │
│ 4       │ 906609       │ ✅     │
│ 5       │ 232792560    │ ✅     │
│ 6       │ 25164150     │ ✅     │
│ 7       │ 104743       │ ✅     │
│ 8       │ 23514624000  │ ✅     │
│ 9       │ 31875000     │ ✅     │
│ 10      │ 142913828922 │ ✅     │
│ 11      │ 73812150     │ ❌     │
│ 12      │ 76576500     │ ✅     │
│ 13      │ 5537376230   │ ✅     │
│ 14      │ 837799       │ ✅     │
│ 15      │ 137846528820 │ ✅     │
│ 16      │ 1366         │ ✅     │
│ 17      │ 21124        │ ✅     │
│ 18      │ 1074         │ ✅     │
│ 19      │ 171          │ ✅     │
│ 20      │ 648          │ ✅     │
└─────────┴──────────────┴────────┘
```

## All options
```--problem <number>``` - Problem number to start from.

```--amount <number>``` - Amount of problems to loop through.

```--output <table(default)|json|pretty-json>``` - Output format.

```--temperature <number from 0.0 to 1.0>``` - Creativity temperature for the model. 0 is low 1 is high.

```--max_tries <number>``` - Number of attempts to slove the problems.

## Example output in pretty-json
```bash
$ poetry run ./main.py --problem 27 --output pretty-json

[
  {
    "problem": "27",
    "prompt": "For the following problem, return only the solution as a number without any other text:\n\nEuler discovered the remarkable quadratic formula:\n\nn^2 + n + 41\n\nIt turns out that the formula will produce 40 primes for the consecutive integer values 0 ≤ n ≤ 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.\n\nThe incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 ≤ n ≤ 79. The product of the coefficients, −79 and 1601, is −126479.\n\nConsidering quadratics of the form:\n\n\nn^2 + an + b, where |a| < 1000 and |b| ≤ 1000where |n| is the modulus/absolute value of ne.g. |11| = 11 and |-4| = 4\n\n\nFind the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.",
    "solution": "59231",
    "status": false,
    "tries": 1
  }
]
```

## Contributing

Some of the problems might not get parsed correctly and chatGPT will not be happy with the input.
If you find any problem, please open an issue, or even better, a PR.

### Run GHA

I use [nektos/act](https://github.com/nektos/act) tool to run the Git Hub Action locally.
By default, act runs on a slim container image, for docker-compose usage the base image is replaced.

```bash
act --platform=ubuntu-latest=lucasalt/act_base:latest -j <JOB>
```