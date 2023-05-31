from instances.heir_to_ss_reddit_ins import reddit
from utilities.muggle_insult_generator import make_muggle_insult
import threading
from dotenv import load_dotenv
import os

load_dotenv()

subreddit = reddit.subreddit(os.getenv("SUBREDDIT"))

print("The Heir To Salazar Slytherin Bot is running")

key_phrase = ["!enemies of the heir beware", "!enemies of the heir, beware", "!enemies of the heir beware!", "!enemies of the heir, beware!", "!enemies_of_the_heir_beware"]

def process_comments():
    for comment in subreddit.stream.comments():
        try:
            if hasattr(comment, "body"):
                if any(keyword.lower() in comment.body.lower() for keyword in key_phrase):
                    print(f"Summoned from this comment: {comment.body}")
                    comment.reply(make_muggle_insult())
            print("Searching for the next comment")
        except Exception as e:
            print(e)

def process_submissions():
    for submission in subreddit.stream.submissions():
        try:
            if any(keyword.lower() in submission.selftext.lower() for keyword in key_phrase):
                print("Summoned from this submission: {submission.title}")
                muggle_insult = make_muggle_insult()
                submission.reply(muggle_insult)
                print(f"Replied with: {muggle_insult}")
            print("Searching for the next submission")
        except Exception as e:
            print(e)



comment_thread = threading.Thread(target=process_comments)
submission_thread = threading.Thread(target=process_submissions)

comment_thread.start()
submission_thread.start()
