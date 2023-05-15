from typing import Any, List

from xpanse.api.asset_management.assets_management_v1 import AssetsManagementV1
from xpanse.iterator import XpanseResultIterator


from xpanse.response import XpanseResponse


class ExternalIpRangesApi(AssetsManagementV1):
    """
    Part of the Public API for handling External IP Ranges.
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-All-External-IP-Address-Ranges
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-External-IP-Address-Range
    """

    def list(self, request_data: Any = None, **kwargs: Any) -> XpanseResultIterator:
        return super(ExternalIpRangesApi, self)._list(
            f"{self.ENDPOINT}/get_external_ip_address_ranges/",
            request_data=request_data,
            **kwargs,
        )

    def get(
        self, ip_range_ids: List[str], request_data: Any = None, **kwargs: Any
    ) -> XpanseResponse:
        extra_request_data = {"range_id_list": ip_range_ids}
        return super(ExternalIpRangesApi, self)._get(
            f"{self.ENDPOINT}/get_external_ip_address_range/",
            extra_request_data=extra_request_data,
            request_data=request_data,
            **kwargs,
        )

    def count(self, request_data: Any = None, **kwargs: Any) -> XpanseResponse:
        return super(ExternalIpRangesApi, self)._count(
            f"{self.ENDPOINT}/get_external_ip_address_ranges/",
            request_data=request_data,
            **kwargs,
        )
