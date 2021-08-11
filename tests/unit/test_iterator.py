from unittest.mock import MagicMock

import pytest

from expanse.client import ExClient
from expanse.iterator import ExResultIterator


def test_ExResultIterator_clean_params(api):
    params = {"type_": "Test Value"}
    i = ExResultIterator(api, "fake/route", params)
    assert i._params.get("type") == "Test Value"


def test_ExResultIterator_next():
    mock_api = ExClient(jwt="1234")
    mock_api.get = MagicMock(return_value=MockResponse(1, "next"))
    mock_api.direct_get = MagicMock(return_value=MockResponse(2))
    i = ExResultIterator(mock_api, "fake/route", {})
    assert i.next() == 1
    assert i.next() == 2


def test_ExResultIterator_next_exhausted():
    mock_api = ExClient(jwt="1234")
    mock_api.get = MagicMock(return_value=MockResponse(1))
    i = ExResultIterator(mock_api, "fake/route", {})
    assert i.next() == 1
    with pytest.raises(StopIteration) as ex:
        i.next()
        assert ex.args == "Pagination exhausted"


class MockResponse:
    def __init__(self, val, next_=None):
        self._val = val
        self._next = next_

    def json(self):
        return {"data": self._val, "pagination": {"next": self._next}}
