# Christian Bull

"""
this will collect all new comments for a defined subreddit
collects body, user, x tree, and time
for user, it assigns a unique identifier and strips the username
"""

import csv
import time
import praw

# creates reddit instance
reddit = praw.Reddit('comment_bot',
                     user_agent='comment_bot_agent',
                     )
