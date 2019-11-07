import random
from brain_games.utils import is_even, convert_to_yes_no

GAME_DESCRIPTION = 'Answer "yes" if number even otherwise answer "no"'
MAX_INT = 100
MIN_INT = 0


def create_question():
    number = random.randint(MIN_INT, MAX_INT)
    correct_answer = convert_to_yes_no(is_even(number))
    return (str(number), correct_answer)
