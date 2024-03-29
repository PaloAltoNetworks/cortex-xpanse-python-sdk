from unittest.mock import MagicMock

import pytest

from tests.unit.test_iterator import MockResponse
from xpanse.const import DEFAULT_REQUEST_PAYLOAD_FIELD, PublicApiFields
from xpanse.iterator import XpanseResultIterator
from xpanse.response import XpanseResponse


@pytest.mark.vcr()
def test_OwnedIpRangesApi_list(api):
    _api = api.owned_ip_ranges

    expected_data = ["range1", "range2"]
    api.post = MagicMock(return_value=MockResponse(_api.LIST_DATA_KEY, expected_data))
    actual_kwargs = {DEFAULT_REQUEST_PAYLOAD_FIELD: {}}

    iterator = _api.list(**actual_kwargs)
    assert isinstance(iterator, XpanseResultIterator)

    expected_kwargs = {
        DEFAULT_REQUEST_PAYLOAD_FIELD: {
            PublicApiFields.REQUEST_DATA: {},
        },
    }
    assert actual_kwargs == expected_kwargs

    actual_data = iterator.next()
    assert actual_data == expected_data


@pytest.mark.vcr()
def test_OwnedIpRangesApi_get(api):
    _api = api.owned_ip_ranges

    expected_data = ["range1", "range2"]
    api.post = MagicMock(return_value=MockResponse(_api.GET_DATA_KEY, expected_data))

    actual_kwargs = {DEFAULT_REQUEST_PAYLOAD_FIELD: {}}
    object_ids = ["1", "2"]
    actual_data = _api.get(ip_range_ids=object_ids, **actual_kwargs)

    expected_kwargs = {
        DEFAULT_REQUEST_PAYLOAD_FIELD: {
            PublicApiFields.REQUEST_DATA: {
                "range_id_list": object_ids,
            },
        },
    }

    assert actual_kwargs == expected_kwargs
    assert isinstance(actual_data, XpanseResponse)
    assert actual_data.data == expected_data


@pytest.mark.vcr()
def test_OwnedIpRangesApi_count(api):
    _api = api.owned_ip_ranges

    expected_count = 1_111
    api.post = MagicMock(return_value=MockResponse(_api.LIST_DATA_KEY, None, total_count=expected_count))

    actual_kwargs = {DEFAULT_REQUEST_PAYLOAD_FIELD: {}}
    actual_count = _api.count(**actual_kwargs)

    expected_kwargs = {
        DEFAULT_REQUEST_PAYLOAD_FIELD: {
            PublicApiFields.REQUEST_DATA: {
                PublicApiFields.SEARCH_FROM: 0,
                PublicApiFields.SEARCH_TO: 1,
            },
        },
    }

    assert actual_kwargs == expected_kwargs
    assert isinstance(actual_count, XpanseResponse)
    assert actual_count.data == expected_count
