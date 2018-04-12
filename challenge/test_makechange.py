import unittest

from makechange import makechange


class TestMakeChange(unittest.TestCase):

    def test_basic_make_change(self):
        change = makechange(35)
        self.assertEqual(change[25], 1, '1 quarter')
        self.assertEqual(change[10], 1, '1 dime')
        self.assertEqual(len(change.keys()), 2, 'Two types of coins')

    def test_weird_coin_system(self):
        change = makechange(22, [1, 3, 7])
        self.assertEqual(change[7], 3, '3 7 pieces')
        self.assertEqual(change[1], 1, '1 cent')
        self.assertEqual(len(change.keys()), 2, 'Two types')
