import brain_games.cli as cli


WIN_MESSAGE = "Congratulations, {}!"
LOSE_MESSAGE = "Let's try again, {}!"
WRONG_ANSWER_MESSAGE = (
    "'{}' is wrong answer ;(. Correct answer was '{}'"
)


def run(game):
    cli.greet(game.GAME_DESCRIPTION)
    name = cli.ask_name()
    player_won = True
    counter = 0
    while counter < 3:
        (question, correct_answer) = game.create_question()
        answer = cli.ask_question(question)
        if answer == correct_answer:
            print("Correct!")
            counter = counter + 1
        else:
            print(WRONG_ANSWER_MESSAGE.format(answer, correct_answer))
            player_won = False
            break
    message = WIN_MESSAGE if player_won else LOSE_MESSAGE
    print(message.format(name))
