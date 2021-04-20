#!/usr/bin/env python3
''' Unittests '''
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        ''' Tests access nested map exception '''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    ''' Tests getJson '''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        ''' tests get json '''
        mock = unittest.mock.Mock()
        mock.json.return_value = test_payload
        with patch('requests.get', return_value=mock):
            test_json = get_json(test_url)
            self.assertEqual(test_json, test_payload)


if __name__ == '__main__':
    unittest.main()
