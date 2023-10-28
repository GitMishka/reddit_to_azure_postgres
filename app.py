import praw

reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     user_agent='YOUR_APP_NAME')

subreddit = reddit.subreddit('SUBREDDIT_NAME')

for submission in subreddit.new(limit=10): 
    # Process the data as needed
    print(submission.title, submission.selftext)
