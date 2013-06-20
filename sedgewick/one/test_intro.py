import unittest

import intro


class GCDTestCase(unittest.TestCase):

    def test_basic(self):
        gcd = intro.gcd(10, 2)
        self.assertEqual(gcd, 2)


class RankTestCase(unittest.TestCase):

    def test_key_above_middle(self):
        rank = intro.rank(5, [1, 2, 5, 10])
        self.assertEqual(rank, 2)

    def test_key_below_middle(self):
        rank = intro.rank(3, [1, 2, 3, 7, 9, 10, 11])
        self.assertEqual(rank, 2)

    def test_not_in(self):
        rank = intro.rank(55, [1, 2, 10, 100, 700])
        self.assertEqual(rank, -1)

    def test_too_high(self):
        rank = lambda: intro.rank(10, [1, 2, 3], 0, 700)
        self.assertRaises(ValueError, rank)
