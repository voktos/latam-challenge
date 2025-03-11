"""
Challenge 1:
- Get the top 10 dates that have the most tweets.
- Mention the user (its username) with most tweets for each of these dates.
- Optimize execution time.
"""

from collections import Counter
from datetime import datetime
from typing import List, Tuple

import numpy as np
from msgspec.json import decode

from schemas import Tweet


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Gets the top 10 dates with the most tweets and the user with the most
    posts for each day while optimizing execution time.

    Args:
        file_path: The path to the input JSON file.

    Returns:
        A list of tuples, where each tuple contains a date and its
            corresponding top user.
    """
    tweet_dates = []
    tweet_usernames = []

    with open(file_path, encoding="utf-8") as json_file:
        for line in json_file:
            tweet = decode(line, type=Tweet)
            tweet_date = tweet.date[:10]
            tweet_username = tweet.user.username

            tweet_dates.append(tweet_date)
            tweet_usernames.append(tweet_username)

    tweet_dates = np.array(tweet_dates)
    tweet_usernames = np.array(tweet_usernames)

    top_10_dates = Counter(tweet_dates).most_common(10)

    results = []
    for date, _ in top_10_dates:
        date_usernames = tweet_usernames[
            tweet_dates == date
        ]  # Since tweet_dates and tweet_usernames have the same length we can
        # filter tweets for the specific date by masking tweet_usernames
        # with tweet_dates
        date_usernames, counts = np.unique(date_usernames, return_counts=True)
        top_user = date_usernames[np.argmax(counts)]
        results.append(
            (datetime.strptime(date, "%Y-%m-%d").date(), str(top_user))
        )

    return results
