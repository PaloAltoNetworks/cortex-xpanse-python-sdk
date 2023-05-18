from typing import Any, List, Optional

from xpanse.const import V1_PREFIX, FilterOperator
from xpanse.endpoint import XpanseEndpoint
from xpanse.iterator import XpanseResultIterator
from xpanse.response import XpanseResponse
from xpanse.types import RequestData, Filter
from xpanse.utils import build_request_payload


class IncidentsApi(XpanseEndpoint):
    """
    Part of the Public API for handling Incidents.
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-Incidents
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Update-an-Incident
    """

    ENDPOINT = f"{V1_PREFIX}/incidents"
    DATA_KEY = "incidents"

    def list(
        self, request_data: Optional[RequestData] = None, **kwargs: Any
    ) -> XpanseResultIterator:
        kwargs = build_request_payload(request_data=request_data, **kwargs)
        return XpanseResultIterator(
            api=self._api,
            path=f"{self.ENDPOINT}/get_incidents/",
            data_key=self.DATA_KEY,
            **kwargs,
        )

    def get(
        self,
        incident_ids: List[str],
        request_data: Optional[RequestData] = None,
        **kwargs: Any,
    ) -> XpanseResponse:
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
        response = self._api.post(f"{self.ENDPOINT}/get_incidents/", **kwargs)
        return XpanseResponse(response, data_key=self.DATA_KEY)

    def count(
        self, request_data: Optional[RequestData] = None, **kwargs: Any
    ) -> XpanseResponse:
        return super(IncidentsApi, self)._count(
            f"{self.ENDPOINT}/get_incidents/", request_data=request_data, **kwargs
        )

    def update(
        self, incident_ids: List[str], update_data: Any, **kwargs: Any
    ) -> XpanseResponse:
        extra_request_data = {
            "incident_id_list": incident_ids,
            "update_data": update_data,
        }
        kwargs = build_request_payload(extra_request_data=extra_request_data, **kwargs)
        response = self._api.post(f"{self.ENDPOINT}/update_incident/", **kwargs)
        return XpanseResponse(response)
