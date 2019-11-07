import brain_games.cli as cli


WIN_MESSAGE = "Congratulations, {}!"
LOSE_MESSAGE = "Let's try again, {}!"


def run(game):
    cli.greeting(game.GAME_DESCRIPTION)
    name = cli.ask_name()
    player_won = start_game(game)
    message = LOSE_MESSAGE
    if player_won:
        message = WIN_MESSAGE
    print(message.format(name))


def start_game(game):
    counter = 0
    while counter < 3:
        (question, correct_answer) = game.create_question()
        answer = cli.ask_question(question)
        answer_is_correct = chek_answer(answer, correct_answer)
        if answer_is_correct:
            counter = counter + 1
        else:
            return False
    return True


def chek_answer(answer, correct_answer):
    if answer == correct_answer:
        print("Correct!")
        return True
    else:
        print("'{}' is wrong answer ;(. Correct answer was \
'{}'".format(answer, correct_answer))
        return False
