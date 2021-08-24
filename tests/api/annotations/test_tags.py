import pytest

from xpanse.iterator import ExResultIterator
from conftest import TEST_TAG_NAME, TEST_TAG_ID


@pytest.mark.vcr()
def test_annotations_tags_list(api):
    i = api.annotations.tags.list()
    assert isinstance(
        i, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."
    assert isinstance(i.next(), list), "Expected that next should return a list."


@pytest.mark.vcr()
def test_annotations_tags_get(api):
    tag = api.annotations.tags.get(tag_id=TEST_TAG_ID)
    assert isinstance(tag, dict), "Expected instance of `dict` to be returned."
    assert tag["id"] == TEST_TAG_ID
    assert tag["name"] == TEST_TAG_NAME


@pytest.mark.vcr()
def test_annotations_tags_create(api):
    # We will disable this initially because tags cannot be deleted.
    tag = api.annotations.tags.create(
        name="sdk_test4",
        description="This is a test tag created by the SDK",
        disabled=True,
    )
    assert isinstance(tag, dict), "Expected instance of `dict` to be returned."
    assert tag["disabled"] == True


@pytest.mark.vcr()
def test_annotations_tags_update(api):
    tag = api.annotations.tags.update(tag_id=TEST_TAG_ID, disabled=True)
    assert isinstance(tag, dict), "Expected instance of `dict` to be returned."
    assert tag["disabled"] == True
    tag = api.annotations.tags.update(tag_id=TEST_TAG_ID, disabled=False)
    assert tag["disabled"] == False
