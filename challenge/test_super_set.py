import unittest

import super_set as ss


class TestSuperSet(unittest.TestCase):

    def test_basic_cheat(self):
        result = ss.super_set([1, 2, 3])
        expected = {
            (), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)
        }
        self.assertEqual(result, expected)

    def test_basic_mine(self):
        result = ss.super_set([1, 2, 3], ss.my_combinations)
        expected = {
            (), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)
        }
        self.assertEqual(result, expected)


class TestMyCombinations(unittest.TestCase):

    def test_0(self):
        combinations = tuple(ss.my_combinations('ABCD', 0))
        self.assertEqual(combinations, ((),))

    def test_1(self):
        combinations = set(ss.my_combinations('ASD', 1))
        self.assertEqual(combinations, {('A',), ('S',), ('D',)})

    def test_2(self):
        combinations = set(ss.my_combinations([1, 2, 3], 2))
        self.assertEqual(
            combinations,
            {
                (1, 2),
                (2, 3),
                (1, 3),
            }
        )
