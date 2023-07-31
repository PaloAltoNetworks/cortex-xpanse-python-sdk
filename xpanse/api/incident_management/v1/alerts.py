from typing import Any, List, Optional

from xpanse.const import V1_PREFIX
from xpanse.endpoint import XpanseEndpoint
from xpanse.response import XpanseResponse
from xpanse.utils import build_request_payload


class AlertsEndpointV1(XpanseEndpoint):
    """
    Part of the Public API for handling Alert Updates Endpoint.
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-Xpanse-REST-API/Update-Alerts
    """

    UPDATE_ENDPOINT = f"{V1_PREFIX}/alerts/update_alerts"
    UPDATE_DATA_KEY = "alerts_ids"

    def update(
        self, alert_id_list: List[str], update_data: Any, **kwargs: Any
    ) -> XpanseResponse:
        """
        This endpoint will update a set of Incidents' data.

        Args:
            alert_id_list (List[str]):
                The Incident id to modify with your request data.
            update_data (Any):
                The data with which to update the Alerts.
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
            >>> alerts =  client.alerts.update(alert_id_id="id1",
            >>>                                update_data={"comment": "alert has changed"})
            >>> if alerts.response.status_code < 300:
            >>>     results = alerts.data

        """
        extra_request_data = {
            "alert_id_list": alert_id_list,
            "update_data": update_data,
        }
        kwargs = build_request_payload(extra_request_data=extra_request_data, **kwargs)
        response = self._api.post(self.UPDATE_ENDPOINT, **kwargs)
        return XpanseResponse(response, data_key=self.UPDATE_DATA_KEY)
