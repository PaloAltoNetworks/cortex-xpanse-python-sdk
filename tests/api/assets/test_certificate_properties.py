import pytest

from expanse.iterator import ExResultIterator


@pytest.mark.vcr()
def test_assets_certificate_properties_list(api):
    i = api.assets.certificate_properties.v2.list()
    assert isinstance(
        i, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."
    assert isinstance(i.next(), list), "Expected that next should return a list."
