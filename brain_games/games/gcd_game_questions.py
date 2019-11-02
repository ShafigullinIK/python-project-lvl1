import random


def create_question():
    max_int = 100
    min_int = 0
    number1 = random.randint(min_int, max_int)
    number2 = random.randint(min_int, max_int)
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
