import random


def create_question():
    max_int = 100
    min_int = 0
    number = random.randint(min_int, max_int)
    correct_answer = "yes"
    if number % 2 == 1:
        correct_answer = "no"
    return (str(number), correct_answer)
