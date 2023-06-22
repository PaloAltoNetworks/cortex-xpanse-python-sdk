from typing import Any, List, Optional, Set

from xpanse.api.asset_management.assets_management_base import (
    AssetsManagementBaseEndpoint,
)
from xpanse.const import AssetType, FilterOperator
from xpanse.iterator import XpanseResultIterator
from xpanse.response import XpanseResponse
from xpanse.types import RequestData, Filter
from xpanse.utils import build_request_payload


class AssetsEndpoint(AssetsManagementBaseEndpoint):
    """
    Part of the Public API for handling Assets.
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-All-Assets
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-Asset
    """

    LIST_ENDPOINT = (
        f"{AssetsManagementBaseEndpoint.ENDPOINT}/get_assets_internet_exposure/"
    )
    GET_ENDPOINT = (
        f"{AssetsManagementBaseEndpoint.ENDPOINT}/get_asset_internet_exposure/"
    )

    LIST_DATA_KEY = "assets_internet_exposure"

    def list(
        self,
        asset_types: Optional[Set[AssetType]] = None,
        request_data: Optional[RequestData] = None,
        **kwargs: Any,
    ) -> XpanseResultIterator:
        """
        This endpoint will return a paginated list of Assets.

        Args:
            asset_types (Set[AssetType], Optional):
                An optional set of Asset types that can be used to filter your request.
            request_data (RequestData, Optional):
                Any supplemental request_data to be included with your request. This is
                needed to implement any additional filters, offsets, limits, or sort ordering.
            **kwargs:
                Any extraneous parameters you would like to include when executing your
                request with the `requests` module. Note: By default, all payload data
                is sent under the "json" keyword for your request.

        Returns:
            :obj:`XpanseResultIterator`:
                An iterator containing all of the Asset results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Return all Assets dumped to a list:
            >>> assets =  client.assets.list().dump()
        """
        filters = self._build_asset_type_filters(asset_types=asset_types)
        return super(AssetsEndpoint, self)._list(
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
        """
        This endpoint will return details for a list of Asset ids. Arguments should be passed
        as keyword args using the names below.

        Args:
            asset_ids (List[str]):
                The lists of asset ids to retrieve with your request.
            request_data (RequestData, Optional):
                Any supplemental request_data to be included with your request. This is needed to
                implement any additional filters, offsets, limits, or sort ordering.
            **kwargs:
                Any extraneous parameters you would like to include when executing your
                request with the Requests.request module. Note: By default, all payload data
                is sent under the "json" keyword for your request.

        Returns:
            :obj:`XpanseResponse`:
                An object containing the raw requests.Response and parsed data results.
                The raw response can be accessed with `<xpanse_reponse>.response` attribute.
                The parsed results can be accessed with the `<xpanse_response>.data` attribute.

        Examples:
            >>> # Get Assets with specified ids to a list:
            >>> assets =  client.assets.get(asset_ids=["id1", "id2"])
            >>> if assets.response.status_code < 300:
            >>>     results = assets.data
        """
        extra_request_data = {"asm_id_list": asset_ids}
        return super(AssetsEndpoint, self)._get(
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
        """
        This endpoint will return a count of Assets.

        Args:
            asset_types (Set[AssetType], Optional):
                An optional set of asset types that can be used to filter your request.
            request_data (RequestData, Optional):
                Any supplemental request_data to be included with your request. This is needed to
                implement any additional filters, offsets, limits, or sort ordering.
            **kwargs:
                Any extraneous parameters you would like to include when executing your
                request with the Requests.request module. Note: By default, all payload data
                is sent under the "json" keyword for your request.

        Returns:
            :obj:`XpanseResponse`:
                An object containing the raw requests.Response and parsed data results.
                The raw response can be accessed with `<xpanse_reponse>.response` attribute.
                The parsed results can be accessed with the `<xpanse_response>.data` attribute.

        Examples:
            >>> # Get Assets total count:
            >>> assets =  client.assets.count()
            >>> if assets.response.status_code < 300:
            >>>     count = assets.data
        """
        filters = self._build_asset_type_filters(asset_types=asset_types)
        kwargs = build_request_payload(filters=filters, **kwargs)
        return super(AssetsEndpoint, self)._count(
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
