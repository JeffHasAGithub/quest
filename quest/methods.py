"""
methods.py

The methods module contains functions that implement
the various actions/verbs used in the HTTP protocol.
"""

from typing import NamedTuple
from urllib.request import urlopen, Request


class Response(NamedTuple):
    status: int
    body: bytes


def get(url: str, headers: dict = None) -> Response:
    if not headers:
        headers = {}

    request = Request(url, headers=headers)
    with urlopen(request) as resp:
        retv = Response(status=resp.status,
                        body=resp.read())

    return retv
