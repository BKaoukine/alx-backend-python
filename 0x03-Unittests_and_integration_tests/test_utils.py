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
from utils import access_nested_map
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
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


if __name__ == '__main__':
    unittest.main()
