from typing import Any, List, Optional

from xpanse.api.asset_management.assets_management_v1 import AssetsManagementV1
from xpanse.const import AssetType
from xpanse.iterator import XpanseResultIterator
from xpanse.response import XpanseResponse
from xpanse.utils import build_request_payload


class AssetsApi(AssetsManagementV1):
    """
    Part of the Public API for handling Assets.
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-All-Assets
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-Asset
    """

    def list(
        self,
        asset_types: Optional[List[AssetType]] = None,
        request_data: Any = None,
        **kwargs: Any,
    ) -> XpanseResultIterator:
        return super(AssetsApi, self)._list(
            f"{self.ENDPOINT}/get_assets_internet_exposure/",
            asset_types=asset_types,
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

    def count(
        self,
        asset_types: Optional[List[AssetType]] = None,
        request_data: Any = None,
        **kwargs: Any,
    ) -> XpanseResponse:
        filters = []
        if asset_types is not None:
            value = [t.value for t in asset_types]
            filters.append({"field": "type", "operator": "in", "value": value})

        kwargs = build_request_payload(filters=filters, **kwargs)

        return super(AssetsManagementV1, self)._count(
            f"{self.ENDPOINT}/get_assets_internet_exposure/",
            request_data=request_data,
            **kwargs,
        )
