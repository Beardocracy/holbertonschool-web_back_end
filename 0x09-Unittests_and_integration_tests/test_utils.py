#!/usr/bin/env python3
''' Unittests '''
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    ''' Unittests '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, map):
        ''' Tests access nested map '''
        self.assertEqual(access_nested_map(nested_map, path), map)


if __name__ == '__main__':
    unittest.main()