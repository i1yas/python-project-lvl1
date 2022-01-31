#!/usr/bin/env python

import random
from brain_games import cli, game


def main():
    name = cli.welcome_user()
    questions = []
    answers = []

    for _ in range(0, 3):
        question = random.randint(1, 20)
        answer = ['yes', 'no'][question % 2]
        questions.append(question)
        answers.append(answer)

    print('Answer "yes" if the number is even, otherwise answer "no".')

    game.run(
        name=name,
        questions=questions,
        answers=answers
    )


if __name__ == "__main__":
    main()
