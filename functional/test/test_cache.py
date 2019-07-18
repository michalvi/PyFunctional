from __future__ import absolute_import

import unittest
from itertools import count, islice

from functional._cache import Cache


class TestCache(unittest.TestCase):

    def setUp(self):
        self.counter = count()
        self.cached = [-1]
        self.cache = Cache(iterable=self.counter, cached=self.cached)

    def test_iteration_extends_the_cached_items(self):
        result = [x for x in islice(self.cache, 2)]

        self.assertListEqual(result, [-1, 0])
        self.assertListEqual(self.cached, [-1, 0])
        self.assertEqual(next(self.counter), 1)

    def test_iterating_twice_gives_the_same_result(self):
        result1 = [x for x in islice(self.cache, 2)]
        result2 = [x for x in islice(self.cache, 2)]

        self.assertListEqual(result1, [-1, 0])
        self.assertListEqual(result2, [-1, 0])

    def test_str_result_looks_similar_to_list(self):
        self.assertEqual(str(Cache(count(), [-1])), '[-1, ...]')
        self.assertEqual(str(Cache(count())), '[...]')

    def test_repr_wraps_str_with_its_name(self):
        self.assertEqual(repr(Cache(count(), [-1])), 'Cache([-1, ...])')
        self.assertEqual(repr(Cache(count())), 'Cache([...])')
