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


class HttpError(Exception):
    def __init__(self, status: int):
        self.status = status
