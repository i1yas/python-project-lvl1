#!/usr/bin/env python

import random
import math
import itertools
from brain_games import cli, game


def is_prime(number):
    if number < 4:
        return True
    start = 2
    end = math.ceil(math.sqrt(number)) + 1
    for d in range(start, end):
        if math.gcd(number, d) != 1:
            return False
    return True


def get_prime(n):
    index = 0
    for number in itertools.count(2):
        if not is_prime(number):
            continue
        index += 1
        if index == n:
            return number


def main():
    name = cli.welcome_user()
    questions = []
    answers = []

    show_prime_on = random.randint(0, 2)

    for index in range(0, 3):
        is_prime = show_prime_on == index
        number = 0
        if is_prime:
            number = get_prime(random.randint(5, 13))
        else:
            number = random.randint(2, 5) * random.randint(2, 10)

        question = number
        answer = ['no', 'yes'][int(is_prime)]

        questions.append(question)
        answers.append(answer)

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    game.run(
        name=name,
        questions=questions,
        answers=answers
    )


if __name__ == "__main__":
    main()
