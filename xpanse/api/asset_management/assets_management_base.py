from typing import Any, Dict, List, Optional

from xpanse.const import V1_PREFIX
from xpanse.endpoint import XpanseEndpoint
from xpanse.iterator import XpanseResultIterator
from xpanse.response import XpanseResponse
from xpanse.types import RequestData, Filter
from xpanse.utils import build_request_payload


class AssetsManagementBaseEndpoint(XpanseEndpoint):
    """
    Part of the Public API for handling all things relating to Asset Management. This class is wrapped by the
    specific data type implementations in the client endpoints.
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Asset-Management-APIs
    """

    ENDPOINT = f"{V1_PREFIX}/assets"
    LIST_DATA_KEY = "data"
    GET_DATA_KEY = "details"

    def _list(
        self,
        path: str,
        request_data: Optional[RequestData] = None,
        filters: Optional[List[Filter]] = None,
        **kwargs: Any,
    ) -> XpanseResultIterator:
        """

        Args:
            path (str):
                The endpoint used to make the request for each respective data type.
            request_data (RequestData, Optional):
                Any supplemental request_data to be included with your request. This is needed to
                implement any additional filters, offsets, limits, or sort ordering.
            filters:
                A list of filter objects to be applied to the query. In this context, this is used
                to support the built-in "asset_types" filter for the Assets data type.
            **kwargs:
                Any extraneous parameters you would like to include when executing your
                request with the Requests.request module. Note: By default, all payload data
                is sent under the "json" keyword for your request.

        Returns:
            :obj:`XpanseResponse`:
                An object containing the raw requests.Response and parsed data results.
                The raw response can be accessed with `<xpanse_reponse>.response` attribute.
                The parsed results can be accessed with the `<xpanse_response>.data` attribute.

        """
        kwargs = build_request_payload(
            request_data=request_data, filters=filters, **kwargs
        )
        return XpanseResultIterator(
            api=self._api,
            path=path,
            data_key=self.LIST_DATA_KEY,
            **kwargs,
        )

    def _get(
        self,
        path: str,
        extra_request_data: Dict[str, List],
        request_data: Optional[RequestData] = None,
        **kwargs: Any,
    ) -> XpanseResponse:
        """
        Helper method to list or get any Asset Management data (Assets, Owned IP Ranges, Services).

        Args:
            path (str):
                The endpoint used to make the request for each respective data type.
            extra_request_data (Dict[str, List]):
                The request data used to filter on a set of object ids.
            request_data (RequestData, Optional):
                Any supplemental request_data to be included with your request. This is needed to
                implement any additional filters, offsets, limits, or sort ordering.
            **kwargs:
                Any extraneous parameters you would like to include when executing your
                request with the Requests.request module. Note: By default, all payload data
                is sent under the "json" keyword for your request.

        Returns:
            :obj:`XpanseResponse`:
                An object containing the raw requests.Response and parsed data results.
                The raw response can be accessed with `<xpanse_reponse>.response` attribute.
                The parsed results can be accessed with the `<xpanse_response>.data` attribute.
        """
        kwargs = build_request_payload(
            request_data=request_data, extra_request_data=extra_request_data, **kwargs
        )
        response = self._api.post(path, **kwargs)
        return XpanseResponse(response, data_key=self.GET_DATA_KEY)
