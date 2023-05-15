from typing import Any, List

from xpanse.endpoint import XpanseEndpoint
from xpanse.iterator import XpanseResultIterator


# TODO:// Implement Assets https://jira-hq.paloaltonetworks.local/browse/EXPANDR-2601
class AssetsApi(XpanseEndpoint):
    """
    Part of the Public API for handling Assets.
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-All-Assets
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-Asset
    """

    def list(self, **kwargs: Any) -> XpanseResultIterator:
        raise NotImplementedError()

    def get(self, asset_ids: List[str], **kwargs: Any) -> Any:
        raise NotImplementedError()

    def count(self, **kwargs: Any) -> int:
        raise NotImplementedError()
