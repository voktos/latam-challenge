from unittest import TestCase
from unittest.mock import mock_open, patch

from parameterized import parameterized

from src.q2_memory import q2_memory
from src.q2_time import q2_time


class TestQ2(TestCase):
    @parameterized.expand(
        [
            (
                "",
                [],
            ),
            (
                '{"content": "Tweet 1 😊", "date": "2023-10-26T10:00:00", "user": {"username": "user1"}, "mentionedUsers": []}',  # noqa: E501
                [("😊", 1)],
            ),
            (
                '{"content": "Tweet 1 😊", "date": "2023-10-26T10:00:00", "user": {"username": "user1"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 2 🎉😊", "date": "2023-10-27T12:00:00", "user": {"username": "user2"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 3 🎉", "date": "2023-10-27T14:00:00", "user": {"username": "user2"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 4 😃", "date": "2023-10-27T16:00:00", "user": {"username": "user3"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 5 🚀", "date": "2023-10-28T16:00:00", "user": {"username": "user4"}, "mentionedUsers": []}\n',  # noqa: E501
                [("😊", 2), ("🎉", 2), ("😃", 1), ("🚀", 1)],
            ),
            (
                '{"content": "Tweet 1 😊", "date": "2023-10-01T10:00:00", "user": {"username": "user1"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 2 🎉", "date": "2023-10-02T10:00:00", "user": {"username": "user2"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 3 😃", "date": "2023-10-03T10:00:00", "user": {"username": "user3"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 4 🚀", "date": "2023-10-04T10:00:00", "user": {"username": "user4"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 5 😇", "date": "2023-10-05T10:00:00", "user": {"username": "user5"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 6 🤣", "date": "2023-10-06T10:00:00", "user": {"username": "user6"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 7 😉", "date": "2023-10-07T10:00:00", "user": {"username": "user7"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 8 ✊", "date": "2023-10-08T10:00:00", "user": {"username": "user8"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 9 😎", "date": "2023-10-09T10:00:00", "user": {"username": "user9"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 10 🤯", "date": "2023-10-10T10:00:00", "user": {"username": "user10"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 11 😊", "date": "2023-10-11T10:00:00", "user": {"username": "user11"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 12 🎉", "date": "2023-10-11T10:00:00", "user": {"username": "user11"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 13 😃", "date": "2023-10-11T10:00:00", "user": {"username": "user12"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 14 🚀😊😊", "date": "2023-10-11T10:00:00", "user": {"username": "user12"}, "mentionedUsers": []}\n',  # noqa: E501
                [
                    ("😊", 4),
                    ("🎉", 2),
                    ("😃", 2),
                    ("🚀", 2),
                    ("😇", 1),
                    ("🤣", 1),
                    ("😉", 1),
                    ("✊", 1),
                    ("😎", 1),
                    ("🤯", 1),
                ],
            ),
        ]
    )
    def test_q2(self, file_content, expected_result):
        with patch("builtins.open", mock_open(read_data=file_content)) as _:
            result = q2_memory("dummy_file_path")
            self.assertListEqual(result, expected_result)

            result = q2_time("dummy_file_path")
            self.assertListEqual(result, expected_result)
