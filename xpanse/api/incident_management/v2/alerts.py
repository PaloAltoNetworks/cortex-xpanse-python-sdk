from typing import Any, List, Optional

from xpanse.const import V2_PREFIX, PublicApiFields, FilterOperator
from xpanse.endpoint import XpanseEndpoint
from xpanse.iterator import XpanseResultIterator
from xpanse.response import XpanseResponse
from xpanse.types import RequestData, Filter
from xpanse.utils import build_request_payload


class AlertsEndpoint(XpanseEndpoint):
    """
    Part of the Public API for handling Alerts Multi-Events v2.
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-Alerts-Multi-Events
    """

    ENDPOINT = f"{V2_PREFIX}/alerts/get_alerts_multi_events/"
    DATA_KEY = "alerts"

    def list(
        self, request_data: Optional[RequestData] = None, **kwargs: Any
    ) -> XpanseResultIterator:
        """
        This endpoint will return a paginated list of Alerts.

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
                An iterator containing all of the Alert results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Return all Alerts dumped to a list:
            >>> alerts =  client.alerts.list().dump()
        """
        kwargs = build_request_payload(request_data=request_data, **kwargs)
        return XpanseResultIterator(
            api=self._api, path=self.ENDPOINT, data_key=self.DATA_KEY, **kwargs
        )

    def get(
        self,
        alert_ids: List[str],
        request_data: Optional[RequestData] = None,
        **kwargs: Any,
    ) -> XpanseResponse:
        """
        This endpoint will return details for a list of Alert ids. Arguments should be passed as keyword args using
        the names below.

        Args:
            alert_ids (List[str]):
                The lists of Alert ids to retrieve with your request.
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
            >>> # Get Alerts with specified ids to a list:
            >>> alerts =  client.alerts.get(alert_ids=["id1", "id2"])
            >>> if alerts.response.status_code < 300:
            >>>     results = alerts.data
        """
        filters: List[Filter] = [
            {
                "field": "alert_id_list",
                "operator": FilterOperator.IN.value,
                "value": alert_ids,
            }
        ]
        kwargs = build_request_payload(
            request_data=request_data, filters=filters, **kwargs
        )
        response = self._api.post(self.ENDPOINT, **kwargs)
        return XpanseResponse(response, data_key=self.DATA_KEY)

    def count(
        self, request_data: Optional[RequestData] = None, **kwargs: Any
    ) -> XpanseResponse:
        """
        This endpoint will return a count of Alerts.

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
            >>> # Get Alerts total count:
            >>> alerts =  client.alerts.count()
            >>> if alerts.response.status_code < 300:
            >>>     count = alerts.data
        """
        return super(AlertsEndpoint, self)._count(
            self.ENDPOINT, request_data=request_data, **kwargs
        )
