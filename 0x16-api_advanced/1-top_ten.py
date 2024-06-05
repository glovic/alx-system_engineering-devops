#!/usr/bin/python3

"""
    This module contains the function top 10 posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """Returns the titles of the top ten posts for a given subreddit."""
    
    # Validate subreddit name
    if not subreddit or not subreddit.isalnum():
        print("Invalid subreddit name:", subreddit)
        return []
    
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "MyRedditClient/1.0 (by /u/victorglo)"
    }
    params = {"limit": 10}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    data = response.json().get("data")
    titles = [post.get("data").get("title") for post in data.get("children")]
        
    return titles

# Example usage:
if __name__ == "__main__":
    subreddit = "python"
    top_posts = top_ten(subreddit)
    print("Top 10 posts in r/{}:".format(subreddit))
    for idx, post in enumerate(top_posts, start=1):
        print(f"{idx}. {post}")

