import brain_games.cli as cli
import brain_games.games.game_logic as game_logic


def main():
    cli.greeting('What number is missing in the progression?\n')
    name = cli.run()
    win_game = game_logic.game("progression_game")
    if win_game is True:
        print("Congratulations, {}!".format(name))
    else:
        print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()
