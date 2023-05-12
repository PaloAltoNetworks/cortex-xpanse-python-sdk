from typing import Any, List

from xpanse.endpoint import XpanseEndpoint
from xpanse.iterator import XpanseResultIterator


# TODO:// Implement Attack Surface Rules https://jira-hq.paloaltonetworks.local/browse/EXPANDR-2602
class AttackSurfaceRulesApi(XpanseEndpoint):
    """
    Part of the Alerts v2 Public API for handling Alerts Multi-Events v2.
    See: TODO:// https://jira-hq.paloaltonetworks.local/browse/EXPANDR-3062
    """

    def list(self, **kwargs: Any) -> XpanseResultIterator:
        raise NotImplementedError()

    def get(self, rule_ids: List[str], **kwargs: Any) -> Any:
        raise NotImplementedError()

    def count(self, **kwargs: Any) -> int:
        raise NotImplementedError()
