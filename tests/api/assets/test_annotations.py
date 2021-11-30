import pytest

from xpanse.iterator import ExResultIterator
from conftest import TEST_TAG_NAME_ASSET_ANNOTATIONS, TEST_ASSETS_TAG_ID


@pytest.mark.vcr()
def test_assets_annotations_list_tag(api):
    i = api.assets.annotations.v2.list_tag()
    assert isinstance(
        i, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."
    assert isinstance(i.next(), list), "Expected that next should return a list."


@pytest.mark.vcr()
def test_assets_annotations_create_tag(api):
    tag = api.assets.annotations.v2.create_tag(f"{TEST_TAG_NAME_ASSET_ANNOTATIONS}")
    assert isinstance(tag, dict), "Expected instance of `dict` to be returned."
    assert tag["name"] == f"{TEST_TAG_NAME_ASSET_ANNOTATIONS}"
    assert tag["id"] is not None


@pytest.mark.vcr()
def test_assets_annotations_get_tag(api):
    tag_get = api.assets.annotations.v2.get_tag(TEST_ASSETS_TAG_ID)
    assert isinstance(tag_get, dict), "Expected instance of `dict` to be returned."


@pytest.mark.vcr()
def test_assets_annotations_list_poc(api):
    i = api.assets.annotations.v2.list_poc()
    assert isinstance(
        i, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."
    assert isinstance(i.next(), list), "Expected that next should return a list."


@pytest.mark.vcr()
def test_assets_annotations_create_poc(api):
    poc = api.assets.annotations.v2.create_poc(
        "sdk.tester@expanse.co",
        firstName="SDK",
        lastName="Tester",
        phone="555-555-5555",
        role="QA",
    )
    assert isinstance(poc, dict), "Expected instance of `dict` to be returned."
    assert poc["email"] == "sdk.tester@expanse.co"
    assert poc["id"] is not None
    assert api.assets.annotations.v2.delete_poc(poc["id"]), "Error cleaning up poc"


@pytest.mark.vcr()
def test_assets_annotations_get_poc(api):
    poc = api.assets.annotations.v2.create_poc(
        "sdk.tester@expanse.co",
        firstName="SDK",
        lastName="Tester",
        phone="555-555-5555",
        role="QA",
    )
    assert poc["id"] is not None
    poc_get = api.assets.annotations.v2.get_poc(poc["id"])
    assert isinstance(poc_get, dict), "Expected instance of `dict` to be returned."
    for key in poc.keys() & poc_get.keys():
        assert poc[key] == poc_get[key]
    assert api.assets.annotations.v2.delete_poc(poc["id"]), "Error cleaning up poc"


@pytest.mark.vcr()
def test_assets_annotations_delete_poc(api):
    poc = api.assets.annotations.v2.create_poc(
        "sdk.tester@expanse.co",
        firstName="SDK",
        lastName="Tester",
        phone="555-555-5555",
        role="QA",
    )
    assert poc["id"] is not None
    assert api.assets.annotations.v2.delete_poc(poc["id"])
    assert not api.assets.annotations.v2.delete_poc(
        poc["id"]
    ), "Expected `False` to be returned for non-existant poc id."
