#!/usr/bin/python3
"""
function that returns the titles of the first 10 hot posts listed for a given subreddit
"""


import requests

def top_ten(subreddit):
    """some stuff"""
    url = f'http://reddit.com/r/{subreddit}/hot.json'
    """some other stuff"""
    headers = {'User-Agent':'Mozila/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children'][:10]:
            print(post['data']['title'])

    else:
        print('None')