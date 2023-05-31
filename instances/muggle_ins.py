import praw
from dotenv import load_dotenv
import os

load_dotenv()

reddit = praw.Reddit(
    client_id = os.getenv("MUGGLE_CLIENT_ID"),
    client_secret = os.getenv("MUGGLE_CLIENT_SECRET"),
    user_agent = f"Muggle Poster by /u/_{os.getenv('MUGGLE_REDDIT_USERNAME')}",
    username = os.getenv('MUGGLE_REDDIT_USERNAME'),
    password= os.getenv('THE_PASSWORD')
)
