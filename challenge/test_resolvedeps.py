import unittest

from resolvedeps import resolvedeps


class TestResolveDeps(unittest.TestCase):

    def test_basic(self):
        map = {
            'foo': ['bar', 'baz'],
            'bar': ['quux'],
            'baz': [],
            'quux': ['baz']
        }
        result = ['baz', 'quux', 'bar', 'foo']
        self.assertEqual(resolvedeps(map), result, 'Basic case')

    def test_invalid_dep(self):
        map = {
            'bar': ['qqqq'],
            'quux': [],
        }

        with self.assertRaisesRegex(Exception, 'qqqq'):
            resolvedeps(map)
