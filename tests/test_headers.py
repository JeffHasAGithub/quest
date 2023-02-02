"""
test_headers.py

Tests for the 'Headers' class found
in the quest.headers module
"""

import unittest
import quest.headers


class TestHeaders(unittest.TestCase):
    def test_headers_set_valid(self):
        headers = quest.headers.Headers()
        headers.set("key1", "val1")

        self.assertIn("key1", headers._headers)
        self.assertEqual(headers.get("key1"), "val1")
