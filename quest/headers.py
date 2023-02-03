"""
headers.py

The headers module contains definitions for the
Headers class and various helper functions for
working with the header entries found Http
requests and response.
"""


class Headers():
    def __init__(self, headers: dict = {}):
        self._headers = headers
        if not self.is_valid():
            raise ValueError

    def get(self, key: str):
        return self._headers.get(key)

    def set(self, key: str, val: str):
        if not _valid_kvpair(key, val):
            raise ValueError(key, val)
        self._headers[key] = val

    def is_valid(self) -> bool:
        return not any(((k, v) for k, v in self._headers.items()
                        if not _valid_kvpair(k, v)))


def _valid_string(string: any) -> bool:
    return isinstance(string, str)


def _valid_kvpair(key: any, val: any) -> bool:
    return _valid_string(key) and _valid_string(val)
