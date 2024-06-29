#!/usr/bin/env python3
"""
Unit tests for the utils.access_nested_map function.

This script defines a TestAccessNestedMap class.
that contains unit tests for theaccess_nested_map function.
from the utils module. It uses the unittest framework.
and the parameterized library to test the function with.
different sets of inputs
and expected outputs.

Classes:
    TestAccessNestedMap

Functions:
    TestAccessNestedMap.test_access_nested_map

Example:
    To run the tests, use the following command:

        python -m unittest test_access_nested_map.py

"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
)

from utils import (
    access_nested_map,
    get_json
)


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit test class for the access_nested_map function.

    Methods:
        test_access_nested_map: Tests the access_nested_map function with
                                various nested maps and paths.
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), 2),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Tests the access_nested_map function from the utils module.

        Args:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The tuple of keys representing the path to the value.
            expected: The expected value at the end of the path.

        Asserts:
            The value obtained from the access_nested_map function is equal to
            the expected value.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError)
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path, exception):
        """
        Test access_nested_map function for cases.
        that should raise an exception.

        Args:
            nested_map (Mapping): The nested dictionary to access.
            path (Sequence): The tuple of keys representing.
            the path to the value.
            expected (type): The type of exception expected to be raised.

        Asserts:
            Asserts that the access_nested_map function
            raises the expected exception
            when called with the given nested_map and path.
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Unit test class for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json function with different URLs and payloads."""
        with patch('utils.requests.get') as mock_get:
            # Create a mock response object with a json method
            # returning test_payload
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call get_json with the test_url
            result = get_json(test_url)

            # Check that requests.get was called once with the test_url
            mock_get.assert_called_once_with(test_url)

            # Check that the result of get_json is equal to test_payload
            self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
