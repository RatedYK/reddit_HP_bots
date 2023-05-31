import praw
from dotenv import load_dotenv
import os

load_dotenv()

reddit = praw.Reddit(
    client_id = os.getenv("HEIR_TO_SS_CLIENT_ID"),
    client_secret= os.getenv("HEIR_TO_SS_CLIENT_SECRET"),
    user_agent = f"The Heir To Salazar Slytherin by /u/_{os.getenv('HEIR_TO_SS_REDDIT_USERNAME')}",
    username = os.getenv("HEIR_TO_SS_REDDIT_USERNAME"),
    password = os.getenv("THE_PASSWORD")
)