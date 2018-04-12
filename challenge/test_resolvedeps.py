import unittest

from resolvedeps import resolvedeps, resolvetopo


class TestResolveDeps(unittest.TestCase):

    def test_basic(self):
        dmap = {
            'foo': ['bar', 'baz'],
            'bar': ['quux'],
            'baz': [],
            'quux': ['baz']
        }
        result = ['baz', 'quux', 'bar', 'foo']
        self.assertEqual(resolvedeps(dmap), result, 'Basic case')

    def test_invalid_dep(self):
        dmap = {
            'bar': ['qqqq'],
            'quux': [],
        }

        with self.assertRaisesRegex(Exception, 'qqqq'):
            resolvedeps(dmap)

    def test_cyclic(self):
        dmap = {
            'bar': ['baz'],
            'quux': [],
            'baz': ['bar'],
        }
        with self.assertRaisesRegex(Exception, 'Cycle found'):
            resolvedeps(dmap)


class TestResolveTopo(unittest.TestCase):
        def test_basic(self):
            dmap = {
                'foo': ['bar', 'baz'],
                'bar': ['quux'],
                'baz': [],
                'quux': ['baz']
            }
            result = ['baz', 'quux', 'bar', 'foo']
            self.assertEqual(resolvetopo(dmap), result, 'Basic case')

        def test_invalid_dep(self):
            dmap = {
                'bar': ['qqqq'],
                'quux': [],
            }

            with self.assertRaisesRegex(Exception, 'qqq'):
                resolvetopo(dmap)

        def test_cyclic(self):
            dmap = {
                'bar': ['baz'],
                'quux': [],
                'baz': ['bar'],
            }
            with self.assertRaisesRegex(Exception, 'Cycle found'):
                resolvetopo(dmap)
