import pytest

from xpanse.iterator import ExResultIterator


@pytest.mark.vcr()
def test_services_country_codes_list(api):
    i = api.services.country_codes.list()
    assert isinstance(
        i, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."
    first = i.next()
    assert isinstance(first, list)
