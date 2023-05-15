from typing import Optional

from requests import Response

from xpanse.const import PublicApiFields


class XpanseResponse:
    def __init__(self, response: Response, data_key: Optional[str] = None):
        self._response = response
        self._data_key = data_key

    @property
    def response(self):
        return self._response

    @property
    def data(self):
        response_data = self.response.json()
        if self._data_key is not None and self._data_key in response_data.get(
            PublicApiFields.REPLY, {}
        ):
            return response_data[PublicApiFields.REPLY][self._data_key]

        return (
            response_data.get(PublicApiFields.REPLY, response_data)
            if isinstance(response_data, dict)
            else response_data
        )
