#!/usr/bin/env python

import random
from brain_games import cli, game


def mult(a, b):
    return a * b


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def main():
    name = cli.welcome_user()
    questions = []
    answers = []

    mapping = {
        '+': plus,
        '-': minus,
        '*': mult
    }

    for _ in range(0, 3):
        a = random.randint(0, 20)
        b = random.randint(0, 20)
        op = random.choice(['*', '+', '-'])
        get_result = mapping[op]
        result = get_result(a, b)

        question = f'{a} {op} {b}'
        answer = str(result)

        questions.append(question)
        answers.append(answer)

    print('What is the result of the expression?')

    game.run(
        name=name,
        questions=questions,
        answers=answers
    )


if __name__ == "__main__":
    main()
