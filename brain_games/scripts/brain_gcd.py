#!/usr/bin/env python

import random
from brain_games import cli, game


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    name = cli.welcome_user()
    questions = []
    answers = []

    for _ in range(0, 3):
        a = random.randint(1, 50)
        b = random.randint(1, 50)

        question = f'{a} {b}'
        answer = str(gcd(a, b))

        questions.append(question)
        answers.append(answer)

    print('Find the greatest common divisor of given numbers.')

    game.run(
        name=name,
        questions=questions,
        answers=answers
    )


if __name__ == "__main__":
    main()
