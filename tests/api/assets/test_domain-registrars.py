import pytest

from xpanse.iterator import ExResultIterator


@pytest.mark.vcr()
def test_assets_domain_registrars_list(api):
    i = api.assets.domain_registrars.v2.list()
    assert isinstance(
        i, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."
    assert isinstance(i.next(), list), "Expected that next should return a list."
