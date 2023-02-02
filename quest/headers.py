"""
headers.py

The headers module contains definitions for the
Headers class and various helper functions for
working with the header entries found Http
requests and response.
"""


class Headers():
    def __init__(self):
        self._headers: dict = {}
