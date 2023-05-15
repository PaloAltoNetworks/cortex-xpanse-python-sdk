from typing import Any, List

from xpanse.const import V2_PREFIX, PublicApiFields
from xpanse.endpoint import XpanseEndpoint
from xpanse.iterator import XpanseResultIterator
from xpanse.response import XpanseResponse
from xpanse.utils import build_request_payload


class AlertsApi(XpanseEndpoint):
    """
    Part of the Alerts v2 Public API for handling Alerts Multi-Events v2.
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-Alerts-Multi-Events
    """

    ENDPOINT = f"{V2_PREFIX}/alerts/get_alerts_multi_events/"
    DATA_KEY = "data"

    def list(self, request_data: Any = None, **kwargs: Any) -> XpanseResultIterator:
        kwargs = build_request_payload(request_data=request_data, **kwargs)
        return XpanseResultIterator(
            api=self._api, path=self.ENDPOINT, data_key=self.DATA_KEY, **kwargs
        )

    def get(self, alert_ids: List[str], request_data: Any = None, **kwargs: Any) -> XpanseResponse:
        filters = [{"field": "alert_id_list", "operator": "in", "value": alert_ids}]
        kwargs = build_request_payload(
            request_data=request_data, filters=filters, **kwargs
        )
        response = self._api.post(self.ENDPOINT, **kwargs)
        return XpanseResponse(response, data_key=self.DATA_KEY)

    def count(self, request_data: Any = None, **kwargs: Any) -> XpanseResponse:
        kwargs = build_request_payload(request_data=request_data, **kwargs)
        response = self._api.post(self.ENDPOINT, **kwargs)
        return XpanseResponse(response, data_key=PublicApiFields.TOTAL_COUNT)
