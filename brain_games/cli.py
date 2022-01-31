import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    return name


def ask_question(question):
    print(f'Question: {question}')
    return prompt.string('Your answer: ')


def correct_answer():
    print('Correct')


def wrong_answer(right_answer, wrong_answer):
    print(
        f'\'{wrong_answer}\' is wrong answer ;(. '
        f'Correct answer was \'{right_answer}\'.')


def try_again(name):
    print(f'Let\'s try again, {name}!')


def win(name):
    print(f'Congratulations, {name}!')
