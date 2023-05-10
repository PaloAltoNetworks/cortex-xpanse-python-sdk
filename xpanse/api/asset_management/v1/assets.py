from typing import Any, List

from xpanse.endpoint import XpanseEndpoint
from xpanse.iterator import XpanseResultIterator


# TODO:// Implement Assets https://jira-hq.paloaltonetworks.local/browse/EXPANDR-2601
class AssetsApi(XpanseEndpoint):
    """
    Part of the Alerts v2 Public API for handling Alerts Multi-Events v2.
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-All-Assets
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-Asset
    """
    def list(self, **kwargs: Any) -> XpanseResultIterator:
        pass

    def get(self, asset_ids: List[str], **kwargs: Any) -> Any:
        pass

    def count(self, **kwargs: Any) -> int:
        pass
