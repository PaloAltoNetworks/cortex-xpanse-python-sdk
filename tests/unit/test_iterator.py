from typing import Any, List
from unittest.mock import MagicMock

import pytest

from xpanse.const import PublicApiFields
from xpanse.iterator import XpanseResultIterator


@pytest.mark.vcr()
def test_XpanseResultIterator_next(api):
    api.post = MagicMock(return_value=MockResponse("data", 1, "_next_page_token"))
    i = XpanseResultIterator(api=api, path="fake/route", data_key="data")
    assert i.next() == 1
    api.post = MagicMock(return_value=MockResponse("data", 2))
    assert i.next() == 2


@pytest.mark.vcr()
def test_XpanseResultIterator_has_next(api):
    api.post = MagicMock(return_value=MockResponse("data", 1, "_next_page_token"))
    i = XpanseResultIterator(api=api, path="fake/route", data_key="data")
    assert i.has_next()
    assert i.next() == 1
    assert i.has_next()

    api.post = MagicMock(return_value=MockResponse("data", 2))
    assert i.next() == 2
    assert not i.has_next()


@pytest.mark.vcr()
def test_XpanseResultIterator_next_exhausted(api):
    api.post = MagicMock(return_value=MockResponse("data", 1))
    i = XpanseResultIterator(api=api, path="fake/route", data_key="data")
    assert i.next() == 1
    with pytest.raises(StopIteration) as ex:
        i.next()
        assert ex.args == "Pagination exhausted"


class MockResponse:
    def __init__(self,
                 key: str,
                 val: List[Any],
                 next_page_token: str = None,
                 total_count: int = 1000,
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
