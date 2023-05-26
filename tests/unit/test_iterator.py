from typing import Any, List
from unittest.mock import MagicMock

import pytest

from xpanse.const import PublicApiFields, DEFAULT_SEARCH_TO, MAX_TOTAL_COUNT, DEFAULT_SEARCH_FROM
from xpanse.iterator import XpanseResultIterator


@pytest.mark.vcr()
def test_XpanseResultIterator_next_page_token(api):
    api.post = MagicMock(return_value=MockResponse("data", [1], "_next_page_token"))
    i = XpanseResultIterator(api=api, path="fake/route", data_key="data")
    assert i.next() == [1]
    api.post = MagicMock(return_value=MockResponse("data", [2]))
    assert i.next() == [2]
    assert not hasattr(i, '_search_from')
    assert not hasattr(i, '_search_to')


@pytest.mark.vcr()
def test_XpanseResultIterator_has_next_page_token(api):
    api.post = MagicMock(return_value=MockResponse("data", [1], "_next_page_token"))
    i = XpanseResultIterator(api=api, path="fake/route", data_key="data")
    assert i.has_next()
    assert i.next() == [1]
    assert i.has_next()

    api.post = MagicMock(return_value=MockResponse("data", [2]))
    assert i.next() == [2]
    assert not i.has_next()
    assert not hasattr(i, '_search_from')
    assert not hasattr(i, '_search_to')


@pytest.mark.vcr()
def test_XpanseResultIterator_next_exhausted_page_token(api):
    i = XpanseResultIterator(api=api, path="fake/route", data_key="data")
    api.post = MagicMock(return_value=MockResponse("data", [1]))
    assert i.next() == [1]
    with pytest.raises(StopIteration) as ex:
        i.next()
        assert ex.args == "Pagination exhausted"
    assert not hasattr(i, '_search_from')
    assert not hasattr(i, '_search_to')


@pytest.mark.vcr()
def test_XpanseResultIterator_next_limit_offset(api):
    i = XpanseResultIterator(api=api, path="fake/route", data_key="data", use_page_token=False)
    limit = DEFAULT_SEARCH_TO - DEFAULT_SEARCH_FROM

    api.post = MagicMock(return_value=MockResponse("data", [1], "_next_page_token"))
    assert i._search_from == DEFAULT_SEARCH_FROM
    assert i._search_to == DEFAULT_SEARCH_TO

    assert i.next() == [1]
    assert i._search_from == DEFAULT_SEARCH_TO
    assert i._search_to == DEFAULT_SEARCH_TO + limit

    api.post = MagicMock(return_value=MockResponse("data", [2]))
    assert i.next() == [2]
    assert i._search_from == DEFAULT_SEARCH_TO + limit
    assert i._search_to == DEFAULT_SEARCH_TO + (limit * 2)


@pytest.mark.vcr()
def test_XpanseResultIterator_has_next_limit_offset_over_9999(api):
    i = XpanseResultIterator(api=api, path="fake/route", data_key="data", use_page_token=False, total_count=MAX_TOTAL_COUNT)
    limit = DEFAULT_SEARCH_TO - DEFAULT_SEARCH_FROM

    api.post = MagicMock(return_value=MockResponse("data", [1], "_next_page_token"))
    assert i.has_next()
    assert i._search_from == DEFAULT_SEARCH_FROM
    assert i._search_to == DEFAULT_SEARCH_TO
    assert i.next() == [1]

    api.post = MagicMock(return_value=MockResponse("data", [2], total_count=MAX_TOTAL_COUNT))
    assert i.has_next()
    assert i._search_from == DEFAULT_SEARCH_TO
    assert i._search_to == DEFAULT_SEARCH_TO + limit
    assert i.next() == [2]

    api.post = MagicMock(return_value=MockResponse("data", [], total_count=MAX_TOTAL_COUNT, results_count=0))
    assert i.has_next()
    assert i._search_from == DEFAULT_SEARCH_TO + limit
    assert i._search_to == DEFAULT_SEARCH_TO + (limit * 2)
    assert i.next() == []

    assert not i.has_next()
    assert i._search_from == DEFAULT_SEARCH_TO + (limit * 2)
    assert i._search_to == DEFAULT_SEARCH_TO + (limit * 3)


