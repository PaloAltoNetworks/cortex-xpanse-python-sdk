from unittest.mock import MagicMock

import pytest

from tests.unit.test_iterator import MockResponse
from xpanse.const import DEFAULT_REQUEST_PAYLOAD_FIELD, PublicApiFields
from xpanse.iterator import XpanseResultIterator
from xpanse.response import XpanseResponse


@pytest.mark.vcr()
def test_AttackSurfaceRulesApi_list(api):
    _api = api.attack_surface_rules

    expected_data = ["rule1", "rule2"]
    api.post = MagicMock(return_value=MockResponse(_api.DATA_KEY, [expected_data[0]], results_count=1, total_count=2))
    actual_kwargs = {
        DEFAULT_REQUEST_PAYLOAD_FIELD: {}
    }
    request_data = {
        PublicApiFields.SEARCH_FROM: 0,
        PublicApiFields.SEARCH_TO: 1,
    }

    i = _api.list(request_data=request_data, **actual_kwargs)

    expected_kwargs = {
        DEFAULT_REQUEST_PAYLOAD_FIELD: {
            PublicApiFields.REQUEST_DATA: {
                PublicApiFields.SEARCH_FROM: 0,
                PublicApiFields.SEARCH_TO: 1,
            },
        },
    }

    assert actual_kwargs == expected_kwargs
    assert isinstance(i, XpanseResultIterator)

    assert i._search_from == 0
    assert i._search_to == 1
    assert i.has_next()
    assert i.next() == [expected_data[0]]

    api.post = MagicMock(return_value=MockResponse(_api.DATA_KEY, [expected_data[1]], results_count=1, total_count=2))
    assert i._search_from == 1
    assert i._search_to == 2
    assert i.has_next()
    assert i.next() == [expected_data[1]]

    assert not i.has_next()


@pytest.mark.vcr()
def test_AttackSurfaceRulesApi_get(api):
    _api = api.attack_surface_rules

    expected_data = ["rule1", "rule2"]
    api.post = MagicMock(return_value=MockResponse(_api.DATA_KEY, expected_data))

    actual_kwargs = {DEFAULT_REQUEST_PAYLOAD_FIELD: {}}
    object_ids = ["1", "2"]
    actual_data = _api.get(attack_surface_rule_ids=object_ids, **actual_kwargs)

    expected_kwargs = {
        DEFAULT_REQUEST_PAYLOAD_FIELD: {
            PublicApiFields.REQUEST_DATA: {
                PublicApiFields.FILTERS: [{
                    "field": "attack_surface_rule_id",
                    "operator": "in",
                    "value": object_ids,
                }],
            }
        },
    }

    assert actual_kwargs == expected_kwargs
    assert isinstance(actual_data, XpanseResponse)
    assert actual_data.data == expected_data


@pytest.mark.vcr()
def test_AttackSurfaceRulesApi_count(api):
    _api = api.attack_surface_rules

    expected_count = 1_111
    api.post = MagicMock(return_value=MockResponse(_api.DATA_KEY, None, total_count=expected_count))

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
