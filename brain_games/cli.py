import prompt


def run():
    name = prompt.string('May I have your name? ')
    print("Hello, {}! \n".format(name))
    return name


def ask_question(Q_A):
    (question, correct_answer) = Q_A
    print('Question: {}'.format(question))
    answer = prompt.string('Your answer: ')
    if answer == correct_answer:
        print("Correct!")
        return True
    else:
        print("'{}' is wrong answer ;(. Correct answer was \
'{}'".format(answer, correct_answer))
        return False
