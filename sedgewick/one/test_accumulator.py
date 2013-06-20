import unittest

import accumulator


class AccumulatorTestCase(unittest.TestCase):

    def test_add_value(self):
        acc = accumulator.Accumulator()
        acc.add_value(5)
        acc.add_value(10)
        acc.add_value(15)
        self.assertEqual(acc.total, 30)
        self.assertEqual(acc.N, 3)

    def test_mean(self):
        acc = accumulator.Accumulator()
        acc.add_value(10)
        acc.add_value(10)
        acc.add_value(20)
        acc.add_value(20)
        self.assertEqual(acc.mean(), 15)

    def test_str(self):
        acc = accumulator.Accumulator()
        acc.add_value(999)
        s = str(acc)
        self.assertIn("999", s)
        self.assertIn("1", s)
