import random
import operator


GAME_DESCRIPTION = 'What is the result of the expression?'
MAX_INT = 100
MIN_INT = 0


def create_question():
    number1 = random.randint(MIN_INT, MAX_INT)
    number2 = random.randint(MIN_INT, MAX_INT)
    (operation, symbol) = get_random_operation_and_symbol()
    question = "{} {} {} =".format(number1, symbol, number2)
    correct_answer = str(operation(number1, number2))
    return (question, correct_answer)


def get_random_operation_and_symbol():
    symbol = random.choice("+-*")
    if symbol == "+":
        return (operator.add, "+")
    if symbol == "-":
        return (operator.sub, "-")
    return (operator.mul, "*")
