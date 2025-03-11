"""
Challenge 3:
- Get the top 10 most mentioned users.
- Mention the count for each of these users.
- Optimize memory usage.
"""

from json import loads
from typing import List, Tuple

from utils import get_top_10


def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Gets the top 10 most mentioned users and its counts while optimizing
    memory usage.

    Args:
        file_path: The path to the input JSON file.

    Returns:
        A list of tuples, where each tuple contains a username and its
            corresponding count.
    """
    username_counts = {}

    with open(file_path, encoding="utf-8") as json_file:
        for line in json_file:
            line = loads(line)
            if line["mentionedUsers"]:
                for user in line["mentionedUsers"]:
                    username_counts.setdefault(user["username"], 0)
                    username_counts[user["username"]] += 1

    top_10_counts = get_top_10(username_counts.values())
    username_counts = {
        k: v for k, v in username_counts.items() if v in top_10_counts
    }

    return sorted(username_counts.items(), key=lambda x: x[1], reverse=True)[
        :10
    ]  # Same consideration here as in q1_memory
