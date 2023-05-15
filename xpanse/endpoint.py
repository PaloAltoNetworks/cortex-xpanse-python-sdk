from typing import Any

from xpanse.const import PublicApiFields
from xpanse.response import XpanseResponse
from xpanse.utils import build_request_payload


class XpanseEndpoint:
    """
    The XpanseEndpoint class is used as a base class for all endpoints.
    Any additional logic that is desired to be present on all endpoints, but is
    outside of the scope of the session or client can be added here.
    """

    def __init__(self, session):
        self._api = session

    def _count(self, path: str, request_data: Any = None, **kwargs):
        # Performance enhancement for count endpoint
        extra_request_data = {
            PublicApiFields.SEARCH_FROM: 0,
            PublicApiFields.SEARCH_TO: 1,
        }
        kwargs = build_request_payload(
            request_data=request_data, extra_request_data=extra_request_data, **kwargs
        )
        response = self._api.post(path, **kwargs)
        return XpanseResponse(response, data_key=PublicApiFields.TOTAL_COUNT)
