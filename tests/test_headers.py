""" test_headers.py

Tests for the 'Headers' class found
in the quest.headers module
"""

import unittest
import quest.headers


class TestHeaders(unittest.TestCase):
    def setUp(self):
        self.headers = quest.headers.Headers()

    def test_headers_new_valid(self):
        test_headers = {"key1": "val1",
                        "key2": "val2"}

        self.headers = quest.headers.Headers(test_headers)
        self.assertDictEqual(self.headers._headers, test_headers)

    def test_headers_new_invalid(self):
        test_headers = {1: [1, 2, 3],
                        "key2": "val2"}

        with self.assertRaises(ValueError):
            quest.headers.Headers(test_headers)

    def test_headers_set_valid(self):
        key = "key1"
        val = "val1"

        self.headers.set(key, val)

        self.assertIn(key, self.headers._headers)
        self.assertEqual(self.headers.get(key), val)

    def test_headers_set_invalid(self):
        bad_key = 1
        bad_val = ["not", "valid"]

        with self.assertRaises(ValueError) as err_ctx:
            self.headers.set(bad_key, bad_val)
        self.assertIn(bad_key, err_ctx.exception.args)
        self.assertIn(bad_val, err_ctx.exception.args)

    def test_headers_is_valid(self):
        bad_key = 1
        good_key = "key1"
        good_val = "val1"

        self.headers._headers = {bad_key: good_val,
                                 good_key: good_val}

        self.assertFalse(self.headers.is_valid())
