import random


GAME_DESCRIPTION = 'Answer "yes" if given number is prime.\
 Otherwise answer "no".\n'


def create_question():
    MAX_INT = 100
    MIN_INT = 0
    number = random.randint(MIN_INT, MAX_INT)
    question = "{}".format(number)
    correct_answer = is_prime(number)
    return(question, correct_answer)


def is_prime(n):
    counter = 2
    while counter <= n/2:
        if n % counter == 0:
            return "no"
        counter = counter + 1
    return "yes"
