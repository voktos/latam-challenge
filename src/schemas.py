"""
Schemas for decoding the JSON file with msgspec.
"""

from msgspec import Struct


class User(Struct):
    username: str


class Tweet(Struct):
    content: str
    date: str
    user: User
    mentionedUsers: list[User] | None = None
