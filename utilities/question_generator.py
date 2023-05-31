import random
from utilities.all_words import *

def question_generator():
    random_number = random.randint(0, 1)

    if random_number == 0:
        return wh_question_generator()
    else:
        return yn_question_generator()


def wh_question_generator():
    question = ""
    question += wh_question[random.randint(0, len(wh_question) - 1)] + " "
    question += name_or_place[random.randint(0, len(name_or_place) - 1)] + " "
    question += verbs[random.randint(0, len(verbs) - 1)] + " "
    question += nouns[random.randint(0, len(nouns) - 1)] + "?"
    return question

def yn_question_generator():
    question = ""
    question += yn_question[random.randint(0, len(yn_question) - 1)] + " "
    question += name_or_place[random.randint(0, len(name_or_place) - 1)]  + " "
    question += verbs[random.randint(0, len(be_verbs) - 1)] + " "
    question += nouns[random.randint(0, len(nouns) - 1)] + "?"
    return question