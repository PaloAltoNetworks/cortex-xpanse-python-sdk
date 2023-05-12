from typing import Any, List

from xpanse.endpoint import XpanseEndpoint
from xpanse.iterator import XpanseResultIterator


# TODO:// Implement Alerts https://jira-hq.paloaltonetworks.local/browse/EXPANDR-2599
class AlertsApi(XpanseEndpoint):
    """
    Part of the Alerts v2 Public API for handling Alerts Multi-Events v2.
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-Alerts-Multi-Events
    """

    def list(self, **kwargs: Any) -> XpanseResultIterator:
        raise NotImplementedError()

    def get(self, alert_ids: List[str], **kwargs: Any) -> Any:
        raise NotImplementedError()

    def count(self, **kwargs: Any) -> int:
        raise NotImplementedError()
