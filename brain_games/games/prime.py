import random
import math
from brain_games.utils import is_even, convert_to_yes_no


GAME_DESCRIPTION = (
    'Answer "yes" if given number is prime.'
    'Otherwise answer "no".'
)
MAX_INT = 100
MIN_INT = 0


def create_question():
    number = random.randint(MIN_INT, MAX_INT)
    question = "{}".format(number)
    correct_answer = convert_to_yes_no(is_prime(number))
    return(question, correct_answer)


def is_prime(n):
    if n == 2:
        return True
    if is_even(n):
        return False
    counter = 3
    bound = math.sqrt(n)
    while counter <= bound:
        if not n % counter:
            return False
        counter = counter + 2
    return True
