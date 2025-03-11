"""
Challenge 1:
- Get the top 10 dates that have the most tweets.
- Mention the user (its username) with most tweets for each of these dates.
- Optimize memory usage.
"""

from datetime import datetime
from json import loads
from typing import List, Tuple

from utils import get_top_10


def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Gets the top 10 dates with the most tweets and the user with the most
    posts for each day while optimizing memory usage.

    Args:
        file_path: The path to the input JSON file.

    Returns:
        A list of tuples, where each tuple contains a date and its
            corresponding top user.
    """
    date_counts = {}
    user_counts = {}
    with open(file_path, encoding="utf-8") as json_file:
        for line in json_file:
            tweet = loads(line)
            tweet_date = tweet["date"][:10]
            tweet_username = tweet["user"]["username"]

            date_counts.setdefault(tweet_date, 0)
            user_counts.setdefault(tweet_date, {})
            user_counts[tweet_date].setdefault(tweet_username, 0)

            date_counts[tweet_date] += 1
            user_counts[tweet_date][tweet_username] += 1

    top_10_counts = get_top_10(date_counts.values())
    date_counts = {k: v for k, v in date_counts.items() if v in top_10_counts}

    return [
        (
            datetime.strptime(tweet_date, "%Y-%m-%d").date(),
            max(user_counts[tweet_date], key=user_counts[tweet_date].get),
        )
        for tweet_date, _ in sorted(
            date_counts.items(),
            key=lambda x: x[1],
            reverse=True,
        )[
            :10
        ]  # This slice is here in case len(date_counts) > 10, wich can
        # happen if there are multiple dates with the same count and
        # that count is among the top 10 counts
    ]
