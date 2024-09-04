#!/usr/bin/python3
""" Subs """
import requests


def number_of_subscribers(subreddit):
    """
    Queries Reddit Api and returns number of subscribers for given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My Reddit API Client by /u/lelaabk'}
    response = requests.get(url, headers=headers,
                            allow_redirects=False)

    if (not response.ok):
        return 0
    subscribers = response.json().get('data').get('subscribers')
    return subscribers
