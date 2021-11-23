import pytest

from xpanse.iterator import ExResultIterator


@pytest.mark.vcr()
def test_assets_ip_range_list(api):
    i = api.assets.ip_range.v2.list()
    assert isinstance(
        i, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."
    assert isinstance(i.next(), list), "Expected that next should return a list."


@pytest.mark.vcr()
def test_assets_ip_range_get(api):
    ip_range = api.assets.ip_range.v2.get("07a03fce-df64-38ee-a024-1ea84d2df18c")
    assert isinstance(ip_range, dict)


@pytest.mark.vcr()
def test_assets_ip_range_create(api):
    start = "2.117.113.130"
    end = "2.117.113.135"
    parent_id = "01dd9d37-b0fe-3014-a17a-7db042383a00"
    ip_range = api.assets.ip_range.v2.create(start, end, parent_id)
    assert isinstance(ip_range, dict), "Expected instance of `dict` to be returned."
    assert ip_range["id"] is not None
    assert ip_range["startAddress"] == start
    assert ip_range["endAddress"] == end
    assert ip_range["parentId"] == parent_id
    assert api.assets.ip_range.v2.delete(ip_range["id"]), "Error cleaning up IP range"


@pytest.mark.vcr()
def test_assets_ip_range_delete(api):
    start = "2.117.113.130"
    end = "2.117.113.135"
    parent_id = "01dd9d37-b0fe-3014-a17a-7db042383a00"
    ip_range = api.assets.ip_range.v2.create(start, end, parent_id)
    assert ip_range["id"] is not None
    assert api.assets.ip_range.v2.delete(ip_range["id"])
    assert not api.assets.ip_range.v2.delete(
        ip_range["id"]
    ), "Expected `False` to be returned for non-existant ip_range id."


@pytest.mark.vcr()
def test_assets_ip_range_update(api):
    start = "2.117.113.130"
    end = "2.117.113.135"
    parent_id = "01dd9d37-b0fe-3014-a17a-7db042383a00"
    ip_range = api.assets.ip_range.v2.create(start, end, parent_id)
    assert ip_range["id"] is not None
    new_range = api.assets.ip_range.v2.update(
        ip_range["id"], endAddress="2.117.113.131"
    )
    assert new_range["startAddress"] == "2.117.113.130"
    assert new_range["endAddress"] == "2.117.113.131"
    assert api.assets.ip_range.v2.delete(ip_range["id"]), "Error cleaning up IP range"


@pytest.mark.vcr()
def test_assets_ip_range_tag(api):
    start = "2.117.113.130"
    end = "2.117.113.135"
    parent_id = "01dd9d37-b0fe-3014-a17a-7db042383a00"
    ip_range = api.assets.ip_range.v2.create(start, end, parent_id)
    assert ip_range["id"] is not None
    assert api.assets.ip_range.v2.tag(ranges=[ip_range["id"]], tags=["sdk_test_cc"])
    assert api.assets.ip_range.v2.delete(ip_range["id"]), "Error cleaning up IP range"
