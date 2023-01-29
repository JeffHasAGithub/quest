"""
methods.py

The methods module contains functions that implement
the various actions/verbs used in the HTTP protocol.
"""

import typing
import urllib.error
import urllib.request


class HttpError(Exception):
    """HTTP error"""


class Response(typing.NamedTuple):
    status: int
    body: bytes


def get(url: str, headers: dict = None) -> Response:
    if not headers:
        headers = {}

    request = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(request) as resp:
        retv = Response(status=resp.status,
                        body=resp.read())

    return retv
