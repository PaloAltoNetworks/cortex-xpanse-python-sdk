from typing import Any, List, Optional

from xpanse.api.asset_management.assets_management_base import (
    AssetsManagementBaseEndpoint,
)
from xpanse.iterator import XpanseResultIterator
from xpanse.response import XpanseResponse
from xpanse.types import RequestData


class ServicesEndpoint(AssetsManagementBaseEndpoint):
    """
    Part of the Public API for handling Services.
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-All-External-Services
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-External-Service
    """

    LIST_ENDPOINT = f"{AssetsManagementBaseEndpoint.ENDPOINT}/get_external_services/"
    GET_ENDPOINT = f"{AssetsManagementBaseEndpoint.ENDPOINT}/get_external_service/"

    LIST_DATA_KEY = "external_services"

    def list(
        self, request_data: Optional[RequestData] = None, **kwargs: Any
    ) -> XpanseResultIterator:
        """
        This endpoint will return a paginated list of Services.

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
                An iterator containing all of the Service results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Return all Services dumped to a list:
            >>> services =  client.services.list().dump()
        """
        return super(ServicesEndpoint, self)._list(
            self.LIST_ENDPOINT,
            request_data=request_data,
            **kwargs,
        )

    def get(
        self,
        service_ids: List[str],
        request_data: Optional[RequestData] = None,
        **kwargs: Any,
    ) -> XpanseResponse:
        """
        This endpoint will return details for a list of Service ids. Arguments should be passed as keyword args using
        the names below.

        Args:
            service_ids (List[str]):
                The lists of Service ids to retrieve with your request.
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
            >>> # Get Services with specified ids to a list:
            >>> services =  client.services.get(service_ids=["id1", "id2"])
            >>> if services.response.status_code < 300:
            >>>     results = services.data
        """
        extra_request_data = {"service_id_list": service_ids}
        return super(ServicesEndpoint, self)._get(
            self.GET_ENDPOINT,
            extra_request_data=extra_request_data,
            request_data=request_data,
            **kwargs,
        )

    def count(
        self, request_data: Optional[RequestData] = None, **kwargs: Any
    ) -> XpanseResponse:
        """
        This endpoint will return a count of Services.

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
            >>> # Get Services total count:
            >>> services =  client.services.count()
            >>> if services.response.status_code < 300:
            >>>     count = services.data
        """
        return super(ServicesEndpoint, self)._count(
            self.LIST_ENDPOINT,
            request_data=request_data,
            **kwargs,
        )
