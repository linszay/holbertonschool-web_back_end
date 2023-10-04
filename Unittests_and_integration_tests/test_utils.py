#!/usr/bin/env python3
"""unittesting"""
import unittest
from parameterized import parameterized
import unittest.mock
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


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
        """creating mock object"""
        mock_resp = Mock()
        """setting mock response return value to test_payload"""
        mock_resp.json.return_value = test_payload
        """setting mock response return value to mock_resp"""
        mock_get.return_value = mock_resp
        """checking if the values are the same"""
        self.assertEqual(get_json(test_url), test_payload)
        """assert that mocked get call was only done once"""
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """testing memoize"""
    def test_memoize(self):
        """test memoize function"""
        class TestClass:
            """test class for test_memoize"""
            def a_method(self):
                """method returns 42"""
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        """creating mock method from patch"""
        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_method:
            test = TestClass()
            """testing a_property twice"""
            test_one = test.a_property
            test_two = test.a_property
            """checking if outputs are equal"""
            self.assertEqual(test_one, 42)
            self.assertEqual(test_two, 42)
            """asserting that mock_method is called once"""
            mock_method.assert_called_once()
