from typing import Any, List

from xpanse.endpoint import XpanseEndpoint
from xpanse.iterator import XpanseResultIterator


# TODO:// Implement Services https://jira-hq.paloaltonetworks.local/browse/EXPANDR-2600
class ServicesApi(XpanseEndpoint):
    """
    Part of the Alerts v2 Public API for handling Alerts Multi-Events v2.
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-All-External-Services
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-External-Service
    """

    def list(self, **kwargs: Any) -> XpanseResultIterator:
        raise NotImplementedError()

    def get(self, service_ids: List[str], **kwargs: Any) -> Any:
        raise NotImplementedError()

    def count(self, **kwargs: Any) -> int:
        raise NotImplementedError()
