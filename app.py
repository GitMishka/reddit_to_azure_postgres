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
    historical_data = []

    for submission in subreddit.new(limit=limit):
        data = {
            "title": submission.title,
            "selftext": submission.selftext,
            "created_utc": submission.created_utc,
            "upvotes": submission.score,
            "url": submission.url
        }
        historical_data.append(data)

    return historical_data

#Example Usage
subreddit_data = collect_subreddit_history('watchexchange', limit=50)
for data in subreddit_data:
    print(data)
