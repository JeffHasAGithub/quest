"""
test_methods.py

Tests for the quest.methods module"
"""

import unittest
from unittest.mock import Mock, patch
from urllib.error import URLError, HTTPError
from quest.method import get, post
from quest.error import UrlError, HttpError

_test_url = "https://test.com"
_mock_funcname = "quest.methods.urllib.request.urlopen"


class TestGet(unittest.TestCase):
    def setUp(self):
        self.mock_urlopen_patch = patch(_mock_funcname)
        self.mock_urlopen = self.mock_urlopen_patch.start()

    def test_get_200(self):
        mock_retv = self.mock_urlopen.return_value.__enter__.return_value
        mock_retv.status = 200

        response = get(_test_url)
        self.assertEqual(response.status, 200)

    def test_get_404(self):
        mock_ctx = self.mock_urlopen.return_value.__enter__
        mock_ctx.side_effect = HTTPError(url=_test_url, code=404,
                                         hdrs=None, msg=None, fp=None)

        with self.assertRaises(HttpError) as err_ctx:
            get(_test_url)

        self.assertEqual(err_ctx.exception.status, 404)

    def test_get_bad_url(self):
        mock_ctx = self.mock_urlopen.return_value.__enter__
        mock_ctx.side_effect = URLError(reason="bad url")

        with self.assertRaises(UrlError):
            get(_test_url)


class TestPost(unittest.TestCase):
    def setUp(self):
        self.mock_urlopen_patch = patch(_mock_funcname)
        self.mock_urlopen = self.mock_urlopen_patch.start()

    def test_post_200(self):
        mock_retv = self.mock_urlopen.return_value.__enter__.return_value
        mock_retv.status = 200

        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {"Name": "Jeff", "State": "Texas"}

        response = post(_test_url, headers=headers, data=data)
        self.assertEqual(response.status, 200)

    def test_post_404(self):
        mock_ctx = self.mock_urlopen.return_value.__enter__
        mock_ctx.side_effect = HTTPError(url=_test_url, code=404,
                                         hdrs=None, msg=None, fp=None)

        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {"Name": "Jeff", "State": "Texas"}

        with self.assertRaises(HttpError) as err_ctx:
            post(_test_url, headers=headers, data=data)

        self.assertEqual(err_ctx.exception.status, 404)
