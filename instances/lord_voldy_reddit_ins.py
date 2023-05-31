import praw
from dotenv import load_dotenv
import os

load_dotenv()

reddit = praw.Reddit(
    client_id = os.getenv("LORD_VOLDY_CLIENT_ID"),
    client_secret = os.getenv("LORD_VOLDY_CLIENT_SECRET"),
    user_agent = f"Lord Voldy by /u/_{os.getenv('LORD_VOLDY_REDDIT_USERNAME')}",
    username = os.getenv('LORD_VOLDY_REDDIT_USERNAME'),
    password = os.getenv('THE_PASSWORD')
)