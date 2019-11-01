import brain_games.cli
import brain_games.brain_even_logic


def main():
    print("Welcome to the Brain Games!")
    print('Answer "yes" if number even otherwise answer "no"\n')
    name = brain_games.cli.run()
    win_even_game = brain_games.brain_even_logic.even_game()
    if win_even_game is True:
        print("Congratulations, {}!".format(name))
    else:
        print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()
