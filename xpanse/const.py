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


class AssetType(Enum):
    """Enums for Asset Types"""

    DOMAIN = "domain"
    """Domain Type"""

    CERTIFICATE = "certificate"
    """Certificate Type"""

    RESPONSIVE_IP = "unassociated_responsive_ip"
    """Unassociated Responsive IP Type"""

    CLOUD_RESOURCES = "cloud_compute_instance"
    """"Cloud Compute Instance Type"""

    PRISMA_CLOUD_RESOURCE = "cloud_integration"
    """"Cloud Integration Type"""


class TaggableDataType(Enum):
    ASSETS = "assets_internet_exposure"
    """Asset Data Type for Tag Management"""

    EXTERNAL_IP_RANGES = "external_ip_address_ranges"
    """Asset Data Type for Tag Management"""


class PublicApiFields:
    """Keys for PAPI Requests and Responses"""

    REQUEST_DATA = "request_data"
    """Common Field For Providing Request Data"""

    FILTERS = "filters"
    """Common Field For Providing Request Data"""

    TAGS = "tags"
    """Common Field For Providing Request Data"""

    SEARCH_FROM = "search_from"
    """Common Field For Query Offset"""

    SEARCH_TO = "search_to"
    """Common Field For Calculating Query Limit"""

    USE_PAGE_TOKEN = "use_page_token"
    """Common Field To Use Pagination"""

    REPLY = "reply"
    """Common Top-Level Response Key"""

    NEXT_PAGE_TOKEN = "next_page_token"
    """Common Pagination Token Field"""

    TOTAL_COUNT = "total_count"
    """Common Field for Total Results Count - Limit is 9,999"""

    RESULTS_COUNT = "results_count"
    """Common Field for Page Size Count"""


DEFAULT_REQUEST_PAYLOAD_FIELD = "json"
"""Default Parameter Used by the Requests Library for the Payload"""

CORTEX_FQDN = "CORTEX_FQDN"
"""Env Variable for API Host (Fully Qualified Domain Name)"""

CORTEX_API_KEY_ID = "CORTEX_API_KEY_ID"
"""Env Variable for Cortex Public API Key ID"""

CORTEX_API_KEY = "CORTEX_API_KEY"
"""Env Variable for Cortex Public API Key"""

V1_PREFIX = "public_api/v1"
"""V1 URL Prefix"""

V2_PREFIX = "public_api/v2"
"""V2 URL Prefix"""
