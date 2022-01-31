#!/usr/bin/env python

import random
import prompt
from brain_games import cli


def main():
    name = cli.welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    n = 0
    while n < 3:
        n += 1
        number = random.randint(1, 20)
        answer = prompt.string(f'Question: {number}\nYour answer: ')
        right_answer = ['yes', 'no'][number % 2]
        if answer != right_answer:
            break
        else:
            print('Correct!')
    else:
        print(f'Congratulations, {name}!')
        return
    print(
        f'\'{answer}\' is wrong answer ;(. '
        f'Correct answer was \'{right_answer}\'.')
    print(f'Let\'s try again, {name}!')


if __name__ == "__main__":
    main()
