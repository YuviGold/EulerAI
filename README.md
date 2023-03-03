# EulerAI - Project Euler GPT Resolver

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
<!-- [[[cog
import cog
from textwrap import dedent
import subprocess

def print_command(command):
    cog.outl(dedent(f"""
```bash
$ {command}

{subprocess.getoutput(command)}
```
    """))

print_command("poetry run ./main.py --problem 1 --amount 50")

print_command("poetry run ./main.py --problem 27 --max-tries 3 --output pretty-json")

]]] -->

```bash
$ poetry run ./main.py --problem 1 --amount 50

                                                                Project Euler                                                                
┏━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Problem ┃ Solution     ┃ Status ┃ Answers                                                                                                 ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 1       │ 233168       │ ✅     │ [('gpt-3.5-turbo', 0, '233168')]                                                                        │
│ 2       │ 4613732      │ ✅     │ [('gpt-3.5-turbo', 0, '4613732')]                                                                       │
│ 3       │ 6857         │ ✅     │ [('gpt-3.5-turbo', 0, '6857')]                                                                          │
│ 4       │ 906609       │ ✅     │ [('gpt-3.5-turbo', 0, '906609')]                                                                        │
│ 5       │ 232792560    │ ✅     │ [('gpt-3.5-turbo', 0, '232792560')]                                                                     │
│ 6       │ 25164150     │ ✅     │ [('gpt-3.5-turbo', 0, '25164150')]                                                                      │
│ 7       │ 104743       │ ✅     │ [('gpt-3.5-turbo', 0, '104743')]                                                                        │
│ 8       │ 23514624000  │ ✅     │ [('gpt-3.5-turbo', 0, '23514624000')]                                                                   │
│ 9       │ 31875000     │ ✅     │ [('gpt-3.5-turbo', 0, '31875000')]                                                                      │
│ 10      │ 142913828922 │ ✅     │ [('gpt-3.5-turbo', 0, '142913828922')]                                                                  │
│ 11      │ 70600674     │ ✅     │ [('gpt-3.5-turbo', 0, '70600674')]                                                                      │
│ 12      │ 76576500     │ ✅     │ [('gpt-3.5-turbo', 0, '76576500')]                                                                      │
│ 13      │ 5537376230   │ ✅     │ [('gpt-3.5-turbo', 0, '5537376230')]                                                                    │
│ 14      │ 837799       │ ✅     │ [('gpt-3.5-turbo', 0, '837799')]                                                                        │
│ 15      │ 137846528820 │ ✅     │ [('gpt-3.5-turbo', 0, '137846528820')]                                                                  │
│ 16      │ 1366         │ ✅     │ [('gpt-3.5-turbo', 0, '1366')]                                                                          │
│ 17      │ 21124        │ ✅     │ [('gpt-3.5-turbo', 0, '21124')]                                                                         │
│ 18      │ 1074         │ ✅     │ [('gpt-3.5-turbo', 0, '1074')]                                                                          │
│ 19      │ 171          │ ✅     │ [('gpt-3.5-turbo', 0, '171')]                                                                           │
│ 20      │ 648          │ ✅     │ [('gpt-3.5-turbo', 0, '648')]                                                                           │
│ 21      │ 31626        │ ✅     │ [('gpt-3.5-turbo', 0, '31626')]                                                                         │
│ 22      │ 871198282    │ ✅     │ [('gpt-3.5-turbo', 0, '871198282')]                                                                     │
│ 23      │ 4179871      │ ✅     │ [('gpt-3.5-turbo', 0, '4179871')]                                                                       │
│ 24      │ 2783915460   │ ✅     │ [('gpt-3.5-turbo', 0, '2783915460')]                                                                    │
│ 25      │ 4782         │ ✅     │ [('gpt-3.5-turbo', 0, '1000'), ('text-davinci-002', 0, '4782')]                                         │
│ 26      │ 983          │ ✅     │ [('gpt-3.5-turbo', 0, '983')]                                                                           │
│ 27      │ ?            │ ❌     │ [('gpt-3.5-turbo', 0, '59231'), ('text-davinci-002', 0, '59231'), ('text-davinci-003', 0, '59231')]     │
│ 28      │ 669171001    │ ✅     │ [('gpt-3.5-turbo', 0, '669'), ('text-davinci-002', 0, '669171001')]                                     │
│ 29      │ 9183         │ ✅     │ [('gpt-3.5-turbo', 0, '9183')]                                                                          │
│ 30      │ 443839       │ ✅     │ [('gpt-3.5-turbo', 0, '443'), ('text-davinci-002', 0, '19316'), ('text-davinci-003', 0, '443839')]      │
│ 31      │ 73682        │ ✅     │ [('gpt-3.5-turbo', 0, '73682')]                                                                         │
│ 32      │ 45228        │ ✅     │ [('gpt-3.5-turbo', 0, '45228')]                                                                         │
│ 33      │ 100          │ ✅     │ [('gpt-3.5-turbo', 0, '100')]                                                                           │
│ 34      │ 40730        │ ✅     │ [('gpt-3.5-turbo', 0, '40730')]                                                                         │
│ 35      │ 55           │ ✅     │ [('gpt-3.5-turbo', 0, '55')]                                                                            │
│ 36      │ 872187       │ ✅     │ [('gpt-3.5-turbo', 0, '872187')]                                                                        │
│ 37      │ 748317       │ ✅     │ [('gpt-3.5-turbo', 0, '748317')]                                                                        │
│ 38      │ 932718654    │ ✅     │ [('gpt-3.5-turbo', 0, '1'), ('text-davinci-002', 0, '918273645'), ('text-davinci-003', 0, '932718654')] │
│ 39      │ 840          │ ✅     │ [('gpt-3.5-turbo', 0, '840')]                                                                           │
│ 40      │ 210          │ ✅     │ [('gpt-3.5-turbo', 0, '210')]                                                                           │
│ 41      │ 7652413      │ ✅     │ [('gpt-3.5-turbo', 0, '7652413')]                                                                       │
│ 42      │ 162          │ ✅     │ [('gpt-3.5-turbo', 0, '162')]                                                                           │
│ 43      │ 16695334890  │ ✅     │ [('gpt-3.5-turbo', 0, '16695334890')]                                                                   │
│ 44      │ 5482660      │ ✅     │ [('gpt-3.5-turbo', 0, '5482660')]                                                                       │
│ 45      │ 1533776805   │ ✅     │ [('gpt-3.5-turbo', 0, '1533776805')]                                                                    │
│ 46      │ ?            │ ❌     │ [('gpt-3.5-turbo', 0, '577'), ('text-davinci-002', 0, '11'), ('text-davinci-003', 0, '45')]             │
│ 47      │ ?            │ ❌     │ [('gpt-3.5-turbo', 0, '210'), ('text-davinci-002', 0, '6'), ('text-davinci-003', 0, '13')]              │
│ 48      │ 9110846700   │ ✅     │ [('gpt-3.5-turbo', 0, '9110846700')]                                                                    │
│ 49      │ 296962999629 │ ✅     │ [('gpt-3.5-turbo', 0, '296962999629')]                                                                  │
│ 50      │ 997651       │ ✅     │ [('gpt-3.5-turbo', 0, '997651')]                                                                        │
└─────────┴──────────────┴────────┴─────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```


