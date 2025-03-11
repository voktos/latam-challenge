"""
Helper functions for challenges.
"""

from typing import Iterable, Set


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
