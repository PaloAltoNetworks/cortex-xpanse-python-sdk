import logging
from typing import Any, Dict, List, Optional

from xpanse.const import PublicApiFields
from xpanse.error import UnexpectedResponseError


class XpanseResultIterator:
    """
    Iterator for paging though results.
    """

    # Total number of results - may not be available
    _total: int = 0

    # Pages seen so far
    _pages: int = 0

    # Next page token
    _next_page_token: Optional[str] = None

    def __init__(self, api: Any, path: str, data: Any, data_key: str):
        self._api = api
        self._path = path
        self._data = data
        self._data_key = data_key
        self._log = logging.getLogger(
            "{}.{}".format(self.__module__, self.__class__.__name__)
        )

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    @property
    def total(self) -> int:
        return self._total

    def next(self) -> Dict[str, Any]:
        """
        Fetches the result from pagination.next, if a value exists.
        """
        if self._next_page_token is None and self._pages >= 1:
            raise StopIteration("Pagination exhausted")

        return self._get_data()

    def has_next(self) -> bool:
        return self._pages == 0 or self._next_page_token is not None

    def dump(self) -> List[Any]:
        """
        Iterates until completion and returns a list of results.
        """
        return [j for i in self for j in i]

    def _get_data(self) -> Dict[str, Any]:
        """
        Returns the next page of data
        """
        try:
            if self._pages >= 1:
                resp = self._api.post(self._path, data={PublicApiFields.NEXT_PAGE_TOKEN: self._next_page_token})
            else:
                resp = self._api.post(self._path, data={**self._data, PublicApiFields.USE_PAGE_TOKEN: True})

            resp_as_json = resp.json()  # type: ignore

            self._pages += 1

            self._next_page_token = resp_as_json.get(PublicApiFields.REPLY, {})\
                .get(PublicApiFields.NEXT_PAGE_TOKEN, None)

            self._total = resp_as_json.get(PublicApiFields.REPLY, {})\
                .get(PublicApiFields.TOTAL_COUNT, 0)

            return resp_as_json[PublicApiFields.REPLY][self._data_key]
        except KeyError as err:
            raise UnexpectedResponseError(
                "XpanseResultIterator received unexpected response"
            ) from err
