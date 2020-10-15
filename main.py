import praw
from urllib.request import urlretrieve

reddit = praw.Reddit(client_id='###',
                client_secret='###',
                user_agent='foreseon r_RequestABot Request',
                username='##',
                password='##')

videos = []

posts = reddit.subreddit("minecraft").top("week", limit=50)
for sub in posts:
    try:
        url = sub.media['reddit_video']['fallback_url']
        url = url.split("?")[0]
        name = sub.title.rstrip() + ".mp4"
        videos.append((url,name))
    except:
        pass

if videos:
    for section in videos:
        urlretrieve(section[0], section[1])