import logging
from typing import Any, Dict, List, Optional

from xpanse.error import UnexpectedResponseError


class ExResultIterator:
    """
    Iterator for paging though results.
    """

    # Total number of results - may not be available
    _total: int = 0

    # Pages seen so far
    _pages: int = 0

    # Location of next page
    _next_url: Optional[str] = None

    def __init__(self, api: Any, path: str, args: Dict[str, Any]):
        self._api = api
        self._path = path
        self._params = self._clean_params(args)
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
        if self._next_url is None and self._pages >= 1:
            raise StopIteration("Pagination exhausted")

        return self._get_data()

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
                resp = self._api.direct_get(self._next_url)
            else:
                resp = self._api.get(self._path, params=self._params)
            resp_as_json = resp.json()  # type: ignore

            self._pages += 1
            self._next_url = resp_as_json.get("pagination", {}).get("next", None)
            self._total = (
                resp_as_json.get("meta").get("totalCount", 0)
                if resp_as_json.get("meta") is not None
                else 0
            )
            return resp_as_json["data"]
        except KeyError as err:
            raise UnexpectedResponseError(
                "ExResultIterator received unexpected response"
            ) from err

    def _clean_params(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Some param names utilize python required keywords.
        """
        if "type_" in params:
            params["type"] = params.pop("type_")
        return params
