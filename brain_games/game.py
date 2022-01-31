from brain_games import cli


def run(name, questions, answers):
    for question, answer in zip(questions, answers):
        user_answer = cli.ask_question(question)
        if user_answer != answer:
            break
        else:
            cli.correct_answer()
    else:
        cli.win(name)
        return
    cli.wrong_answer(right_answer=answer, wrong_answer=user_answer)
    cli.try_again(name)
