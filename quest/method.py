"""
methods.py

The methods module contains functions that implement
the various actions/verbs used in the HTTP protocol.
"""

import typing
import urllib.error
import urllib.parse
import urllib.request
import quest.error


class Response(typing.NamedTuple):
    status: int
    body: bytes


def get(url: str, headers: dict = None) -> Response:
    if not headers:
        headers = {}

    request = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(request) as resp:
            retv = Response(status=resp.status,
                            body=resp.read())
    except urllib.error.HTTPError as err:
        raise quest.error.HttpError(status=err.status) from err
    except urllib.error.URLError as err:
        raise quest.error.UrlError(reason=err.reason) from err

    return retv


def post(url: str, headers: dict = None, data: dict = None) -> Response:
    if not headers:
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

    encdata = urllib.parse.urlencode(data).encode("UTF-8")
    request = urllib.request.Request(url, headers=headers, data=encdata)

    try:
        with urllib.request.urlopen(request) as resp:
            retv = Response(status=resp.status,
                            body=resp.read())
    except urllib.error.HTTPError as err:
        raise quest.error.HttpError(status=err.status) from err

    return retv
