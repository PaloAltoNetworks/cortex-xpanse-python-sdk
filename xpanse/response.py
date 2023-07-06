from typing import Optional, Any

from requests import Response

from xpanse.const import PublicApiFields


class XpanseResponse:
    """
    This class wraps the existing requests.Response class to enable ease of parsing while maintaining the
    raw response object and status code.

    Usages:
        > To see the raw response from the request, access the "response" attribute: xpanse_response.response
        > To grab the parsed data from the response, access the "data" attribute: xpanse_response.data

    Examples:
        >>> assets = client.assets.get(asset_ids=["id1"])
        >>> if assets.response.status_code < 300:
        >>>     results = assets.data
    """

    def __init__(self, response: Response, data_key: Optional[str] = None):
        self._response = response
        self._data_key = data_key

    @property
    def response(self) -> Response:
        """
        Defines the raw `requests.Response` property
        """
        return self._response

    @property
    def data(self) -> Any:
        """
        Parses the response body and returns it under the `data` property
        """
        response_data = self.response.json()

        if not isinstance(response_data, dict):
            return response_data

        if self._data_key is not None and self._data_key in response_data.get(
            PublicApiFields.REPLY, {}
        ):
            return response_data[PublicApiFields.REPLY][self._data_key]

        return response_data.get(PublicApiFields.REPLY, response_data)
