import brain_games.cli as cli
import brain_games.games.even_game_questions as e_g_q
import brain_games.games.calc_game_questions as c_g_q
import brain_games.games.gcd_game_questions as gcd_g_q
import brain_games.games.progression_game_questions as p_g_q
import brain_games.games.prime_game_questions as prime_g_q


def game(game_name):
    counter = 0
    while counter < 3:
        question_with_answer = create_question(game_name)        
        is_answer_correct = cli.ask_question(question_with_answer)
        if is_answer_correct is True:
            counter = counter + 1
        else:
            return False
    return True


def create_question(game_name):
    question_with_answer = ""
    if game_name == "even_game":
        question_with_answer = e_g_q.create_question()
    if game_name == "calc_game":
        question_with_answer = c_g_q.create_question()
    if game_name == "gcd_game":
        question_with_answer = gcd_g_q.create_question()
    if game_name == "progression_game":
        question_with_answer = p_g_q.create_question()
    if game_name == "prime_game":
        question_with_answer = prime_g_q.create_question()
    return question_with_answer
