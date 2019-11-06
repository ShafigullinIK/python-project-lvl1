import brain_games.cli as cli


def run(game):
    cli.greeting(game.GAME_DESCRIPTION)
    name = cli.run()
    win_game = start_game(game)
    if win_game is True:
        print("Congratulations, {}!".format(name))
    else:
        print("Let's try again, {}!".format(name))


def start_game(game):
    counter = 0
    while counter < 3:
        question_with_answer = game.create_question()
        is_answer_correct = cli.ask_question(question_with_answer)
        if is_answer_correct is True:
            counter = counter + 1
        else:
            return False
    return True
