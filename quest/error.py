"""
error.py

The error module contains class definitions for
exceptions raised by the quest package.
"""


class QuestError(Exception):
    """
    The base class inherited by all
    errors raised within the package.
    """
    def __init___(self, url: str):
        self.url = url


class HttpError(QuestError):
    """
    Raised when bad Http response is received.
    """
    def __init__(self, url: str, status: int):
        super().__init__(url)
        self.status = status


class UrlError(QuestError):
    """
    Raised when bad url is used in Http request.
    """
    def __init__(self, url: str):
        super().__init__(url)


class TimeoutError(QuestError):
    """
    Raised when Http request times out
    """
