"""
test_methods.py

Tests for the quest.methods module"
"""

import unittest
from unittest.mock import Mock, patch
from quest.methods import get

_test_url = "https://test.com"
_mock_funcname = "quest.methods.urlopen"


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.mock_urlopen_patch = patch(_mock_funcname)
        self.mock_urlopen = self.mock_urlopen_patch.start()

    def test_get_200(self):
        mock_retv = self.mock_urlopen.return_value.__enter__.return_value
        mock_retv.status = 200
        mock_retv.read.return_value = b"Hello!"

        response = get(_test_url)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.body, b"Hello!")
