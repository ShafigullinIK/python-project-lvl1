import random


GAME_DESCRIPTION = 'What is the result of the expression?\n'


def create_question():
    MAX_INT = 100
    MIN_INT = 0
    number1 = random.randint(MIN_INT, MAX_INT)
    number2 = random.randint(MIN_INT, MAX_INT)
    operation = random.choice("+-*")
    question = "{} {} {} =".format(number1, operation, number2)
    correct_answer = str(number1*number2)
    if operation == "+":
        correct_answer = str(number1 + number2)
    if operation == "-":
        correct_answer = str(number1 - number2)
    return(question, correct_answer)
