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

    OWNED_RESPONSIVE_IP = "unassociated_responsive_ip"
    """Unassociated Responsive IP Type"""

    CLOUD_RESOURCES = "cloud_compute_instance"
    """"Cloud Compute Instance Type"""

    PRISMA_CLOUD_RESOURCE = "cloud_integration"
    """"Cloud Integration Type"""


class TaggableDataType(Enum):
    ASSETS = "assets_internet_exposure"
    """Asset Data Type for AT Tag Management"""

    OWNED_IP_RANGES = "external_ip_address_ranges"
    """Owned IP Range Data Type for IPR Tag Management"""


class FilterOperator(Enum):
    """Enum for Filter Operators"""

    EQ = "eq"
    """Equals"""

    NEQ = "neq"
    """Not Equals"""

    GTE = "gte"
    """Greater Than or Equal To"""

    LTE = "lte"
    """Less Than or Equal To"""

    IN = "in"
    """Includes"""

    NIN = "nin"
    """Not Includes"""

    CONTAINS = "contains"
    """Contains"""

    NOT_CONTAINS = "not_contains"
    """Not Contains"""


class SortOrder(Enum):
    """Enum for Sort Order"""

    ASC = "asc"
    """Ascending"""

    DESC = "desc"
    """Descending"""


class PublicApiFields:
    """Keys for PAPI Requests and Responses"""

    REQUEST_DATA = "request_data"
    """Common Field For Providing Request Data"""

    FILTERS = "filters"
    """Common Field For Providing Request Data"""

    FIELD = "field"
    """Common Field For Providing Request Data"""

    OPERATOR = "operator"
    """Common Field For Filter Operator in Request Data"""

    VALUE = "value"
    """Common Field For Filter Value in Request Data"""

    SORT = "sort"
    """Common Field For Sorting in Request Data"""

    KEYWORD = "keyword"
    """Common Field For Sorting Keyword in Request Data"""

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

DEFAULT_SEARCH_FROM = 0
"""Default `search_from` Field for Limit-Offset Pagination"""

DEFAULT_SEARCH_TO = 100
"""Default `search_to` Field for Limit-Offset Pagination"""

MAX_TOTAL_COUNT = 9_999
"""Maximum `total_count` in the `reply` for Most Endpoints"""

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
