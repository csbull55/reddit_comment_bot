# Christian Bull

"""
this will collect all new comments for a defined subreddit
collects body, user, x tree, and time
for user, it assigns a unique identifier and strips the username
"""

import time
import pandas as pd
import praw

reddit = praw.Reddit('comment_bot',
                     user_agent='comment_bot_agent',
                     )
# creates df
heads = (
    'author',
    'body',
    'id',
    'parent',
    'time_utc',
)

df = pd.DataFrame(columns=heads)

# run for x amount of time
t_end = time.time() + 30

print(time.time())
print(t_end)
# for each comment in the stream, assigns attributes to variables for the df
while time.time() < t_end:
    for comment in reddit.subreddit('politics').stream.comments():
        auth = comment.author
        body = comment.body
        id = comment.id
        parent = comment.parent_id
        time_utc = comment.created_utc

        # appends df with new comment
        df = df.append({
            'author': auth,
            'body': body,
            'id': id,
            'parent': parent,
            'time_utc': time_utc,
        },
            ignore_index=True)
        print(df.tail())