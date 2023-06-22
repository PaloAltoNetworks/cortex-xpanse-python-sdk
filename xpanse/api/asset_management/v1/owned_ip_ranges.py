from typing import Any, List, Optional

from xpanse.api.asset_management.assets_management_base import (
    AssetsManagementBaseEndpoint,
)
from xpanse.iterator import XpanseResultIterator
from xpanse.response import XpanseResponse
from xpanse.types import RequestData


class OwnedIpRangesEndpoint(AssetsManagementBaseEndpoint):
    """
    Part of the Public API for handling Owned IP Ranges.
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-All-External-IP-Address-Ranges
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-External-IP-Address-Range
    """

    LIST_DATA_KEY = "external_ip_address_ranges"

    LIST_ENDPOINT = (
        f"{AssetsManagementBaseEndpoint.ENDPOINT}/get_external_ip_address_ranges/"
    )
    GET_ENDPOINT = (
        f"{AssetsManagementBaseEndpoint.ENDPOINT}/get_external_ip_address_range/"
    )

    def list(
        self, request_data: Optional[RequestData] = None, **kwargs: Any
    ) -> XpanseResultIterator:
        """
        This endpoint will return a paginated list of Owned IP Ranges.

        Args:
            request_data (RequestData, Optional):
                Any supplemental request_data to be included with your request. This is needed to
                implement any additional filters, offsets, limits, or sort ordering.
            **kwargs:
                Any extraneous parameters you would like to include when executing your
                request with the `requests` module. Note: By default, all payload data
                is sent under the "json" keyword for your request.

        Returns:
            :obj:`XpanseResultIterator`:
                An iterator containing all of the Owned IP Ranges results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Return all Owned IP Ranges dumped to a list:
            >>> ip_ranges =  client.owned_ip_ranges.list().dump()
        """
        return super(OwnedIpRangesEndpoint, self)._list(
            self.LIST_ENDPOINT,
            request_data=request_data,
            **kwargs,
        )

    def get(
        self,
        ip_range_ids: List[str],
        request_data: Optional[RequestData] = None,
        **kwargs: Any,
    ) -> XpanseResponse:
        """
        This endpoint will return details for a list of Owned IP Range ids. Arguments should be passed as keyword args using
        the names below.

        Args:
            ip_range_ids (List[str]):
                The lists of Owned IP Range ids to retrieve with your request.
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

        Examples:
            >>> # Get Owned IP Ranges with specified ids to a list:
            >>> ip_ranges =  client.owned_ip_ranges.get(ip_range_ids=["id1", "id2"])
            >>> if ip_ranges.response.status_code < 300:
            >>>     results = ip_ranges.data
        """
        extra_request_data = {"range_id_list": ip_range_ids}
        return super(OwnedIpRangesEndpoint, self)._get(
            self.GET_ENDPOINT,
            extra_request_data=extra_request_data,
            request_data=request_data,
            **kwargs,
        )

    def count(
        self, request_data: Optional[RequestData] = None, **kwargs: Any
    ) -> XpanseResponse:
        """
        This endpoint will return a count of Owned IP Ranges.

        Args:
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

        Examples:
            >>> # Get Owned IP Ranges total count:
            >>> ip_ranges =  client.owned_ip_ranges.count()
            >>> if ip_ranges.response.status_code < 300:
            >>>     count = ip_ranges.data
        """
        return super(OwnedIpRangesEndpoint, self)._count(
            self.LIST_ENDPOINT,
            request_data=request_data,
            **kwargs,
        )
