import brain_games.cli as cli
import brain_games.games.game_logic as game_logic


def main():
    cli.greeting('Answer "yes" if given number is prime.\
 Otherwise answer "no".\n')
    name = cli.run()
    win_game = game_logic.game("prime_game")
    if win_game is True:
        print("Congratulations, {}!".format(name))
    else:
        print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()
