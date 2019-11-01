import brain_games.cli
import brain_games.games.game_logic


def main():
    print("Welcome to the Brain Games!")
    print('What is the result of the expression?\n')
    name = brain_games.cli.run()
    win_even_game = brain_games.games.game_logic.game("calc_game")
    if win_even_game is True:
        print("Congratulations, {}!".format(name))
    else:
        print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()
