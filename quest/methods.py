"""
methods.py

The methods module contains functions that implement
the various actions/verbs used in the HTTP protocol.
"""

from typing import NamedTuple


class Response(NamedTuple):
    status: int
