import pytest

from xpanse.iterator import ExResultIterator


@pytest.mark.vcr()
def test_issues_business_units_list(api):
    i = api.issues.business_units.v1.list()
    assert isinstance(
        i, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."
    first = i.next()
    assert isinstance(first, list)
