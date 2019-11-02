import random


def create_question():
    max_int = 100
    min_int = 0
    number = random.randint(min_int, max_int)
    question = "{}".format(number)
    correct_answer = is_prime(number)
    return(question, correct_answer)


def is_prime(n):
    counter = 2
    while counter <= n/2:
        if n % counter == 0:
            return "yes"
        counter = counter + 1
    return "no"
