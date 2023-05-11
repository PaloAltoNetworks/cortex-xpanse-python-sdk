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
    def __init__(self, key: str, val: List[Any], next_page_token=None):
        self._key = key
        self._val = val
        self._next = next_page_token

    def json(self):
        return {
            "reply": {
                PublicApiFields.TOTAL_COUNT: 6036,
                PublicApiFields.RESULTS_COUNT: 1000,
                self._key: self._val,
                PublicApiFields.NEXT_PAGE_TOKEN: self._next,
            }
        }
