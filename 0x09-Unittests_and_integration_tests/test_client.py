#!/usr/bin/env python3
''' Client unittests '''
import unittest
import client
from parameterized import parameterized
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    ''' Tests githuborgclient '''
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, test_url, test_mock):
        ''' Docs '''
        test_mock.return_value = True
        goc_object = client.GithubOrgClient(test_url)
        self.assertEqual(goc_object.org, True)
        test_mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
