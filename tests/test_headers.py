"""
test_headers.py

Tests for the 'Headers' class found
in the quest.headers module
"""

import unittest
import quest.headers


class TestHeaders(unittest.TestCase):
    def setUp(self):
        self.headers = quest.headers.Headers()

    def test_headers_set_valid(self):
        self.headers.set("key1", "val1")

        self.assertIn("key1", self.headers._headers)
        self.assertEqual(self.headers.get("key1"), "val1")

    def test_headers_set_invalid(self):
        bad_key = 1
        bad_val = ["not", "valid"]

        with self.assertRaises(ValueError) as err_ctx:
            self.headers.set(bad_key, bad_val)
        self.assertIn(bad_key, err_ctx.exception.args)
        self.assertIn(bad_val, err_ctx.exception.args)
