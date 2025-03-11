from datetime import date
from unittest import TestCase
from unittest.mock import mock_open, patch

from parameterized import parameterized

from src.q1_memory import q1_memory
from src.q1_time import q1_time


class TestQ1(TestCase):
    @parameterized.expand(
        [
            (
                "",
                [],
            ),
            (
                '{"content": "Tweet 1", "date": "2023-10-26T10:00:00", "user": {"username": "user1"}, "mentionedUsers": []}',  # noqa: E501
                [(date(2023, 10, 26), "user1")],
            ),
            (
                '{"content": "Tweet 1", "date": "2023-10-26T10:00:00", "user": {"username": "user1"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 2", "date": "2023-10-27T12:00:00", "user": {"username": "user2"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 3", "date": "2023-10-27T14:00:00", "user": {"username": "user2"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 4", "date": "2023-10-27T16:00:00", "user": {"username": "user3"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 5", "date": "2023-10-28T16:00:00", "user": {"username": "user4"}, "mentionedUsers": []}\n',  # noqa: E501
                [
                    (date(2023, 10, 27), "user2"),
                    (date(2023, 10, 26), "user1"),
                    (date(2023, 10, 28), "user4"),
                ],
            ),
            (
                '{"content": "Tweet 1", "date": "2023-10-01T10:00:00", "user": {"username": "user1"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 2", "date": "2023-10-02T10:00:00", "user": {"username": "user2"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 3", "date": "2023-10-03T10:00:00", "user": {"username": "user3"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 4", "date": "2023-10-04T10:00:00", "user": {"username": "user4"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 5", "date": "2023-10-05T10:00:00", "user": {"username": "user5"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 6", "date": "2023-10-06T10:00:00", "user": {"username": "user6"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 7", "date": "2023-10-07T10:00:00", "user": {"username": "user7"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 8", "date": "2023-10-08T10:00:00", "user": {"username": "user8"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 9", "date": "2023-10-09T10:00:00", "user": {"username": "user9"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 10", "date": "2023-10-10T10:00:00", "user": {"username": "user10"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 11", "date": "2023-10-11T10:00:00", "user": {"username": "user11"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 12", "date": "2023-10-11T10:00:00", "user": {"username": "user11"}, "mentionedUsers": []}\n'  # noqa: E501
                '{"content": "Tweet 13", "date": "2023-10-11T10:00:00", "user": {"username": "user12"}, "mentionedUsers": []}\n',  # noqa: E501
                [
                    (date(2023, 10, 11), "user11"),
                    (date(2023, 10, 1), "user1"),
                    (date(2023, 10, 2), "user2"),
                    (date(2023, 10, 3), "user3"),
                    (date(2023, 10, 4), "user4"),
                    (date(2023, 10, 5), "user5"),
                    (date(2023, 10, 6), "user6"),
                    (date(2023, 10, 7), "user7"),
                    (date(2023, 10, 8), "user8"),
                    (date(2023, 10, 9), "user9"),
                ],
            ),
        ]
    )
    def test_q1(self, file_content, expected_result):
        with patch("builtins.open", mock_open(read_data=file_content)) as _:
            result = q1_memory("dummy_file_path")
            self.assertListEqual(result, expected_result)

            result = q1_time("dummy_file_path")
            self.assertListEqual(result, expected_result)
