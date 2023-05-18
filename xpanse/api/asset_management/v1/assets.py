from typing import Any, List, Optional, Set

from xpanse.api.asset_management.assets_management_v1 import AssetsManagementV1
from xpanse.const import AssetType, FilterOperator
from xpanse.iterator import XpanseResultIterator
from xpanse.response import XpanseResponse
from xpanse.types import RequestData, Filter
from xpanse.utils import build_request_payload


class AssetsApi(AssetsManagementV1):
    """
    Part of the Public API for handling Assets.
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-All-Assets
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-Asset
    """

    LIST_ENDPOINT = f"{AssetsManagementV1.ENDPOINT}/get_assets_internet_exposure/"
    GET_ENDPOINT = f"{AssetsManagementV1.ENDPOINT}/get_asset_internet_exposure/"

    def list(
        self,
        asset_types: Optional[Set[AssetType]] = None,
        request_data: Optional[RequestData] = None,
        **kwargs: Any,
    ) -> XpanseResultIterator:
        filters = self._build_asset_type_filters(asset_types=asset_types)
        return super(AssetsApi, self)._list(
            self.LIST_ENDPOINT,
            request_data=request_data,
            filters=filters,
            **kwargs,
        )

    def get(
        self,
        asset_ids: List[str],
        request_data: Optional[RequestData] = None,
        **kwargs: Any,
    ) -> XpanseResponse:
        extra_request_data = {"asm_id_list": asset_ids}
        return super(AssetsApi, self)._get(
            self.GET_ENDPOINT,
            extra_request_data=extra_request_data,
            request_data=request_data,
            **kwargs,
        )

    def count(
        self,
        asset_types: Optional[Set[AssetType]] = None,
        request_data: Optional[RequestData] = None,
        **kwargs: Any,
    ) -> XpanseResponse:
        filters = self._build_asset_type_filters(asset_types=asset_types)
        kwargs = build_request_payload(filters=filters, **kwargs)
        return super(AssetsApi, self)._count(
            self.LIST_ENDPOINT,
            request_data=request_data,
            **kwargs,
        )

    @staticmethod
    def _build_asset_type_filters(
        asset_types: Optional[Set[AssetType]] = None,
    ) -> List[Filter]:
        """
        Helper method to construct the Asset Type filter for Asset endpoints.
        Args:
            asset_types (Set[AssetType]):
                A set of Asset Types from the AssetType enum

        Returns:
            :List[Filter]: A list of the Asset Type filters for the request_data query
        """
        filters: List[Filter] = []
        if asset_types is not None:
            value = []
            for t in asset_types:
                if t not in AssetType:
                    raise ValueError(f"Invalid AssetType provided: {t}")
                value.append(t.value)

            filters.append(
                {"field": "type", "operator": FilterOperator.IN.value, "value": value}
            )

        return filters
