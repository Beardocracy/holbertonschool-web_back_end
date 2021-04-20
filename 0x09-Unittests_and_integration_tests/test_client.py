#!/usr/bin/env python3
''' Client unittests '''
import unittest
from unittest.mock import patch, PropertyMock
import client
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    ''' Tests githuborgclient '''
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, test_url, test_mock):
        ''' Docs docs '''
        test_mock.return_value = True
        goc_object = client.GithubOrgClient(test_url)
        self.assertEqual(goc_object.org, True)
        test_mock.assert_called_once()

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    def test_public_repos_url(self, test_org):
        ''' Docstrings '''
        test_url = 'https://api.github.com/orgs/{}/repos'.format(test_org)
        test_payload = {'repos_url': test_url}
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=test_payload)):
            goc_object = client.GithubOrgClient(test_org)
            self.assertEqual(goc_object._public_repos_url, test_url)

    @patch('client.get_json')
    def test_public_repos(self, mock):
        ''' Docstrings '''
        return_value = [{'name': 'google'}, {'name': 'abc'}]
        mock.return_value = return_value
        with patch('client.GithubOrgClient._public_repos_url',
                   PropertyMock(return_value=return_value)) as pub:
            goc_obj = client.GithubOrgClient('test')
            self.assertEqual(goc_obj.public_repos(), ['google', 'abc'])
            mock.assert_called_once()
            pub.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, has_license):
        ''' Docstring docs '''
        goc_obj = client.GithubOrgClient('test')
        self.assertEqual(goc_obj.has_license(repo, license_key), has_license)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    ''' Doc doc docs '''
    @classmethod
    def setUpClass(cls):
        ''' Setup '''
        config = {
            'return_value.json.side_effect': [
                cls.org_payload, cls.repos_payload,
                cls.org_payload, cls.repos_payload
            ]
        }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        ''' teardown '''
        cls.get_patcher.stop()

    def test_public_repos(self):
        ''' Test public repos '''
        goc_obj = client.GithubOrgClient('test')
        self.assertEqual(goc_obj.org, self.org_payload)
        self.assertEqual(goc_obj.repos_payload, self.repos_payload)
        self.assertEqual(goc_obj.public_repos(), self.expected_repos)
        self.assertEqual(goc_obj.public_repos('test'), [])
        self.mock.assert_called()


if __name__ == '__main__':
    unittest.main()
