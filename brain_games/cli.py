import prompt


def greeting(description):
    print("Welcome to the Brain Games!")
    print(description)
    print()


def ask_name():
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    print()
    return name


def ask_question(question):
    print('Question: {}'.format(question))
    answer = prompt.string('Your answer: ')
    return answer