```bash
$ poetry run ./main.py --problem 27 --max-tries 3 --output pretty-json

[
    {
        "problem": "27",
        "prompt": "For the following problem, return only the solution as a number without any other text:

            Euler discovered the remarkable quadratic formula:

            n^2 + n + 41

            It turns out that the formula will produce 40 primes for the consecutive integer values 0 \u2264 n \u2264 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

            The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 \u2264 n \u2264 79. The product of the coefficients, \u221279 and 1601, is \u2212126479.

            Considering quadratics of the form:


            n^2 + an + b, where |a| < 1000 and |b| \u2264 1000where |n| is the modulus/absolute value of ne.g. |11| = 11 and |-4| = 4


            Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.",
        "solution": "?",
        "answers": [
            [
                "gpt-3.5-turbo",
                0,
                "59231"
            ],
            [
                "text-davinci-002",
                0,
                "59231"
            ],
            [
                "text-davinci-003",
                0,
                "59231"
            ],
            [
                "gpt-3.5-turbo",
                0.5,
                "59231"
            ],
            [
                "text-davinci-002",
                0.5,
                "59231"
            ],
            [
                "text-davinci-003",
                0.5,
                "59231"
            ],
            [
                "gpt-3.5-turbo",
                1.0,
                "59231"
            ],
            [
                "text-davinci-002",
                1.0,
                "59231"
            ],
            [
                "text-davinci-003",
                1.0,
                "59231"
            ]
        ],
        "status": false,
        "tries": 3
    }
]
```

<!-- [[[end]]] -->

## Options

```--problem <number>``` The problem number to start from, minimum is 1

```--amount <number>``` The amount of problems to solve, default is 10

```--output <table|pretty-json|json>``` The output format, default is table

```--max-tries <number>``` The maximum amount of tries to get a correct answer, default is 1

```--temperture <decimal>``` The creativty temperture of the model, default is 0, max is 1. 

## Contributing

Some of the problems might not get parsed correctly and chatGPT will not be happy with the input.
If you find any problem, please open an issue, or even better, a PR.

### Run GHA

I use [nektos/act](https://github.com/nektos/act) tool to run the Git Hub Action locally.
By default, act runs on a slim container image, for docker-compose usage the base image is replaced.

```bash
act --platform=ubuntu-latest=lucasalt/act_base:latest -j <JOB>
```

## Generate docs

Might take a couple of minutes due to OpenAI rate limiter

```bash
make docs
```
