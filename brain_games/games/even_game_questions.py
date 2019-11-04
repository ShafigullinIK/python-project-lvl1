import random


def create_question():
    MAX_INT = 100
    MIN_INT = 0
    number = random.randint(MIN_INT, MAX_INT)
    correct_answer = "yes"
    if number % 2 == 1:
        correct_answer = "no"
    return (str(number), correct_answer)
