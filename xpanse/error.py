import logging
from typing import Optional

from requests import Response


class XpanseException(Exception):
    """
    Base exception class.
    """

    def __init__(self, msg: str, response: Response = None):
        self._log = logging.getLogger(
            "{}.{}".format(self.__module__, self.__class__.__name__)
        )
        self.msg = str(msg)
        self.resp = response
        self._log.error(self.msg)

    def __str__(self) -> str:
        return self.msg

    def __repr__(self) -> str:
        return repr(self.__str__())


class UnexpectedValueError(XpanseException):
    """
    An unexpected value error is thrown whenever the value specified for a
    parameter is outside the bounds of what is expected or is missing.
    """

    pass


class UnexpectedResponseError(XpanseException):
    """
    Response from the server was unexpected and requires further investigation.
    """

    pass


class JWTExpiredError(XpanseException):
    """
    JWT has expired.
    """

    pass
