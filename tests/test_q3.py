from unittest import TestCase
from unittest.mock import mock_open, patch

from parameterized import parameterized

from src.q3_memory import q3_memory
from src.q3_time import q3_time


class TestQ3Memory(TestCase):
    @parameterized.expand(
        [
            (
                "",
                [],
            ),
            (
                '{"content": "Tweet 1", "date": "2023-10-26T10:00:00", "user": {"username": "user1"}, "mentionedUsers": [{"username": "user2"}]}',  # noqa: E501
                [("user2", 1)],
            ),
            (
                '{"content": "Tweet 1", "date": "2023-10-26T10:00:00", "user": {"username": "user1"}, "mentionedUsers": [{"username": "user2"}]}\n'  # noqa: E501
                '{"content": "Tweet 2", "date": "2023-10-27T12:00:00", "user": {"username": "user2"}, "mentionedUsers": [{"username": "user3"}, {"username": "user4"}]}\n'  # noqa: E501
                '{"content": "Tweet 3", "date": "2023-10-27T14:00:00", "user": {"username": "user3"}, "mentionedUsers": [{"username": "user2"}, {"username": "user4"}]}\n'  # noqa: E501
                '{"content": "Tweet 4", "date": "2023-10-27T16:00:00", "user": {"username": "user4"}, "mentionedUsers": [{"username": "user5"}]}\n'  # noqa: E501
                '{"content": "Tweet 5", "date": "2023-10-28T16:00:00", "user": {"username": "user5"}, "mentionedUsers": []}\n',  # noqa: E501
                [("user2", 2), ("user4", 2), ("user3", 1), ("user5", 1)],
            ),
            (
                '{"content": "Tweet 1", "date": "2023-10-01T10:00:00", "user": {"username": "user1"}, "mentionedUsers": [{"username": "user2"}]}\n'  # noqa: E501
                '{"content": "Tweet 2", "date": "2023-10-02T10:00:00", "user": {"username": "user2"}, "mentionedUsers": [{"username": "user3"}]}\n'  # noqa: E501
                '{"content": "Tweet 3", "date": "2023-10-03T10:00:00", "user": {"username": "user3"}, "mentionedUsers": [{"username": "user4"}]}\n'  # noqa: E501
                '{"content": "Tweet 4", "date": "2023-10-04T10:00:00", "user": {"username": "user4"}, "mentionedUsers": [{"username": "user5"}]}\n'  # noqa: E501
                '{"content": "Tweet 5", "date": "2023-10-05T10:00:00", "user": {"username": "user5"}, "mentionedUsers": [{"username": "user6"}]}\n'  # noqa: E501
                '{"content": "Tweet 6", "date": "2023-10-06T10:00:00", "user": {"username": "user6"}, "mentionedUsers": [{"username": "user7"}]}\n'  # noqa: E501
                '{"content": "Tweet 7", "date": "2023-10-07T10:00:00", "user": {"username": "user7"}, "mentionedUsers": [{"username": "user8"}]}\n'  # noqa: E501
                '{"content": "Tweet 8", "date": "2023-10-08T10:00:00", "user": {"username": "user8"}, "mentionedUsers": [{"username": "user9"}]}\n'  # noqa: E501
                '{"content": "Tweet 9", "date": "2023-10-09T10:00:00", "user": {"username": "user9"}, "mentionedUsers": [{"username": "user10"}]}\n'  # noqa: E501
                '{"content": "Tweet 10", "date": "2023-10-10T10:00:00", "user": {"username": "user10"}, "mentionedUsers": [{"username": "user11"}]}\n'  # noqa: E501
                '{"content": "Tweet 11", "date": "2023-10-11T10:00:00", "user": {"username": "user11"}, "mentionedUsers": [{"username": "user2"}]}\n'  # noqa: E501
                '{"content": "Tweet 12", "date": "2023-10-11T10:00:00", "user": {"username": "user11"}, "mentionedUsers": [{"username": "user2"}]}\n'  # noqa: E501
                '{"content": "Tweet 13", "date": "2023-10-11T10:00:00", "user": {"username": "user12"}, "mentionedUsers": [{"username": "user3"}]}\n'  # noqa: E501
                '{"content": "Tweet 14", "date": "2023-10-11T10:00:00", "user": {"username": "user13"}, "mentionedUsers": [{"username": "user2"}, {"username": "user3"}, {"username": "user2"}]}\n',  # noqa: E501
                [
                    ("user2", 5),
                    ("user3", 3),
                    ("user4", 1),
                    ("user5", 1),
                    ("user6", 1),
                    ("user7", 1),
                    ("user8", 1),
                    ("user9", 1),
                    ("user10", 1),
                    ("user11", 1),
                ],
            ),
        ]
    )
    def test_q3_memory(self, file_content, expected_result):
        with patch("builtins.open", mock_open(read_data=file_content)) as _:
            result = q3_memory("dummy_file_path")
            self.assertListEqual(result, expected_result)

            result = q3_time("dummy_file_path")
            self.assertListEqual(result, expected_result)
