import pytest

from expanse.iterator import ExResultIterator


@pytest.mark.vcr()
def test_issues_updates_list(api):
    i = api.issues.updates.v1.list(
        createdAfter="2020-07-20T00:00:00Z",
        createdBefore="2020-07-21T00:00:00Z",
        limit=5,
    )
    assert isinstance(
        i, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."
    first = i.next()
    assert isinstance(first, list), "Expected that next should return a list."
    assert len(first) == 5, "Expected limit of 5 to be observed."
