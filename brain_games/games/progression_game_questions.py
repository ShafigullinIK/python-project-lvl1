import random


def create_question():
    max_int = 10
    number = random.randint(0, max_int)
    step = random.randint(1, max_int)
    position = random.randint(0, max_int)
    counter = 0
    question = ""
    while counter < 10:
        if counter != position:
            question = question + " {}".format(number + step*counter)
        else:
            question = question + " .."
            correct_answer = str(number + step*counter)
        counter = counter + 1
    return(question, correct_answer)
