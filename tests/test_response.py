"""
test_response.py

Tests for the 'Response' class found
in the quest.response module
"""

import unittest
import quest.response


class TestResponse(unittest.TestCase):
    def setUp(self):
        test_url = "https://test.com"
        test_status = 200
        test_headers = {"header_1": "one header",
                        "header_2": "two header"}
        test_content = b"This is a response body"

        self.response = quest.response.Response(test_url, test_status,
                                                test_headers, test_content)

    def test_headers_valid(self):
        header_1_val = self.response.get_header("header_1")
        header_2_val = self.response.get_header("header_2")

        self.assertEqual(header_1_val, "one header")
        self.assertEqual(header_2_val, "two header")

    def test_headers_invalid(self):
        bad_header_val = self.response.get_header("header_3")
        self.assertIsNone(bad_header_val)

    def test_content_utf8(self):
        default_arg = self.response.get_content()
        with_arg = self.response.get_content("utf-8")

        self.assertEqual(default_arg, "This is a response body")
        self.assertEqual(with_arg, "This is a response body")
