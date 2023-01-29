"""
methods.py

The methods module contains functions that implement
the various actions/verbs used in the HTTP protocol.
"""

from typing import NamedTuple


class Response(NamedTuple):
    status: int


def get(url: str, header: dict = None):
    pass
