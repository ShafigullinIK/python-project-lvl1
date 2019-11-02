import brain_games.cli
import brain_games.games.game_logic


def main():
    print("Welcome to the Brain Games!")
    print('What number is missing in the progression?\n')
    name = brain_games.cli.run()
    win_game = brain_games.games.game_logic.game("progression_game")
    if win_game is True:
        print("Congratulations, {}!".format(name))
    else:
        print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()
