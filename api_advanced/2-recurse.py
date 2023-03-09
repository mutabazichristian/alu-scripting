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

    if after:
        params['after'] = params
        response = requests.get(url, headers=headers, params=params)
        return recurse(subreddit,hot_list,after)
    if response.status_code != 200 :
        return None
    data = response.json()
    child = data['children']
    for child in children:
        title = child['data']['title']
        hot_list.append(title)
