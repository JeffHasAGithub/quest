"""
test_post.py

Tests for the 'post' function found
in the quest.method module
"""

import unittest
import unittest.mock
import urllib.error
import quest.error
import quest.method

from .common import _test_url, _mock_funcname


class TestPost(unittest.TestCase):
    def setUp(self):
        self.mock_urlopen_patch = unittest.mock.patch(_mock_funcname)
        self.mock_urlopen = self.mock_urlopen_patch.start()

        self.headers = {"Content-Type": "application/x-www-form-urlencoded"}
        self.data = {"Name": "Jeff", "State": "Texas"}

    def test_post_200(self):
        mock_retv = self.mock_urlopen.return_value.__enter__.return_value
        mock_retv.status = 200

        response = quest.method.post(_test_url, headers=self.headers,
                                     data=self.data)
        self.assertEqual(response.status, 200)

    def test_post_404(self):
        mock_ctx = self.mock_urlopen.return_value.__enter__
        mock_ctx.side_effect = urllib.error.HTTPError(url=_test_url, code=404,
                                                      hdrs=None, msg=None,
                                                      fp=None)

        with self.assertRaises(quest.error.HttpError) as err_ctx:
            quest.method.post(_test_url, headers=self.headers, data=self.data)

        self.assertEqual(err_ctx.exception.status, 404)

    def test_post_bad_url(self):
        mock_ctx = self.mock_urlopen.return_value.__enter__
        mock_ctx.side_effect = urllib.error.URLError(reason="bad url")

        with self.assertRaises(quest.error.UrlError):
            quest.method.post(_test_url, headers=self.headers, data=self.data)

    def test_post_timeout(self):
        mock_ctx = self.mock_urlopen.return_value.__enter__
        mock_ctx.side_effect = TimeoutError()

        with self.assertRaises(quest.error.TimeoutError):
            quest.method.post(_test_url, headers=self.headers, data=self.data)
