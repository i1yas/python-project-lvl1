#!/usr/bin/env python

import random
from brain_games import cli, game


def main():
    name = cli.welcome_user()
    questions = []
    answers = []

    for _ in range(0, 3):
        step = random.randint(2, 10)
        start = 1
        stop = step * random.randint(5, 10)
        progression = list(str(element) for element in range(start, stop, step))

        unknown_element_pos = random.choice(
            [index for index, _ in enumerate(progression)])
        unknown_element = progression[unknown_element_pos]
        progression[unknown_element_pos] = '..'

        question = ' '.join(progression)
        answer = str(unknown_element)

        questions.append(question)
        answers.append(answer)

    print('What number is missing in the progression?')

    game.run(
        name=name,
        questions=questions,
        answers=answers
    )


if __name__ == "__main__":
    main()
