"""
response. py

The response module contains definitions for the
Response class and various helper functions for
working with Http responses.
"""


class Response():

    def __init__(self, url: str, status: int,
                 headers: dict = {}, content: bytes = b""):
        self._url = url
        self._status = status
        self._headers = headers
        self._content = content

    @property
    def url(self):
        return self._url

    @property
    def status(self):
        return self._status

    @property
    def headers(self, key: str):
        return self._headers.get(key)
