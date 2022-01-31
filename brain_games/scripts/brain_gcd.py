#!/usr/bin/env python

import random
import math
from brain_games import cli, game


def main():
    name = cli.welcome_user()
    questions = []
    answers = []

    for _ in range(0, 3):
        k = random.randint(2, 20)
        a = k * random.randint(1, 20)
        b = k * random.randint(1, 20)

        question = f'{a} {b}'
        answer = str(math.gcd(a, b))

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
