from instances.true_born_wizard_reddit_ins import reddit
from utilities.all_words import *
from praw.exceptions import APIException
from dotenv import load_dotenv
import random
import time
import re
import threading
import os

load_dotenv()

house_words = ["I'm gonna tell papa &nbsp; !enemies of the heir beware", 
               "Harry Sucks! &nbsp; !enemies of the heir beware", 
               "Filthy mudblood &nbsp; !enemies of the heir beware", 
               "Muggles... &nbsp; !enemies of the heir beware", 
               "I AM THE HEIR TO SALAZAR SLYTHERIN &nbsp; !enemies of the heir beware", 
               "AVADA KADAVRA &nbsp; !enemies of the heir beware"]

subreddit = reddit.subreddit(os.getenv("SUBREDDIT"))
print("True Born Bot is running")

def process_submissions():
    try:
        for submission in subreddit.stream.submissions():
            if hasattr(submission, "selftext"):
                if any(keyword.lower() in submission.selftext.lower() for keyword in name_or_place):
                    print("**True Born bot has found the muggles!**")
                    random_index = random.randint(0, len(house_words) - 1)
                    submission.reply(house_words[random_index])
    except (APIException) as e:
        for sub in e.items:
            if sub.error_type == "RATELIMIT":
                delay = re.search("(\d+) minutes?", sub.message)
                delay_seconds = float(int(delay.group(1)) + 1) * 60
                print(f"Sleeping for {delay_seconds} seconds")
                time.sleep(delay_seconds)
                random_index = random.randint(0, len(house_words) - 1)
                submission.reply(house_words[random_index])

def process_comments():
    try:
        for comment in subreddit.stream.comments():
            if any(keyword in comment.body.lower() for keyword in name_or_place):
                print("**True born bot has found the muggles**")
                random_index = random.randint(0, len(house_words) - 1)
                comment.reply(house_words[random_index])
    except (APIException) as e:
        for sub in e.items:
            if sub.error_type == "RATELIMIT":
                delay = re.search("(\d+) minutes?", sub.message)
                delay_seconds = float(int(delay.group(1)) + 1) * 60
                print(f"Sleeping for {delay_seconds} seconds")
                time.sleep(delay_seconds)
                random_index = random.randint(0, len(house_words) - 1)
                comment.reply(house_words[random_index])


comment_thread = threading.Thread(target=process_comments)
submission_thread = threading.Thread(target=process_submissions)

comment_thread.start()
submission_thread.start()
