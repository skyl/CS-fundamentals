
import unittest

import mountain_rainfall as mr


class TestMountainRainfall(unittest.TestCase):

    def test_basic(self):
        land = [
            [1, 0, 2, 5, 8],
            [2, 3, 4, 7, 9],
        ]

        result = {
            (0, 1): 10,
        }

        self.assertEqual(mr.mountain_rainfall(land), result)

    def test_bigger_example_with_ties(self):
        landscape = [
            [9, 9, 0, 8, 9, 7],
            [1, 3, 1, 3, 1, 3],
            [0, 9, 8, 7, 6, 5],
            [0, 1, 2, 3, 4, 5],
        ]
        result = {
            (0, 2): 7,
        }
        result = {
            (0, 2): 8,
            (1, 4): 6,
            (2, 0): 9,
            (3, 0): 1,
        }
        self.assertEqual(mr.mountain_rainfall(landscape), result)

    def test_that_would_have_caught_missing_neighbor(self):
        land = [
            [1, 1, 1],
            [0, 0, 1],
            [-1, 1, 2],
        ]
        result = {
            (2, 0): 9,
        }
        self.assertEqual(mr.mountain_rainfall(land), result)


class TestWhoIsLowest(unittest.TestCase):

    def test_basic(self):
        land = [
            [1, 1, 1],
            [1, 0, 1],
            [0, -5, 0],
        ]
        self.assertEqual(mr.who_is_lowest(0, 0, land), (1, 1))
        self.assertEqual(mr.who_is_lowest(1, 1, land), (2, 1))