@pytest.mark.vcr()
def test_XpanseResultIterator_has_next_limit_offset_under_9999(api):
    i = XpanseResultIterator(api=api, path="fake/route", data_key="data", use_page_token=False)
    limit = DEFAULT_SEARCH_TO - DEFAULT_SEARCH_FROM

    api.post = MagicMock(return_value=MockResponse("data", [1], "_next_page_token", total_count=DEFAULT_SEARCH_TO + 1))
    assert i.has_next()
    assert i._search_from == DEFAULT_SEARCH_FROM
    assert i._search_to == DEFAULT_SEARCH_TO
    assert i.next() == [1]

    assert i.has_next()
    assert i._search_from == DEFAULT_SEARCH_TO
    assert i._search_to == DEFAULT_SEARCH_TO + limit
    assert i.next() == [1]

    assert not i.has_next()
    assert i._search_from == DEFAULT_SEARCH_TO + limit
    assert i._search_to == DEFAULT_SEARCH_TO + (limit * 2)


@pytest.mark.vcr()
def test_XpanseResultIterator_next_exhausted_limit_offset(api):
    i = XpanseResultIterator(api=api, path="fake/route", data_key="data", use_page_token=False)
    api.post = MagicMock(return_value=MockResponse("data", [1, 2], total_count=2))
    assert i.next() == [1, 2]
    with pytest.raises(StopIteration) as ex:
        i.next()
        assert ex.args == "Pagination exhausted"


def test_XpanseResultIterator_invalid_search_from():
    with pytest.raises(ValueError) as ex:
        XpanseResultIterator(api=None, path="fake/route", data_key="data", search_from=-1, use_page_token=False)
        assert ex.args == f"'{PublicApiFields.SEARCH_FROM}' in '{PublicApiFields.REQUEST_DATA}' must be a positive integer. -1 > 0."


def test_XpanseResultIterator_invalid_search_to():
    with pytest.raises(ValueError) as ex:
        XpanseResultIterator(api=None, path="fake/route", data_key="data", search_to=-1, use_page_token=False)
        assert ex.args == f"'{PublicApiFields.SEARCH_TO}' in '{PublicApiFields.REQUEST_DATA}' must be a positive integer. -1 > 0."


def test_XpanseResultIterator_invalid_search_from_search_to():
    with pytest.raises(ValueError) as ex:
        XpanseResultIterator(api=None, path="fake/route", data_key="data", search_to=5, search_from=6, use_page_token=False)
        assert ex.args == f"'{PublicApiFields.SEARCH_FROM}' must be less than '{PublicApiFields.SEARCH_TO}'. 6 < 5"

    with pytest.raises(ValueError) as ex:
        XpanseResultIterator(api=None, path="fake/route", data_key="data", search_to=5, search_from=5, use_page_token=False)
        assert ex.args == f"'{PublicApiFields.SEARCH_FROM}' must be less than '{PublicApiFields.SEARCH_TO}'. 5 < 5"


class MockResponse:
    def __init__(self,
                 key: str,
                 val: List[Any],
                 next_page_token: str = None,
                 total_count: int = 1_000,
                 results_count: int = 100):
        self._key = key
        self._val = val
        self._next = next_page_token
        self._total_count = total_count
        self._results_count = results_count

    def json(self):
        return {
            PublicApiFields.REPLY: {
                PublicApiFields.TOTAL_COUNT: self._total_count,
                PublicApiFields.RESULTS_COUNT: self._results_count,
                self._key: self._val,
                PublicApiFields.NEXT_PAGE_TOKEN: self._next,
            }
        }
