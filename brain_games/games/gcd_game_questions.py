import random


def create_question():
    MAX_INT = 100
    MIN_INT = 0
    number1 = random.randint(MIN_INT, MAX_INT)
    number2 = random.randint(MIN_INT, MAX_INT)
    question = "{} {}".format(number1, number2)
    correct_answer = str(find_gcd((number1, number2)))
    return(question, correct_answer)


def find_gcd(pair):
    (first, second) = pair
    if second > first:
        (first, second) = (second, first)
    while first % second != 0:
        temp = second
        second = first % second
        first = temp
    return second
