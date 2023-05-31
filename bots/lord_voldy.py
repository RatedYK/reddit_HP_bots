from instances.lord_voldy_reddit_ins import reddit
import threading
from dotenv import load_dotenv
import os

load_dotenv()

subreddit = reddit.subreddit(os.getenv("SUBREDDIT"))

print("Lord Voldy Bot is running")

def process_submissions():
    for submission in subreddit.stream.submissions():
        try:
            if "voldemort" in submission.title.lower() or "voldemort" in submission.selftext.lower():
                print(f"MY LORD YOU HAVE BEEN SUMMONED AT: {submission.title} WITH THE TEXT: {submission.selftext}")
                # Wait for my approval
                reponse = input("Do you want to reply my lord? (y/n): ")
                if reponse.lower() == "y":
                    comment_response = input("What do you want to reply my lord?: ")
                    submission.reply(comment_response)
                    print("I have replied my lord")
                    print("Searching for the next muggle")
                else:
                    print("I will not reply my lord")
            # print("Searching for the next submission")
        except Exception as e:
            print(e)

def process_comments():
    for comment in subreddit.stream.comments():
        try:
            if "voldemort" in comment.body.lower():
                print(f"MY LORD YOU HAVE BEEN SUMMONED AT THIS COMMENT: {comment.body}")
                reponse = input("Do you want to reply my lord? (y/n): ")
                if reponse.lower() == "y":
                    comment_response = input("What do you want to reply my lord?: ")
                    comment.reply(comment_response)
                    print("I have replied my lord")
                    print("Searching for the next muggle")
                else:
                    print("I will not reply my lord")
            # print("Searching for the next comment")
        except Exception as e:
            print(e)

comment_thread = threading.Thread(target=process_comments)
submission_thread = threading.Thread(target=process_submissions)

comment_thread.start()
submission_thread.start()