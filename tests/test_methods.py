"""
test_methods.py

Tests for the quest.methods module"
"""

import unittest
from unittest.mock import Mock, patch
from quest.methods import get, HttpError

_test_url = "https://test.com"
_mock_funcname = "quest.methods.urllib.request.urlopen"


class TestGet(unittest.TestCase):
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

    def test_get_404(self):
        mock_ctx = self.mock_urlopen.return_value.__enter__
        mock_ctx.side_effect = HttpError(status=404)

        with self.assertRaises(HttpError) as err_ctx:
            get(_test_url)

        self.assertEqual(err_ctx.exception.status, 404)


class TestPost(unittest.TestCase):
    def setUp(self):
        self.mock_urlopen_patch = patch(_mock_funcname)
        self.mock_urlopen = self.mock_urlopen_patch.start()
