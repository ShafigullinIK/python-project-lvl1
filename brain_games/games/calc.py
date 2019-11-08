import random
import operator


GAME_DESCRIPTION = 'What is the result of the expression?'
MAX_INT = 100
MIN_INT = 0


def create_question():
    number1 = random.randint(MIN_INT, MAX_INT)
    number2 = random.randint(MIN_INT, MAX_INT)
    operations = [
        (operator.add, "+"), (operator.sub, "-"), (operator.mul, "*")
    ]
    (operation, symbol) = random.choice(operations)
    question = "{} {} {} =".format(number1, symbol, number2)
    correct_answer = str(operation(number1, number2))
    return (question, correct_answer)
