from typing import Any, List, Optional

from xpanse.api.asset_management.assets_management_base import (
    AssetsManagementBaseEndpoint,
)
from xpanse.iterator import XpanseResultIterator
from xpanse.response import XpanseResponse
from xpanse.types import RequestData


class ServicesApi(AssetsManagementBaseEndpoint):
    """
    Part of the Public API for handling Services.
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-All-External-Services
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-External-Service
    """

    LIST_ENDPOINT = f"{AssetsManagementBaseEndpoint.ENDPOINT}/get_external_services/"
    GET_ENDPOINT = f"{AssetsManagementBaseEndpoint.ENDPOINT}/get_external_service/"

    def list(
        self, request_data: Optional[RequestData] = None, **kwargs: Any
    ) -> XpanseResultIterator:
        return super(ServicesApi, self)._list(
            self.LIST_ENDPOINT,
            request_data=request_data,
            **kwargs,
        )

    def get(
        self,
        service_ids: List[str],
        request_data: Optional[RequestData] = None,
        **kwargs: Any,
    ) -> XpanseResponse:
        extra_request_data = {"service_id_list": service_ids}
        return super(ServicesApi, self)._get(
            self.GET_ENDPOINT,
            extra_request_data=extra_request_data,
            request_data=request_data,
            **kwargs,
        )

    def count(
        self, request_data: Optional[RequestData] = None, **kwargs: Any
    ) -> XpanseResponse:
        return super(ServicesApi, self)._count(
            self.LIST_ENDPOINT,
            request_data=request_data,
            **kwargs,
        )
