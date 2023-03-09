#!/usr/bin/python3
"""
Recursive function that queries Reddit API,
and returns a list containing the titles of all hot
articles for a given subreddit.

No result returns "None"
"""

import requests

def recurse(subreddit, hot_list=[],after='None'):
    url = 'https://reddit.com/r/hot.json'.format('subreddit')
    headers = {'User-Agent' : 'Mozilla/5.o'}
    params = {'limit' : 100}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()

        for post in data['data']['children']:
            title = post['data']['title']
            hot_list.append(title)

        after = data['data']['after']
    if data['after']:
        return recurse(subreddit, hot_list,data['after'])
    else:
        return 'None'
    
