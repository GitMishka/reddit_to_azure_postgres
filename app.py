import pandas as pd
import praw
import config

def collect_subreddit_history(subreddit_name, limit=100):
    user_agent = "Searchbot_01"
    reddit = praw.Reddit(username=config.reddit_username,
                         password=config.reddit_password,
                         client_id=config.reddit_client_id,
                         client_secret=config.reddit_client_secret,
                         user_agent=user_agent,
                         check_for_async=False)

    subreddit = reddit.subreddit(subreddit_name)
    data_list = []

    for submission in subreddit.new(limit=limit):
        data = {
            "title": submission.title,
            "selftext": submission.selftext,
            "created_utc": submission.created_utc,
            "upvotes": submission.score,
            "url": submission.url
            # Add more fields as required
        }
        data_list.append(data)

    return pd.DataFrame(data_list)

df = collect_subreddit_history('python', limit=50)
print(df.head())

import psycopg2

conn = psycopg2.connect(
    host=config.pg_host,
    database=config.pg_database,
    user=config.pg_user,
    password=config.pg_password)

cur = conn.cursor()

# Example: Insert data into the database
# cur.execute("INSERT INTO your_table (column1, column2) VALUES (%s, %s)", (data1, data2))

conn.commit()
cur.close()
conn.close()

