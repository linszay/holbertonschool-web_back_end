#!/usr/bin/env python3
"""unittesting"""
import unittest
from parameterized import parameterized
import unittest.mock
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """unittesting access_nested_map"""
    """@parameterized.expand shows a tuple of list cases"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """checks nested_map and path result against expected result"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_exception_message):
        """testing with assertRaises context manager"""
        with self.assertRaises(expected_exception_message):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """unittesting get_json"""
    @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ])
    @patch('utils.requests.get')
    def test_get_json(self, test_payload, test_url, mock_get):
        """testing if get_json returns expected result"""
        mock_resp = Mock()
        mock_resp.json.return_value = test_payload
        mock_get.return_value = mock_resp
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)
