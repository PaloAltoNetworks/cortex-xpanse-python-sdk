from typing import Any, Dict, List, Optional

from xpanse.const import V1_PREFIX
from xpanse.endpoint import XpanseEndpoint
from xpanse.iterator import XpanseResultIterator
from xpanse.response import XpanseResponse
from xpanse.types import RequestData, Filter
from xpanse.utils import build_request_payload


class AssetsManagementBaseEndpoint(XpanseEndpoint):
    """
    Part of the Public API for handling all things relating to Asset Management. This class is wrapped by the
    specific data type implementations in the client endpoints.
    See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Asset-Management-APIs
    """

    ENDPOINT = f"{V1_PREFIX}/assets"
    LIST_DATA_KEY = "data"
    GET_DATA_KEY = "details"

    def _list(
        self,
        path: str,
        request_data: Optional[RequestData] = None,
        filters: Optional[List[Filter]] = None,
        **kwargs: Any,
    ) -> XpanseResultIterator:
        kwargs = build_request_payload(
            request_data=request_data, filters=filters, **kwargs
        )
        return XpanseResultIterator(
            api=self._api,
            path=path,
            data_key=self.LIST_DATA_KEY,
            **kwargs,
        )

    def _get(
        self,
        path: str,
        extra_request_data: Dict[str, list],
        request_data: Optional[RequestData] = None,
        **kwargs: Any,
    ) -> XpanseResponse:
        kwargs = build_request_payload(
            request_data=request_data, extra_request_data=extra_request_data, **kwargs
        )
        response = self._api.post(path, **kwargs)
        return XpanseResponse(response, data_key=self.GET_DATA_KEY)
