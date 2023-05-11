from typing import Any, List

from xpanse.const import V1_PREFIX, PublicApiFields
from xpanse.endpoint import XpanseEndpoint
from xpanse.iterator import XpanseResultIterator
from xpanse.utils import build_request_payload


class IncidentsApi(XpanseEndpoint):
    """
    Part of the Alerts v2 Public API for handling Alerts Multi-Events v2.
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
    ) -> Any:
        filters = [
            {"field": "incident_id_list", "operator": "in", "value": incident_ids}
        ]
        kwargs = build_request_payload(
            request_data=request_data, filters=filters, **kwargs
        )
        return self._api.post(f"{self.ENDPOINT}/get_incidents/", **kwargs).json()[
            PublicApiFields.REPLY
        ][self.DATA_KEY]

    def count(self, request_data: Any = None, **kwargs: Any) -> int:
        kwargs = build_request_payload(request_data=request_data, **kwargs)
        return self._api.post(f"{self.ENDPOINT}/get_incidents/", **kwargs).json()[
            PublicApiFields.REPLY
        ][PublicApiFields.TOTAL_COUNT]

    def update(self, incident_ids: List[str], update_data: Any, **kwargs: Any) -> bool:
        extra_request_data = {
            "incident_id_list": incident_ids,
            "update_data": update_data,
        }
        kwargs = build_request_payload(extra_request_data=extra_request_data, **kwargs)
        return self._api.post(f"{self.ENDPOINT}/update_incident/", **kwargs)
