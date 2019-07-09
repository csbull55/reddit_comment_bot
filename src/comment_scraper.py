# Christian Bull

"""
this will collect all new comments for a defined subreddit
collects body, user, x tree, and time
for user, it assigns a unique identifier and strips the username
"""

import csv
import praw

reddit = praw.Reddit('comment_bot',
                     user_agent='comment_bot_agent',
                     )

# for each comment in the stream, assigns attributes to variables for the csv
for comment in reddit.subreddit('politics').stream.comments():
    auth = comment.author
    body = comment.body
    comment_id = comment.id
    parent = comment.parent_id
    time_utc = comment.created_utc

    # assigns comment data to row
    csv_row = [auth, body, comment_id, parent, time_utc]

    # appends comment to csv
    try:
        with open (r'test_comment_data.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(csv_row)
    except:
        print('error')
