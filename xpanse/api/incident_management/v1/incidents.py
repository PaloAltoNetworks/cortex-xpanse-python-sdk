from typing import Any, List

from xpanse.const import V1_PREFIX, PublicApiFields
from xpanse.endpoint import XpanseEndpoint
from xpanse.iterator import XpanseResultIterator
from xpanse.response import XpanseResponse
from xpanse.utils import build_request_payload


class IncidentsApi(XpanseEndpoint):
    """
    Part of the Public API for handling Incidents.
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-Incidents
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Update-an-Incident
    """

    ENDPOINT = f"{V1_PREFIX}/incidents"
    DATA_KEY = "incidents"

    def list(self, request_data: Any = None, **kwargs: Any) -> XpanseResultIterator:
        kwargs = build_request_payload(request_data=request_data, **kwargs)
        return XpanseResultIterator(
            api=self._api,
            path=f"{self.ENDPOINT}/get_incidents/",
            data_key=self.DATA_KEY,
            **kwargs,
        )

    def get(
        self, incident_ids: List[str], request_data: Any = None, **kwargs: Any
    ) -> XpanseResponse:
        filters = [
            {"field": "incident_id_list", "operator": "in", "value": incident_ids}
        ]
        kwargs = build_request_payload(
            request_data=request_data, filters=filters, **kwargs
        )
        response = self._api.post(f"{self.ENDPOINT}/get_incidents/", **kwargs)
        return XpanseResponse(response, data_key=self.DATA_KEY)

    def count(self, request_data: Any = None, **kwargs: Any) -> XpanseResponse:
        kwargs = build_request_payload(request_data=request_data, **kwargs)
        response = self._api.post(f"{self.ENDPOINT}/get_incidents/", **kwargs)
        return XpanseResponse(response, data_key=PublicApiFields.TOTAL_COUNT)

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
