"""
test_methods.py

Tests for the quest.methods module"
"""

import unittest
import quest.methods as methods

_test_url = "https://test.com"


class TestMethods(unittest.TestCase):
    def test_get(self):
        response = methods.get(_test_url)
        self.assertEqual(response.status, 200)
