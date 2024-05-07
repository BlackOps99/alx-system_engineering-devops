#!/usr/bin/python3
"""API Request for get total subscribers"""

import requests


def number_of_subscribers(subreddit):
    """return the total subscribers of reddit.com"""

    res = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit),
                       headers={"User-Agent": "My-Agent"})

    if res.status_code != 200:
        return 0

    return res.json().get("data").get("subscribers")
