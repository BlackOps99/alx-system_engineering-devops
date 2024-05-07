#!/usr/bin/python3
import requests

"""API Request for get total subscribers"""


def number_of_subscribers(subreddit):
    """return the total subscribers of reddit.com"""

    res = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit),
                       headers={"User-Agent": "My-User-Agent"},
                       allow_redirects=False)

    if res.status_code >= 300:
        return 0

    return res.json().get("data").get("subscribers")
