"""
Challenge 3:
- Get the top 10 most mentioned users.
- Mention the count for each of these users.
- Optimize memory usage.
"""

from collections import Counter
from typing import List, Tuple

from msgspec.json import decode

from schemas import Tweet


def q3_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Gets the top 10 most mentioned users and its counts while optimizing
    execution time.

    Args:
        file_path: The path to the input JSON file.

    Returns:
        A list of tuples, where each tuple contains a username and its
            corresponding count.
    """
    username_counter = Counter()

    with open(file_path, encoding="utf-8") as json_file:
        for line in json_file:
            tweet = decode(line, type=Tweet)
            if tweet.mentionedUsers:
                for user in tweet.mentionedUsers:
                    username_counter[user.username] += 1

    return username_counter.most_common(10)
