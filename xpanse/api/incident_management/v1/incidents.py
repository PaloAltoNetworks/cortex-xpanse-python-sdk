from typing import Any, List, Optional, cast

from xpanse.const import (
    V1_PREFIX,
    FilterOperator,
    PublicApiFields,
    DEFAULT_SEARCH_FROM,
    DEFAULT_SEARCH_TO,
)
from xpanse.endpoint import XpanseEndpoint
from xpanse.iterator import XpanseResultIterator
from xpanse.response import XpanseResponse
from xpanse.types import RequestData, Filter
from xpanse.utils import build_request_payload


class IncidentsEndpoint(XpanseEndpoint):
    """
    Part of the Public API for handling Incidents.
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-Incidents
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Update-an-Incident
    """

    LIST_ENDPOINT = f"{V1_PREFIX}/incidents/get_incidents/"
    UPDATE_ENDPOINT = f"{V1_PREFIX}/incidents/update_incident/"
    DATA_KEY = "incidents"

    def list(
        self, request_data: Optional[RequestData] = None, **kwargs: Any
    ) -> XpanseResultIterator:
        """
        This endpoint will return a paginated list of Incidents.

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
                An iterator containing all of the Incident results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Return all Incidents dumped to a list:
            >>> incidents =  client.incidents.list().dump()
        """
        kwargs = build_request_payload(request_data=request_data, **kwargs)
        search_from = (request_data or {}).get(
            PublicApiFields.SEARCH_FROM, DEFAULT_SEARCH_FROM
        )
        search_to = (request_data or {}).get(
            PublicApiFields.SEARCH_TO, DEFAULT_SEARCH_TO
        )
        return XpanseResultIterator(
            api=self._api,
            path=self.LIST_ENDPOINT,
            data_key=self.DATA_KEY,
            use_page_token=False,
            search_from=cast(int, search_from),
            search_to=cast(int, search_to),
            **kwargs,
        )

    def get(
        self,
        incident_ids: List[str],
        request_data: Optional[RequestData] = None,
        **kwargs: Any,
    ) -> XpanseResponse:
        """
        This endpoint will return details for a list of Incident ids. Arguments should be passed as keyword args using
        the names below.

        Args:
            incident_ids (List[str]):
                The list of Incident ids to retrieve with your request.
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
            >>> # Get Incidents with specified ids to a list:
            >>> incidents =  client.incidents.get(incident_ids=["id1", "id2"])
            >>> if incidents.response.status_code < 300:
            >>>     results = incidents.data
        """
        filters: List[Filter] = [
            {
                "field": "incident_id_list",
                "operator": FilterOperator.IN.value,
                "value": incident_ids,
            }
        ]
        kwargs = build_request_payload(
            request_data=request_data, filters=filters, **kwargs
        )
        response = self._api.post(self.LIST_ENDPOINT, **kwargs)
        return XpanseResponse(response, data_key=self.DATA_KEY)

    def count(
        self, request_data: Optional[RequestData] = None, **kwargs: Any
    ) -> XpanseResponse:
        """
        This endpoint will return a count of Incidents.

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
            >>> # Get Incidents total count:
            >>> incidents =  client.incidents.count()
            >>> if incidents.response.status_code < 300:
            >>>     count = incidents.data
        """
        return super(IncidentsEndpoint, self)._count(
            self.LIST_ENDPOINT, request_data=request_data, **kwargs
        )

    def update(
        self, incident_id: str, update_data: Any, **kwargs: Any
    ) -> XpanseResponse:
        """
        This endpoint will update a set of Incidents' data.

        Args:
            incident_id (str):
                The Incident id to modify with your request data.
            update_data (Any):
                The data with which to update the Incident.
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
            >>> # Update Incidents with new assignee:
            >>> incidents =  client.incidents.update(incident_id="id1",
            >>>                                      update_data={"assigned_user_mail": "new@mail.com"})
            >>> if incidents.response.status_code < 300:
            >>>     results = incidents.data

        """
        extra_request_data = {
            "incident_id": incident_id,
            "update_data": update_data,
        }
        kwargs = build_request_payload(extra_request_data=extra_request_data, **kwargs)
        response = self._api.post(self.UPDATE_ENDPOINT, **kwargs)
        return XpanseResponse(response)
