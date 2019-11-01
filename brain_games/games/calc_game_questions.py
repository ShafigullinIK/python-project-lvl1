import random


def create_question():
    max_int = 100
    min_int = 0
    number1 = random.randint(min_int, max_int)
    number2 = random.randint(min_int, max_int)
    operation = random.choice("+-*")
    question = "{} {} {} =".format(number1, operation, number2)
    correct_answer = str(number1*number2)
    if operation == "+":
        correct_answer = str(number1 + number2)
    if operation == "-":
        correct_answer = str(number1 - number2)
    return(question, correct_answer)
