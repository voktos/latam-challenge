"""
Challenge 2:
- Get the top 10 most used emojis.
- Mention the count for each of these emojis.
- Optimize memory usage.
"""

from re import findall
from json import loads
from typing import List, Tuple

from utils import EMOJI_PATTERN, get_top_10


def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Gets the top 10 most used emojis and its counts while optimizing memory
    usage.

    Args:
        file_path: The path to the input JSON file.

    Returns:
        A list of tuples, where each tuple contains an emoji and its
            corresponding count.
    """
    emoji_counts = {}
    with open(file_path, encoding="utf-8") as json_file:
        for line in json_file:
            line = loads(line)["content"]
            for emoji in findall(EMOJI_PATTERN, line):
                emoji_counts.setdefault(emoji, 0)
                emoji_counts[emoji] += 1

    top_10_counts = get_top_10(emoji_counts.values())
    emoji_counts = {
        k: v for k, v in emoji_counts.items() if v in top_10_counts
    }

    return sorted(emoji_counts.items(), key=lambda x: x[1], reverse=True)[
        :10
    ]  # Same consideration here as in q1_memory
