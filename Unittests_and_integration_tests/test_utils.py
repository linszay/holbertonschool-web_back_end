#!/usr/bin/env python3
"""unittesting"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class Test_access_nested_map(unittest.TestCase):
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
