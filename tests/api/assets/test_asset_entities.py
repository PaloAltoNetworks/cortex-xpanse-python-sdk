import pytest

from expanse.iterator import ExResultIterator


@pytest.mark.vcr()
def test_assets_entities_list(api):
    i = api.assets.entities.v2.list()
    assert isinstance(
        i, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."
    assert isinstance(i.next(), list), "Expected that next should return a list."
