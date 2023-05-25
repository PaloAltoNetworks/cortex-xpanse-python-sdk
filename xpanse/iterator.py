import logging
from typing import Any, Dict, List, Optional

from requests import Response

from xpanse.const import (
    PublicApiFields,
    DEFAULT_SEARCH_FROM,
    DEFAULT_SEARCH_TO,
    MAX_TOTAL_COUNT,
)
from xpanse.error import UnexpectedResponseError
from xpanse.utils import build_request_payload


class XpanseResultIterator:
    """
    Iterator for paging though results.
    """

    # Total number of results - may not be available - limit is 9,999 results
    _total: int = 0

    # Last size of results page - used to determine when to stop
    _last_results_count: Optional[int] = None

    # Pages seen so far
    _pages: int = 0

    # Next page token, used when use_page_token is True
    _next_page_token: Optional[str] = None

    def __init__(
        self,
        api: Any,
        path: str,
        data_key: str,
        use_page_token: bool = True,
        search_from: int = DEFAULT_SEARCH_FROM,
        search_to: int = DEFAULT_SEARCH_TO,
        **kwargs,
    ):
        self._api = api
        self._path = path
        self._data_key = data_key
        self._use_page_token = use_page_token
        self._kwargs = kwargs
        self._log = logging.getLogger(
            "{}.{}".format(self.__module__, self.__class__.__name__)
        )

        if not self._use_page_token:
            if search_from < 0:
                raise ValueError(
                    f"'{PublicApiFields.SEARCH_FROM}' in '{PublicApiFields.REQUEST_DATA}' must be a positive integer. f{search_from} > 0."
                )

            if search_to < 0:
                raise ValueError(
                    f"'{PublicApiFields.SEARCH_TO}' in '{PublicApiFields.REQUEST_DATA}' must be a positive integer. f{search_to} > 0."
                )

            if search_to <= search_from:
                raise ValueError(
                    f"'{PublicApiFields.SEARCH_FROM}' must be less than '{PublicApiFields.SEARCH_TO}'. f{search_from} < f{search_to}"
                )

            self._search_from = search_from
            self._search_to = search_to

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    @property
    def total(self) -> int:
        """
        Returns the total number of results. (Max for most data types is 9_999).
        """
        return self._total

    def next(self) -> Dict[str, Any]:
        """
        Fetches the result from pagination.next, if a value exists.
        """
        if not self.has_next():
            raise StopIteration("Pagination exhausted")

        return self._get_data()

    def has_next(self) -> bool:
        """
        True when there's another page of data, False when pagination is complete.
        """
        if self._pages == 0:
            return True

        if self._use_page_token:
            return self._next_page_token is not None
        else:
            # Some APIs will limit the total to 9_999. Only use this logic if the total < 9_999.
            if self._total < MAX_TOTAL_COUNT:
                return self._search_from < self._total
            # When the total >= 9_999, look at the previous page size. If zero, the results are exhausted.
            else:
                return self._last_results_count is None or self._last_results_count > 0

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
            if self._use_page_token:
                resp = self._get_data_with_page_token()
            else:
                resp = self._get_data_with_limit_offset()

            resp_as_json = resp.json()  # type: ignore

            self._pages += 1

            self._next_page_token = resp_as_json.get(PublicApiFields.REPLY, {}).get(
                PublicApiFields.NEXT_PAGE_TOKEN, None
            )

            self._last_results_count = resp_as_json.get(PublicApiFields.REPLY, {}).get(
                PublicApiFields.RESULTS_COUNT,
                len(resp_as_json[PublicApiFields.REPLY][self._data_key]),
            )

            self._total = resp_as_json.get(PublicApiFields.REPLY, {}).get(
                PublicApiFields.TOTAL_COUNT, 0
            )

            return resp_as_json[PublicApiFields.REPLY][self._data_key]
        except (KeyError, TypeError) as err:
            raise UnexpectedResponseError(
                f"XpanseResultIterator received unexpected response: {resp_as_json}"
            ) from err

    def _get_data_with_page_token(self) -> Response:
        """
        When `use_page_token` is True, this method is used to paginate the responses using a page token
        """
        if self._pages >= 1:
            extra_request_data: Dict[str, Any] = {
                PublicApiFields.NEXT_PAGE_TOKEN: self._next_page_token
            }
            self._kwargs = build_request_payload(
                extra_request_data=extra_request_data, **self._kwargs
            )
            return self._api.post(self._path, **self._kwargs)
        else:
            extra_request_data = {PublicApiFields.USE_PAGE_TOKEN: True}
            self._kwargs = build_request_payload(
                extra_request_data=extra_request_data, **self._kwargs
            )
            return self._api.post(self._path, **self._kwargs)

    def _get_data_with_limit_offset(self) -> Response:
        """
        When `use_page_token` is False, this method is used to paginate the responses using
        the `search_from` and `search_to` fields in the `request` data. This behaves as
        limit-offest pagination
        """
        extra_request_data: Dict[str, Any] = {
            PublicApiFields.SEARCH_FROM: self._search_from,
            PublicApiFields.SEARCH_TO: self._search_to,
        }
        self._kwargs = build_request_payload(
            extra_request_data=extra_request_data, **self._kwargs
        )
        resp = self._api.post(self._path, **self._kwargs)

        # Increment offset and limit using search_from and search_to
        limit = self._search_to - self._search_from
        self._search_from = self._search_to
        self._search_to += limit

        return resp
