import random


GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MAX_INT = 100
MIN_INT = 0


def create_question():
    number1 = random.randint(MIN_INT, MAX_INT)
    number2 = random.randint(MIN_INT, MAX_INT)
    question = "{} {}".format(number1, number2)
    correct_answer = str(find_gcd((number1, number2)))
    return(question, correct_answer)


def find_gcd(pair):
    (first, second) = pair
    if second > first:
        (first, second) = (second, first)
    while second != 0:
        (first, second) = (second, first % second)
    return first
