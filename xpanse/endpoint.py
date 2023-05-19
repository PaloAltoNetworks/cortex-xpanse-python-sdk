from typing import Optional

from xpanse.const import PublicApiFields
from xpanse.response import XpanseResponse
from xpanse.types import RequestData
from xpanse.utils import build_request_payload


class XpanseEndpoint:
    """
    The XpanseEndpoint class is used as a base class for all endpoints.
    Any additional logic that is desired to be present on all endpoints, but is
    outside of the scope of the session or client can be added here.
    """

    def __init__(self, session):
        self._api = session

    def _count(self, path: str, request_data: Optional[RequestData] = None, **kwargs):
        """
        Helper method for all count endpoint calls.

        Args:
            path (str):
                The endpoint used to make the request for each respective data type.
            request_data (RequestData, Optional):
                Any supplemental request_data to be included with your request. This is needed to
                implement any additional filters, offsets, limits, or sort ordering.
            **kwargs:
                Any extraneous parameters you would like to include when executing your
                request with the `requests` module. Note: By default, all payload data
                is sent under the "json" keyword for your request.

        Returns:
            :obj:`XpanseResponse`:
                An object containing the raw requests.Response and parsed data results.
                The raw response can be accessed with `<xpanse_reponse>.response` attribute.
                The parsed results can be accessed with the `<xpanse_response>.data` attribute.
        """
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
