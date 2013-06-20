import string
import random
import unittest
import timeit

import point2


randstr = lambda n=100: "".join(
    random.choice(string.ascii_letters) for i in range(n))


class Dot6TestCase(unittest.TestCase):

    def setUp(self):

        self.string1 = randstr()
        self.string2 = randstr()
        while point2.is_circular_rotation3(self.string1, self.string2):
            self.string2 = randstr()
        self.rotation1 = point2.random_circular_rotation(self.string1)

    def test_is_rotation(self):
        args = [self.string1, self.rotation1]
        af = lambda: point2.is_circular_rotation(*args)
        bf = lambda: point2.is_circular_rotation2(*args)
        cf = lambda: point2.is_circular_rotation3(*args)
        self.assert_(all([af(), bf(), cf()]))

        at = timeit.Timer(af)
        bt = timeit.Timer(bf)
        ct = timeit.Timer(cf)
        self.assert_(at.timeit(5) > bt.timeit(5) > ct.timeit(5))

    def test_is_not_rotation(self):
        args = [self.string1, self.string2]
        af = lambda: point2.is_circular_rotation(*args)
        bf = lambda: point2.is_circular_rotation2(*args)
        cf = lambda: point2.is_circular_rotation3(*args)
        self.assert_(not any([af(), bf(), cf()]))

        at = timeit.Timer(af)
        bt = timeit.Timer(bf)
        ct = timeit.Timer(cf)
        self.assert_(at.timeit(5) > bt.timeit(5) > ct.timeit(5))

