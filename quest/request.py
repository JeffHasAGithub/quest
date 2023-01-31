"""
request.py

The request module contains definitions for the
Request class and various helper functions for
working with Http requests.
"""


class Request():
    def __init__(self, url: str, headers: dict = {},
                 data: dict = {}, timeout: int = 10):
        self._url = url
        self._headers = headers
        self._data = data
        self._timeout = timeout

    @property
    def url(self):
        return self._url

    @property
    def headers(self, key: str):
        return self._headers.get(key)

    @headers.setter
    def headers(self, key: str, val: str):
        self._headers[key] = val

    @property
    def data(self, key: str):
        return self._data.get(key)

    @data.setter
    def data(self, key: str, val: str):
        self._data[key] = val

    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, val: int):
        if not isinstance(val, int):
            val = 10
        self._timeout = val
