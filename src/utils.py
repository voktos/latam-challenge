"""
Helper constants and functions for challenges.
"""

from typing import Iterable, Set


EMOJI_PATTERN = (
    r"[\U0001F300-\U0001F5FF"  # Miscellaneous Symbols and Pictographs
    r"\U0001F600-\U0001F64F"  # Emoticons
    r"\U0001F680-\U0001F6FF"  # Transport and Map Symbols
    r"\U0001F700-\U0001F77F"  # Alchemical Symbols
    r"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    r"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    r"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    r"\U0001FA00-\U0001FA6F"  # Chess Symbols
    r"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    r"\U00002702-\U000027B0"  # Dingbats
    r"\U0001F004-\U0001F0CF]"  # Mahjong Tiles, Dominoes, Playing Cards
)


def get_top_10(values: Iterable[int]) -> Set[int]:
    """
    Gets the top 10 highest elements in an iterable of integers.

    Args:
        values: The list of values to process.

    Returns:
        A set containing the top 10 most frequent values.
    """
    top_10_values = set()
    for value in values:
        if len(top_10_values) < 10:
            top_10_values.add(value)
        elif value > min(top_10_values):
            top_10_values.remove(min(top_10_values))
            top_10_values.add(value)
    return top_10_values
