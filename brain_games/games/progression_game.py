import random


GAME_DESCRIPTION = 'What number is missing in the progression?\n'


def create_question():
    MAX_INT = 10
    number = random.randint(0, MAX_INT)
    step = random.randint(1, MAX_INT)
    position = random.randint(0, MAX_INT-1)
    counter = 0
    question = ""
    correct_answer = ""
    while counter < 10:
        if counter != position:
            question = question + " {}".format(number + step*counter)
        else:
            question = question + " .."
            correct_answer = str(number + step*counter)
        counter = counter + 1
    return(question, correct_answer)
