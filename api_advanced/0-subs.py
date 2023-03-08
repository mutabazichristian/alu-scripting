#!/usr/bin/python3
"""
I have no idea what they mean by documenting (didn't quiet get it last time but, we move!)
"""
import requests

"""
Write a function that queries the Reddit API and returns the number of 
subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.
"""
def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0

