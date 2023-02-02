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