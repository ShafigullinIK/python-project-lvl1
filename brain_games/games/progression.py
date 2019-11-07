import random


GAME_DESCRIPTION = 'What number is missing in the progression?'
MAX_INT = 10
MIN_STEP = 1
MAX_STEP = 10
PROGRESSION_LENGTH = 10


def create_question():
    number = random.randint(0, MAX_INT)
    step = random.randint(MIN_STEP, MAX_STEP)
    position = random.randint(0, PROGRESSION_LENGTH-1)
    counter = 0
    question = ""
    correct_answer = ""
    while counter < PROGRESSION_LENGTH:
        term = ""
        if counter == position:
            term = ".."
            correct_answer = str(number)
        else:
            term = str(number)
        question = question + " {}".format(term)
        counter = counter + 1
        number = number + step
    return(question, correct_answer)
