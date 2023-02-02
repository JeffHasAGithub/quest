"""
response. py

The response module contains definitions for the
Response class and various helper functions for
working with Http responses.
"""

import typing


class Response(typing.NamedTuple):
    url: str
    status: int
    headers: dict
    content: bytes
