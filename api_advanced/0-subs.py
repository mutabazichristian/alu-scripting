#!/usr/bin/python3
"""
I have no idea what they mean by documenting (didn't quiet get it last time but, we move!)
"""
import requests

def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/dev/api/{subreddit}'
    headers = {'user-Agent': 'Mozilla/5.0'}
    response = requests.get(url,headers)

    if response.status_code == 200:
        data = response.json()
        return data[data][subscribers]

    else:
        return 0 