from typing import Any, List

from xpanse.endpoint import XpanseEndpoint
from xpanse.iterator import XpanseResultIterator


# TODO:// Implement Tags https://jira-hq.paloaltonetworks.local/browse/EXPANDR-2603
class TagsApi(XpanseEndpoint):
    """
    Part of the Alerts v2 Public API for handling Alerts Multi-Events v2.
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-Alerts-Multi-Events
    """

    def list(self, **kwargs: Any) -> XpanseResultIterator:
        raise NotImplementedError()

    def get(self, tag_ids: List[str], **kwargs: Any) -> Any:
        raise NotImplementedError()

    def create(self, **kwargs: Any) -> Any:
        raise NotImplementedError()

    def update(self, **kwargs: Any) -> Any:
        raise NotImplementedError()
