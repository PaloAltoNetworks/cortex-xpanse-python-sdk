from enum import Enum
from unittest.mock import MagicMock

import pytest

from tests.unit.test_iterator import MockResponse
from xpanse.api.asset_management.v1.assets import AssetsApi
from xpanse.const import DEFAULT_REQUEST_PAYLOAD_FIELD, PublicApiFields, AssetType
from xpanse.iterator import XpanseResultIterator
from xpanse.response import XpanseResponse


@pytest.mark.vcr()
def test_AssetsApi_list(api):
    _api = api.assets

    expected_data = ["asset1", "asset2"]
    api.post = MagicMock(return_value=MockResponse(_api.LIST_DATA_KEY, expected_data))
    actual_kwargs = {DEFAULT_REQUEST_PAYLOAD_FIELD: {}}

    iterator = _api.list(**actual_kwargs)
    assert isinstance(iterator, XpanseResultIterator)

    expected_kwargs = {
        DEFAULT_REQUEST_PAYLOAD_FIELD: {
            PublicApiFields.REQUEST_DATA: {
                PublicApiFields.FILTERS: [],
            },
        },
    }
    assert actual_kwargs == expected_kwargs

    actual_data = iterator.next()
    assert actual_data == expected_data


@pytest.mark.vcr()
def test_AssetsApi_get(api):
    _api = api.assets

    expected_data = ["asset1", "asset2"]
    api.post = MagicMock(return_value=MockResponse(_api.GET_DATA_KEY, expected_data))

    actual_kwargs = {DEFAULT_REQUEST_PAYLOAD_FIELD: {}}
    object_ids = ["1", "2"]
    actual_data = _api.get(asset_ids=object_ids, **actual_kwargs)

    expected_kwargs = {
        DEFAULT_REQUEST_PAYLOAD_FIELD: {
            PublicApiFields.REQUEST_DATA: {
                "asm_id_list": object_ids,
            },
        },
    }

    assert actual_kwargs == expected_kwargs
    assert isinstance(actual_data, XpanseResponse)
    assert actual_data.data == expected_data


@pytest.mark.vcr()
def test_AssetsApi_count(api):
    _api = api.assets

    expected_count = 1_111
    api.post = MagicMock(return_value=MockResponse(_api.LIST_DATA_KEY, None, total_count=expected_count))

    actual_kwargs = {DEFAULT_REQUEST_PAYLOAD_FIELD: {}}
    actual_count = _api.count(**actual_kwargs)

    expected_kwargs = {
        DEFAULT_REQUEST_PAYLOAD_FIELD: {
            PublicApiFields.REQUEST_DATA: {
                PublicApiFields.FILTERS: [],
                PublicApiFields.SEARCH_FROM: 0,
                PublicApiFields.SEARCH_TO: 1,
            },
        },
    }

    assert actual_kwargs == expected_kwargs
    assert isinstance(actual_count, XpanseResponse)
    assert actual_count.data == expected_count


@pytest.mark.vcr()
def test_AssetsApi_asset_type_count(api):
    _api = api.assets

    expected_count = 1_111
    api.post = MagicMock(return_value=MockResponse(_api.LIST_DATA_KEY, None, total_count=expected_count))

    actual_kwargs = {DEFAULT_REQUEST_PAYLOAD_FIELD: {}}
    actual_count = _api.count(asset_types={AssetType.DOMAIN, AssetType.CERTIFICATE}, **actual_kwargs)

    expected_kwargs = {
        DEFAULT_REQUEST_PAYLOAD_FIELD: {
            PublicApiFields.REQUEST_DATA: {
                PublicApiFields.FILTERS: [{"field": "type", "operator": "in", "value": ["domain", "certificate"]}],
                PublicApiFields.SEARCH_FROM: 0,
                PublicApiFields.SEARCH_TO: 1,
            },
        },
    }

    assert actual_kwargs == expected_kwargs
    assert isinstance(actual_count, XpanseResponse)
    assert actual_count.data == expected_count


@pytest.mark.vcr()
def test_AssetsApi_asset_type_list(api):
    _api = api.assets_api = api.assets

    expected_data = ["asset1", "asset2"]
    api.post = MagicMock(return_value=MockResponse(_api.LIST_DATA_KEY, expected_data))
    actual_kwargs = {DEFAULT_REQUEST_PAYLOAD_FIELD: {}}

    iterator = _api.list(asset_types={AssetType.RESPONSIVE_IP, AssetType.CLOUD_RESOURCES}, **actual_kwargs)
    assert isinstance(iterator, XpanseResultIterator)

    expected_kwargs = {
        DEFAULT_REQUEST_PAYLOAD_FIELD: {
            PublicApiFields.REQUEST_DATA: {
                PublicApiFields.FILTERS: [
                    {
                        "field": "type",
                        "operator": "in",
                        "value": ["unassociated_responsive_ip", "cloud_compute_instance"]
                    },
                ],
            },
        },
    }
    assert actual_kwargs == expected_kwargs

    actual_data = iterator.next()
    assert actual_data == expected_data


@pytest.mark.vcr()
def test_AssetsApi_build_asset_type_filters_none(api):
    filters = AssetsApi._build_asset_type_filters()
    assert filters == []


@pytest.mark.vcr()
def test_AssetsApi_build_asset_type_filters_success(api):
    asset_types = {AssetType.DOMAIN, AssetType.CERTIFICATE}
    filters = AssetsApi._build_asset_type_filters(asset_types=asset_types)
    assert len(filters) == 1
    assert filters[0]['field'] == 'type'
    assert filters[0]['operator'] == 'in'
    assert set(filters[0]['value']) == {'domain', 'certificate'}


@pytest.mark.vcr()
def test_AssetsApi_build_asset_type_filters_invalid(api):
    class FakeTypes(Enum):
        FAKE_TYPE = 'look_at_me_im_fake'

    asset_types = {AssetType.DOMAIN, AssetType.CERTIFICATE, FakeTypes.FAKE_TYPE}

    with pytest.raises(ValueError) as e:
        AssetsApi._build_asset_type_filters(asset_types=asset_types)
        assert str(e.value) == "Invalid AssetType provided: look_at_me_im_fake"
