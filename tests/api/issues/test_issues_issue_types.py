import pytest

from expanse.iterator import ExResultIterator


@pytest.mark.vcr()
def test_issues_issue_types_list(api):
    i = api.issues.issue_types.v1.list()
    assert isinstance(
        i, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."
    first = i.next()
    assert isinstance(first, list)
