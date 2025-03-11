import unittest

from parameterized import parameterized

from src.utils import get_top_10


class TestUtils(unittest.TestCase):
    @parameterized.expand(
        [
            ([], set()),
            (range(1, 12), {2, 3, 4, 5, 6, 7, 8, 9, 10, 11}),
            (
                [
                    324,
                    54,
                    2,
                    234,
                    63,
                    534,
                    2,
                    2345,
                    34,
                    5,
                    76,
                    324,
                    657,
                    98,
                    23,
                    234,
                    18,
                    435,
                    703,
                    1045,
                    3,
                    106238,
                ],
                {106238, 2345, 1045, 703, 657, 534, 435, 324, 234, 98},
            ),
        ]
    )
    def test_get_top_10(self, values, expected_result):
        result = get_top_10(values)
        self.assertSetEqual(result, expected_result)
