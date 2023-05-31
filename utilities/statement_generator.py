import random
from utilities.all_words import *

def statement_generator():
    statement = ""
    statement += possesives[random.randint(0, len(possesives) - 1)] + " "
    statement += nouns[random.randint(0, len(nouns) - 1)] + " "
    statement += be_verbs[random.randint(0, len(be_verbs) - 1)] + " "
    statement += adjective[random.randint(0, len(adjective) - 1)]
    statement += "."
    return statement