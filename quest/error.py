"""
error.py

The error module contains class definitions for
exceptions raised by the quest package.
"""


class QuestError(Exception):
    """
    The abstract base class inherited by
    all errors raised within the package.
    """


class HttpError(QuestError):
    """
    Raised when bad Http response is received.
    """
    def __init__(self, status: int):
        self.status = status


class UrlError(QuestError):
    """
    Raised when bad url is used in Http request.
    """
    def __init__(self, reason):
        self.reason = reason


class TimeoutError(QuestError):
    """
    Raised when Http request times out
    """
