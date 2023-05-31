import praw
from dotenv import load_dotenv
import os

load_dotenv()

reddit = praw.Reddit(
    client_id = os.getenv("TRUE_BORN_WIZ_CLIENT_ID"),
    client_secret = os.getenv("TRUE_BORN_WIZ_CLIENT_SECRET"),
    user_agent = f"True Wizards Promoter by /u/_{os.getenv('TRUE_BORN_WIZ_REDDIT_USERNAME')}",
    username = os.getenv('TRUE_BORN_WIZ_REDDIT_USERNAME'),
    password = os.getenv('THE_PASSWORD')
)