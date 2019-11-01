import prompt
import random


def even_game():
    counter = 0
    max_int = 100
    min_int = 0
    while counter < 3:
        number = random.randint(min_int, max_int)
        correct_answer = "yes"
        if number % 2 == 1:
            correct_answer = "no"
        print('Question: {}'.format(number))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print("Correct!")
            counter = counter + 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was \
'{}'".format(answer, correct_answer))
            return False
    return True
