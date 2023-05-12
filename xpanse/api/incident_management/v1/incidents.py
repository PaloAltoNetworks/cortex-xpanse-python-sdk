from typing import Any, List

from xpanse.endpoint import XpanseEndpoint
from xpanse.iterator import XpanseResultIterator


# TODO:// Implement Incidents https://jira-hq.paloaltonetworks.local/browse/EXPANDR-2596
class IncidentsApi(XpanseEndpoint):
    """
    Part of the Alerts v2 Public API for handling Alerts Multi-Events v2.
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-Incidents
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Update-an-Incident
    """

    def list(self, **kwargs: Any) -> XpanseResultIterator:
        raise NotImplementedError()

    def get(self, incident_ids: List[str], **kwargs: Any) -> Any:
        raise NotImplementedError()

    def count(self, **kwargs: Any) -> int:
        raise NotImplementedError()

    def update(self, incident_id: str, update_data: Any, **kwargs: Any) -> Any:
        raise NotImplementedError()
