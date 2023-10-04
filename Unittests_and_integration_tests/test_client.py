#!/usr/bin/env python3
"""tests for client.py"""
import unittest
from parameterized import parameterized
import unittest.mock
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


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
