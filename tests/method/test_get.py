"""
test_get.py

Tests for the 'get' function found
in the quest.method module
"""

import unittest
import unittest.mock
import urllib.error
import quest.error
import quest.method

from .common import _test_url, _mock_funcname

class TestGet(unittest.TestCase):
    def setUp(self):
        self.mock_urlopen_patch = unittest.mock.patch(_mock_funcname)
        self.mock_urlopen = self.mock_urlopen_patch.start()

    def test_get_200(self):
        mock_retv = self.mock_urlopen.return_value.__enter__.return_value
        mock_retv.status = 200

        response = quest.method.get(_test_url)
        self.assertEqual(response.status, 200)

    def test_get_404(self):
        mock_ctx = self.mock_urlopen.return_value.__enter__
        mock_ctx.side_effect = urllib.error.HTTPError(url=_test_url, code=404,
                                                      hdrs=None, msg=None,
                                                      fp=None)

        with self.assertRaises(quest.error.HttpError) as err_ctx:
            quest.method.get(_test_url)

        self.assertEqual(err_ctx.exception.status, 404)

    def test_get_bad_url(self):
        mock_ctx = self.mock_urlopen.return_value.__enter__
        mock_ctx.side_effect = urllib.error.URLError(reason="bad url")

        with self.assertRaises(quest.error.UrlError):
            quest.method.get(_test_url)

    def test_get_timeout(self):
        mock_ctx = self.mock_urlopen.return_value.__enter__
        mock_ctx.side_effect = TimeoutError()

        with self.assertRaises(quest.error.TimeoutError):
            quest.method.get(_test_url)
