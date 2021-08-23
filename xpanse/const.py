from enum import Enum


class HTTPVerb(Enum):
    """Enums for HTTP verbs"""

    HTTP_GET = "GET"
    """HTTP GET Verb"""

    HTTP_PATCH = "PATCH"
    """HTTP PATCH Verb"""

    HTTP_POST = "POST"
    """HTTP POST Verb"""

    HTTP_PUT = "PUT"
    """HTTP PUT Verb"""

    HTTP_DELETE = "DELETE"
    """HTTP DELETE Verb"""


EXPANSE_BEARER_TOKEN = "EXPANSE_BEARER_TOKEN"
"""Env Variable for Bearer Token"""

EXPANSE_JWT_TOKEN = "EXPANSE_JWT_TOKEN"
"""Env Variable for JWT"""

ID_TOKEN_URL = "api/v1/idtoken"
"""Token Refresh URL"""

V1_PREFIX = "api/v1"
"""V1 URL Prefix"""

V2_PREFIX = "api/v2"
"""V2 URL Prefix"""

V3_PREFIX = "api/v3"
"""V3 URL Prefix"""
