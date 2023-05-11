from unittest.mock import MagicMock

import pytest

from tests.unit.test_iterator import MockResponse
from xpanse.const import DEFAULT_REQUEST_PAYLOAD_FIELD, PublicApiFields
from xpanse.iterator import XpanseResultIterator


@pytest.mark.vcr()
def test_IncidentsApi_list(api):
    _api = api.incidents

    expected_data = ["incident1", "incident2"]
    api.post = MagicMock(return_value=MockResponse(_api.DATA_KEY, expected_data))
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
def test_IncidentsApi_get(api):
    _api = api.incidents

    expected_data = ["incident1", "incident2"]
    api.post = MagicMock(return_value=MockResponse(_api.DATA_KEY, expected_data))

    actual_kwargs = {DEFAULT_REQUEST_PAYLOAD_FIELD: {}}
    object_ids = [1, 2]
    actual_data = _api.get(incident_ids=object_ids, **actual_kwargs)

    expected_kwargs = {
        DEFAULT_REQUEST_PAYLOAD_FIELD: {
            PublicApiFields.REQUEST_DATA: {
                PublicApiFields.FILTERS: [{"field": "incident_id_list", "operator": "in", "value": object_ids}],
            },
        },
    }

    assert actual_kwargs == expected_kwargs
    assert actual_data == expected_data


@pytest.mark.vcr()
def test_IncidentsApi_count(api):
    _api = api.incidents

    expected_count = 1_111
    api.post = MagicMock(return_value=MockResponse(_api.DATA_KEY, None, total_count=expected_count))
    
    actual_kwargs = {DEFAULT_REQUEST_PAYLOAD_FIELD: {}}
    actual_count = _api.count(**actual_kwargs)

    expected_kwargs = {
        DEFAULT_REQUEST_PAYLOAD_FIELD: {
            PublicApiFields.REQUEST_DATA: {},
        },
    }

    assert actual_kwargs == expected_kwargs
    assert actual_count == expected_count


@pytest.mark.vcr()
def test_IncidentsApi_update(api):
    _api = api.incidents

    expected_response = True
    api.post = MagicMock(return_value=expected_response)

    actual_kwargs = {DEFAULT_REQUEST_PAYLOAD_FIELD: {}}

    update_data = {"test": "data"}
    update_ids = ["1", "2"]
    actual_response = _api.update(incident_ids=update_ids, update_data=update_data, **actual_kwargs)

    expected_kwargs = {
        DEFAULT_REQUEST_PAYLOAD_FIELD: {
            PublicApiFields.REQUEST_DATA: {
                "incident_id_list": update_ids,
                "update_data": update_data,
            },
        },
    }

    assert actual_kwargs == expected_kwargs
    assert actual_response == expected_response
