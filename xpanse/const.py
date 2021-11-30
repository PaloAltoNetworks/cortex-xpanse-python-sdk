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


XPANSE_CLIENT_ID = "XPANSE_CLIENT_ID"
"""Env Variable for Client ID"""

XPANSE_CLIENT_SECRET = "XPANSE_CLIENT_SECRET"
"""Env Variable for Client Secret"""

XPANSE_BEARER_TOKEN = "XPANSE_BEARER_TOKEN"
"""Env Variable for Bearer Token"""

XPANSE_JWT_TOKEN = "XPANSE_JWT_TOKEN"
"""Env Variable for JWT"""

CLIENT_CREDENTIALS_TOKEN_URL = "api/oauth2/RequestToken"
"""Token Refresh URL for Client Credentials"""

CLIENT_CREDENTIALS_SCOPE = "scope-xpanse"
"""Scope for Client Credentials"""

CLIENT_CREDENTIALS_GRANT_TYPE = "client_credentials"
"""Grant Type for Client Credentials"""

ID_TOKEN_URL = "api/v1/idtoken"
"""Token Refresh URL for Bearer token"""

V1_PREFIX = "api/v1"
"""V1 URL Prefix"""

V2_PREFIX = "api/v2"
"""V2 URL Prefix"""

V3_PREFIX = "api/v3"
"""V3 URL Prefix"""
