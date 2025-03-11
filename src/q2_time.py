"""
Challenge 2:
- Get the top 10 most used emojis.
- Mention the count for each of these emojis.
- Optimize execution time.
"""

import re
from collections import Counter
from typing import List, Tuple

from msgspec.json import decode

from schemas import Tweet
from utils import EMOJI_PATTERN


def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Gets the top 10 most used emojis and their counts while optimizing memory
    usage.

    Args:
        file_path: The path to the input file.

    Returns:
        A list of tuples, where each tuple contains an emoji and its
            corresponding count.
    """
    emoji_counter = Counter()
    emoji_pattern = re.compile(EMOJI_PATTERN)

    with open(file_path, encoding="utf-8") as file:
        for line in file:
            tweet = decode(line, type=Tweet)
            tweet_content = tweet.content
            emoji_counter.update(emoji_pattern.findall(tweet_content))

    return emoji_counter.most_common(10)
