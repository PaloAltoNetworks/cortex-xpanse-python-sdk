import pytest

from expanse.iterator import ExResultIterator


@pytest.mark.vcr()
def test_services_classifications_list(api):
    i = api.services.classifications.list()
    assert isinstance(
        i, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."
    first = i.next()
    assert isinstance(first, list)
