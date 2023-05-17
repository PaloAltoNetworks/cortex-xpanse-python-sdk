from enum import Enum
from unittest.mock import MagicMock

import pytest

from tests.unit.test_iterator import MockResponse
from xpanse.const import (
    DEFAULT_REQUEST_PAYLOAD_FIELD,
    PublicApiFields,
    TaggableDataType,
)
from xpanse.response import XpanseResponse


@pytest.mark.vcr()
def test_TagsApi_assign_asset_tags(api):
    _api = api.tags

    expected_data = "succeeded"
    api.post = MagicMock(return_value=MockResponse(_api.ASSIGN_DATA_KEY, expected_data))

    actual_kwargs = {DEFAULT_REQUEST_PAYLOAD_FIELD: {}}
    object_ids = ["1", "2"]
    tags = ["tag1", "tag2"]
    filters = [{"field": "asm_id_list", "operator": "in", "value": object_ids}]
    actual_data = _api.assign(
        data_type=TaggableDataType.ASSETS, tags=tags, filters=filters, **actual_kwargs
    )

    expected_kwargs = {
        DEFAULT_REQUEST_PAYLOAD_FIELD: {
            PublicApiFields.REQUEST_DATA: {
                PublicApiFields.FILTERS: filters,
                PublicApiFields.TAGS: tags,
            }
        },
    }

    assert actual_kwargs == expected_kwargs
    assert isinstance(actual_data, XpanseResponse)
    assert actual_data.data == expected_data


@pytest.mark.vcr()
def test_TagsApi_assign_ip_range_tags(api):
    _api = api.tags

    expected_data = "succeeded"
    api.post = MagicMock(return_value=MockResponse(_api.ASSIGN_DATA_KEY, expected_data))

    actual_kwargs = {DEFAULT_REQUEST_PAYLOAD_FIELD: {}}
    object_ids = ["1", "2"]
    tags = ["tag1", "tag2"]
    filters = [{"field": "range_id_list", "operator": "in", "value": object_ids}]
    actual_data = _api.assign(
        data_type=TaggableDataType.EXTERNAL_IP_RANGES,
        tags=tags,
        filters=filters,
        **actual_kwargs,
    )

    expected_kwargs = {
        DEFAULT_REQUEST_PAYLOAD_FIELD: {
            PublicApiFields.REQUEST_DATA: {
                PublicApiFields.FILTERS: filters,
                PublicApiFields.TAGS: tags,
            }
        },
    }

    assert actual_kwargs == expected_kwargs
    assert isinstance(actual_data, XpanseResponse)
    assert actual_data.data == expected_data


@pytest.mark.vcr()
def test_TagsApi_assign_invalid_data_type(api):
    class FakeTaggableDataType(Enum):
        FAKE = "this_is_so_fake"

    _api = api.tags
    with pytest.raises(ValueError) as e:
        _api.assign(
            data_type=FakeTaggableDataType.FAKE, tags=["tag1", "tag2"], filters=[]
        )
        assert (
            str(e.value)
            == f"Invalid TaggableDataType: {FakeTaggableDataType.FAKE.value}"
        )


@pytest.mark.vcr()
def test_TagsApi_remove_asset_tags(api):
    _api = api.tags

    expected_data = "succeeded"
    api.post = MagicMock(return_value=MockResponse(_api.REMOVE_DATA_KEY, expected_data))

    actual_kwargs = {DEFAULT_REQUEST_PAYLOAD_FIELD: {}}
    object_ids = ["1", "2"]
    tags = ["tag1", "tag2"]
    filters = [{"field": "asm_id_list", "operator": "in", "value": object_ids}]
    actual_data = _api.remove(
        data_type=TaggableDataType.ASSETS, tags=tags, filters=filters, **actual_kwargs
    )

    expected_kwargs = {
        DEFAULT_REQUEST_PAYLOAD_FIELD: {
            PublicApiFields.REQUEST_DATA: {
                PublicApiFields.FILTERS: filters,
                PublicApiFields.TAGS: tags,
            }
        },
    }

    assert actual_kwargs == expected_kwargs
    assert isinstance(actual_data, XpanseResponse)
    assert actual_data.data == expected_data


@pytest.mark.vcr()
def test_TagsApi_remove_ip_range_tags(api):
    _api = api.tags

    expected_data = "succeeded"
    api.post = MagicMock(return_value=MockResponse(_api.REMOVE_DATA_KEY, expected_data))

    actual_kwargs = {DEFAULT_REQUEST_PAYLOAD_FIELD: {}}
    object_ids = ["1", "2"]
    tags = ["tag1", "tag2"]
    filters = [{"field": "range_id_list", "operator": "in", "value": object_ids}]
    actual_data = _api.remove(
        data_type=TaggableDataType.EXTERNAL_IP_RANGES,
        tags=tags,
        filters=filters,
        **actual_kwargs,
    )

    expected_kwargs = {
        DEFAULT_REQUEST_PAYLOAD_FIELD: {
            PublicApiFields.REQUEST_DATA: {
                PublicApiFields.FILTERS: filters,
                PublicApiFields.TAGS: tags,
            },
        },
    }

    assert actual_kwargs == expected_kwargs
    assert isinstance(actual_data, XpanseResponse)
    assert actual_data.data == expected_data


@pytest.mark.vcr()
def test_TagsApi_remove_invalid_data_type(api):
    class FakeTaggableDataType(Enum):
        FAKE = "this_is_so_fake"

    _api = api.tags
    with pytest.raises(ValueError) as e:
        _api.remove(data_type=FakeTaggableDataType.FAKE, tags=[], filters=[])
        assert (
            str(e.value)
            == f"Invalid TaggableDataType: {FakeTaggableDataType.FAKE.value}"
        )
