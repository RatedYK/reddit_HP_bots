from instances.muggle_ins import reddit
from utilities.question_generator import question_generator
from utilities.statement_generator import statement_generator
import threading
import random
from dotenv import load_dotenv
import os

load_dotenv()

subreddit = reddit.subreddit(os.getenv("SUBREDDIT"))

print("Muggle Bot is running")

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec) 
        func()  
    t = threading.Timer(sec, func_wrapper)
    t.start()
    print(f"Next post will be in {sec} seconds")
    return t

def post_submission():
    subreddit.submit(
        title=statement_generator(),
        selftext=question_generator(),
    )

post_submission()

set_interval(post_submission, random.randint(600, 720))

