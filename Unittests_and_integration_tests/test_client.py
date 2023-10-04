#!/usr/bin/env python3
"""tests for client.py"""
import unittest
from parameterized import parameterized
import unittest.mock
from unittest.mock import patch, Mock
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
        client = GithubOrgClient(orgss)
        expected_result = {"name": orgss, "description": "Mocked description"}
        """setting mock response return value"""
        mock_get_json.return_value = expected_result
        new_org_client = GithubOrgClient(orgss)
        """call org method and check if results are equal"""
        result = new_org_client.org
        self.assertEqual(result, expected_result)
        """assert that get_json was only called once"""
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{orgss}")

