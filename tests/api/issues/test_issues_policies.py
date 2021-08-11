import pytest

from expanse.iterator import ExResultIterator


@pytest.mark.vcr()
def test_issues_policies_list(api):
    i = api.issues.policies.v1.list()
    assert isinstance(
        i, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."


@pytest.mark.vcr()
def test_issues_policies_count(api):
    count = api.issues.policies.v1.count()
    assert isinstance(count.get("count"), int)
    assert isinstance(count.get("overflow"), bool)


@pytest.mark.vcr()
def test_issues_policies_get(api):
    issue = api.issues.policies.v1.get(id="ColocatedPptpServer")
    assert issue.get("issueTypeId") == "ColocatedPptpServer"


@pytest.mark.vcr()
def test_issues_policies_update(api):
    update = api.issues.policies.update(id="ColocatedPptpServer", enabled="On", priority="Low")
    assert update.get("issueTypeId") == "ColocatedPptpServer"
    assert update.get("priority") == "Low"
    assert update.get("enabledStatus") == "On"
