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
        raise quest.error.HttpError(url, err.status) from err
    except urllib.error.URLError as err:
        raise quest.error.UrlError(url) from err

    return retv


def post(url: str, headers: dict = None,
         data: dict = None, timeout: int = 10) -> Response:
    if not headers:
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

    encdata = urllib.parse.urlencode(data).encode("UTF-8")
    request = urllib.request.Request(url, headers=headers, data=encdata)

    try:
        with urllib.request.urlopen(request, timeout=10) as resp:
            retv = Response(status=resp.status,
                            body=resp.read())
    except urllib.error.HTTPError as err:
        raise quest.error.HttpError(url, err.status) from err
    except urllib.error.URLError as err:
        raise quest.error.UrlError(url) from err
    except TimeoutError as err:
        raise quest.error.TimeoutError(url) from err

    return retv
