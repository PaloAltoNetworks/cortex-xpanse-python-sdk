from typing import Any, List

from xpanse.api.asset_management.assets_management_v1 import AssetsManagementV1
from xpanse.iterator import XpanseResultIterator
from xpanse.response import XpanseResponse


class AssetsApi(AssetsManagementV1):
    """
    Part of the Public API for handling Assets.
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-All-Assets
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-Asset
    """

    def list(self, request_data: Any = None, **kwargs: Any) -> XpanseResultIterator:
        return super(AssetsApi, self)._list(
            f"{self.ENDPOINT}/get_assets_internet_exposure/",
            request_data=request_data,
            **kwargs,
        )

    def get(
        self, asset_ids: List[str], request_data: Any = None, **kwargs: Any
    ) -> XpanseResponse:
        extra_request_data = {"asm_id_list": asset_ids}
        return super(AssetsApi, self)._get(
            f"{self.ENDPOINT}/get_asset_internet_exposure/",
            extra_request_data=extra_request_data,
            request_data=request_data,
            **kwargs,
        )

    def count(self, request_data: Any = None, **kwargs: Any) -> XpanseResponse:
        return super(AssetsApi, self)._count(
            f"{self.ENDPOINT}/get_assets_internet_exposure/",
            request_data=request_data,
            **kwargs,
        )
