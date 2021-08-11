import pytest

from expanse.iterator import ExResultIterator


@pytest.mark.vcr()
def test_assets_ip_range_list(api):
    i = api.assets.ip_range.v2.list()
    assert isinstance(
        i, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."
    assert isinstance(i.next(), list), "Expected that next should return a list."


@pytest.mark.vcr()
def test_assets_ip_range_get(api):
    ip_range = api.assets.ip_range.v2.get("75ebc9d8-db03-4c00-b44b-db458d72c817")
    assert isinstance(ip_range, dict)


@pytest.mark.vcr()
def test_assets_ip_range_create(api):
    start = "2.117.113.128"
    end = "2.117.113.135"
    parent_id = "09ce0303-94e5-4037-8226-e708b6e4874f"
    ip_range = api.assets.ip_range.v2.create(start, end, parent_id)
    assert isinstance(ip_range, dict), "Expected instance of `dict` to be returned."
    assert ip_range["id"] is not None
    assert ip_range["startAddress"] == start
    assert ip_range["endAddress"] == end
    assert ip_range["parentId"] == parent_id
    assert api.assets.ip_range.v2.delete(ip_range["id"]), "Error cleaning up IP range"


@pytest.mark.vcr()
def test_assets_ip_range_delete(api):
    start = "2.117.113.128"
    end = "2.117.113.135"
    parent_id = "09ce0303-94e5-4037-8226-e708b6e4874f"
    ip_range = api.assets.ip_range.v2.create(start, end, parent_id)
    assert ip_range["id"] is not None
    assert api.assets.ip_range.v2.delete(ip_range["id"])
    assert not api.assets.ip_range.v2.delete(
        ip_range["id"]
    ), "Expected `False` to be returned for non-existant ip_range id."


@pytest.mark.vcr()
def test_assets_ip_range_update(api):
    start = "2.117.113.128"
    end = "2.117.113.135"
    parent_id = "09ce0303-94e5-4037-8226-e708b6e4874f"
    ip_range = api.assets.ip_range.v2.create(start, end, parent_id)
    assert ip_range["id"] is not None
    new_range = api.assets.ip_range.v2.update(
        ip_range["id"], endAddress="2.117.113.131"
    )
    assert new_range["startAddress"] == "2.117.113.128"
    assert new_range["endAddress"] == "2.117.113.131"
    assert api.assets.ip_range.v2.delete(ip_range["id"]), "Error cleaning up IP range"


@pytest.mark.vcr()
def test_assets_ip_range_tag(api):
    start = "2.117.113.128"
    end = "2.117.113.135"
    parent_id = "09ce0303-94e5-4037-8226-e708b6e4874f"
    ip_range = api.assets.ip_range.v2.create(start, end, parent_id)
    assert ip_range["id"] is not None
    assert api.assets.ip_range.v2.tag(ranges=[ip_range["id"]], tags=["test_tag"])
    assert api.assets.ip_range.v2.delete(ip_range["id"]), "Error cleaning up IP range"
