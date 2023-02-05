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

Not all the problems run smooth. The prompt is consuming Project Euler's HTML and OpenAI doesn't like it that much.
The parsing still needs to be improved.

    ```shell
    ➜  poetry run ./main.py --problem 27 --verbose
                                    Project Euler                                  
    ┏━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃ Problem ┃ Solution ┃ Status ┃ Prompt                                         ┃
    ┡━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
    │ 27      │ 59231    │ ❌     │ For the following problem, return only the     │
    │         │          │        │ solution as a number without any other text:   │
    │         │          │        │                                                │
    │         │          │        │ <div class="problem_content" role="problem">   │
    │         │          │        │ <p>Euler discovered the remarkable quadratic   │
    │         │          │        │ formula:</p>                                   │
    │         │          │        │ <p class="center">$n^2 + n + 41$</p>           │
    │         │          │        │ <p>It turns out that the formula will produce  │
    │         │          │        │ 40 primes for the consecutive integer values   │
    │         │          │        │ $0 \le n \le 39$. However, when $n = 40, 40^2  │
    │         │          │        │ + 40 + 41 = 40(40 + 1) + 41$ is divisible by   │
    │         │          │        │ 41, and certainly when $n = 41, 41^2 + 41 +    │
    │         │          │        │ 41$ is clearly divisible by 41.</p>            │
    │         │          │        │ <p>The incredible formula $n^2 - 79n + 1601$   │
    │         │          │        │ was discovered, which produces 80 primes for   │
    │         │          │        │ the consecutive values $0 \le n \le 79$. The   │
    │         │          │        │ product of the coefficients, −79 and 1601, is  │
    │         │          │        │ −126479.</p>                                   │
    │         │          │        │ <p>Considering quadratics of the form:</p>     │
    │         │          │        │ <blockquote>                                   │
    │         │          │        │ $n^2 + an + b$, where $|a| &lt; 1000$ and $|b| │
    │         │          │        │ \le 1000$<br><br/><div>where $|n|$ is the      │
    │         │          │        │ modulus/absolute value of $n$<br/>e.g. $|11| = │
    │         │          │        │ 11$ and $|-4| = 4$</div>                       │
    │         │          │        │ </br></blockquote>                             │
    │         │          │        │ <p>Find the product of the coefficients, $a$   │
    │         │          │        │ and $b$, for the quadratic expression that     │
    │         │          │        │ produces the maximum number of primes for      │
    │         │          │        │ consecutive values of $n$, starting with $n =  │
    │         │          │        │ 0$.</p>                                        │
    │         │          │        │ </div>                                         │
    └─────────┴──────────┴────────┴────────────────────────────────────────────────┘
    ```
