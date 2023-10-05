#!/usr/bin/env python3
"""tests for client.py"""
import unittest
from parameterized import parameterized, parameterized_class
import unittest.mock
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """unittesting"""
    """use patch to make sure get_json is called once"""
    @parameterized.expand({
        ("google",),
        ("abc",)
    })
    @patch('client.get_json')
    def test_org(self, orgss, mock_get_json):
        expected_result = {"name": orgss, "description": "Mocked description"}
        """setting mock response return value"""
        mock_get_json.return_value = expected_result
        new_org_client = GithubOrgClient(orgss)
        """call org method and check if results are equal"""
        result = new_org_client.org
        self.assertEqual(result, expected_result)
        """assert that get_json was only called once"""
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{orgss}")

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """testing GithubOrgClient._public_repos_url"""
        """using PropertyMock to mock a property"""
        """setting expected return value"""
        test_org_result = {'repos_url': 'https://api.github.com/orgs/test_orgs/repos'}
        mock_org.return_value = test_org_result
        """setting new_org_client to the mocked property"""
        new_org_client = GithubOrgClient('test_repo')
        """checking is result is equal"""
        self.assertEqual(new_org_client._public_repos_url, 'https://api.github.com/orgs/test_orgs/repos')

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Unit test for GithubOrgClient.public_repos"""
        expected_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
        ]
        """mock _public_repos_url property to return a URL"""
        mock_public_repos_url.return_value = \
            "https://api.github.com/orgs/test_org/repos"
        """mock get_json to return the expected payload"""
        mock_get_json.return_value = expected_payload
        """creating an instance of GithubOrgClient"""
        org_name = "test_org"
        client = GithubOrgClient(org_name)
        """calling public_repos method"""
        repos = client.public_repos()
        """assert that the mocked property was only called once"""
        mock_public_repos_url.assert_called_once()
        """assert that get_json was called once with the expected URL"""
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/test_org/repos")
        """assert that result is what you expect for the payload"""
        expected_repos = ["repo1", "repo2"]
        self.assertEqual(repos, expected_repos)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """Moreeee unit test for GithubOrgClient.has_license"""
        client = GithubOrgClient("test_org")
        """call has_license with the provided input"""
        result = client.has_license(repo, license_key)
        """checking if the result is equal"""
        self.assertEqual(result, expected_result)

class TestIntegrationGithubOrgClient(unittest.TestCase):
    """class contains setup and teardown"""
    @parameterized_class(("org_payload", "repos_payload", "expected_repos", "apache2_repos"), [
        (org_payload, repos_payload, expected_repos, apache2_repos),
        ])
    @classmethod
    def setUpClass(cls):
        """mock requests.get to return example payloads"""
        cls.get_patcher = patch('requests.get')
        """mock requests.get side_effect to return URL payloads"""
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = [
            mock_response(org_payload),
            mock_response(repos_payload),
            mock_response(apache2_repos),
        ]

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Integration test for GithubOrgClient.public_repos"""
        client = GithubOrgClient(self.org_payload["name"])
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)
