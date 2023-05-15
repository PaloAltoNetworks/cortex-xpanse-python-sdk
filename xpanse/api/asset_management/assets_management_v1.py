from typing import Any, Dict

from xpanse.const import V1_PREFIX
from xpanse.endpoint import XpanseEndpoint
from xpanse.iterator import XpanseResultIterator
from xpanse.response import XpanseResponse
from xpanse.utils import build_request_payload


class AssetsManagementV1(XpanseEndpoint):
    ENDPOINT = f"{V1_PREFIX}/assets"
    LIST_DATA_KEY = "data"
    GET_DATA_KEY = "details"

    def _list(
        self, path: str, request_data: Any = None, **kwargs: Any
    ) -> XpanseResultIterator:
        kwargs = build_request_payload(request_data=request_data, **kwargs)
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
        request_data: Any = None,
        **kwargs: Any,
    ) -> XpanseResponse:
        kwargs = build_request_payload(
            request_data=request_data, extra_request_data=extra_request_data, **kwargs
        )
        response = self._api.post(path, **kwargs)
        return XpanseResponse(response, data_key=self.GET_DATA_KEY)
