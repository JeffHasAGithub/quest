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
    def __init__(self, url: str):
        self.url = url

    def __str__(self):
        return f"QuestError: {self.url}"

    def __repr__(self):
        return f"<QuestError url='{self.url}'>"


class HttpError(QuestError):
    """
    Raised when bad Http response is received.
    """
    def __init__(self, url: str, status: int):
        super().__init__(url)
        self.status = status

    def __str__(self):
        return f"HttpError: {self.url} - {self.status}"

    def __repr__(self):
        return f"<HttpError url='{self.url}' status={self.status}>"


class UrlError(QuestError):
    """
    Raised when bad url is used in Http request.
    """
    def __init__(self, url: str):
        super().__init__(url)

    def __str__(self):
        return f"UrlError: {self.url}"

    def __repr__(self):
        return f"<UrlError url='{self.url}'>"


class TimeoutError(QuestError):
    """
    Raised when Http request times out
    """
    def __init__(self, url: str):
        super().__init__(url)

    def __str__(self):
        return f"TimeoutError: {self.url}"

    def __repr__(self):
        return f"<TimeoutError url='{self.url}'>"


class HeadersError(ValueError):
    """
    Raised when ValueError is raised by Headers class
    """
    def __init__(self, headers: dict):
        self.headers = headers

    def __str__(self):
        return f"HeadersError: {self.headers}"

    def __repr__(self):
        return f"<HeadersError: headers='{self.headers}'>"
