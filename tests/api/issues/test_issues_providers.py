import pytest

from expanse.iterator import ExResultIterator


@pytest.mark.vcr()
def test_issues_providers_list(api):
    i = api.issues.providers.v1.list()
    assert isinstance(
        i, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."
    first = i.next()
    assert isinstance(first, list)
