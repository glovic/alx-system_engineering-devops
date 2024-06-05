#!/usr/bin/python3

"""
    This module contains the function top 10 posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
     """Returns the titles to top ten posts for a given subreddit"""
     url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
     header = {
             "User-Agent": "MyRedditClient/1.0 (by /u/victorglo)"
             }
     params = {"limit": 10}
     response = requests.get(url,headers=headers, params=params, allow_redirects=False)
     if response.status_code == 404:
         print("None")
         return
     results = response.json().get("data")
     [print(c.get("data").get("title")) for c in results.get("children")]
