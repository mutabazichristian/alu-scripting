#!/usr/bin/python3
"""
function that returns the titles of the first 10 hot posts listed for a given subreddit
"""


import requests
subreddit = 'boy'

def top_ten(subreddit):
    url = f'http://reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent':'Mozila/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for [data][children][:10]:
            return ([post][title])

    else:
        return 0