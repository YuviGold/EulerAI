# Project Euler GPT-3 Tester

Well, just following this question [Twitter Question](https://twitter.com/Arbel2025/status/1622223633853603841)
Can ChatGPT answer [Project Euler](https://projecteuler.net/) questions?

This is a Python script, scraping Project Euler questions, and send them to [OpenAI GPT-3](https://platform.openai.com/docs/models/gpt-3) model.
Then, submitting the answers to [euler.haku.dev](https://euler.haku.dev/) that returns whether those answers were correct or not.


What do you say?
Would ChatGPT answer all the questions correct?

## How To Run?

This project is running with Python and [Poetry](https://python-poetry.org/docs/#installation)


1. Initialize environment
    ```shell
    poetry install
    ```

1. Signup to OpenAI, and retrieve an [API token](https://platform.openai.com/docs/quickstart/build-your-application)
    ```shell
    export OPENAI_API_KEY=<API_TOKEN>
    ```

1. Run the project
    ```shell
    ➜  poetry run ./main.py --problem 1 --amount 20
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
    │ 11      │ 70600674     │ ✅     │
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

## Contributing

Some of the problems might not get parsed correctly and chatGPT will not be happy with the input.
If you find any problem, please open an issue, or even better, a PR.