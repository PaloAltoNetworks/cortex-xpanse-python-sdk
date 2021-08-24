import os
import pytest

from xpanse.iterator import ExResultIterator
from conftest import TEST_ISSUE_ID, TEST_ISSUE_UPDATE_ID


@pytest.mark.vcr()
def test_issues_issues_list(api):
    i = api.issues.issues.v1.list()
    assert isinstance(
        i, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."


@pytest.mark.vcr()
def test_issues_issues_count(api):
    count = api.issues.issues.v1.count(providerId="AWS")
    assert isinstance(count.get("count"), int)
    assert isinstance(count.get("overflow"), bool)


@pytest.mark.vcr()
def test_issues_issues_get(api):
    issue = api.issues.issues.v1.get(id=TEST_ISSUE_ID)
    assert issue.get("id") == TEST_ISSUE_ID


@pytest.mark.vcr()
def test_issues_issues_get_updates(api):
    updates = api.issues.issues.v1.get_updates(id=TEST_ISSUE_ID)
    assert isinstance(
        updates, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."


@pytest.mark.vcr()
def test_issues_issues_get_update(api):
    update_details = api.issues.issues.v1.get_update(
        id=TEST_ISSUE_ID, update_id=TEST_ISSUE_UPDATE_ID
    )
    assert update_details.get("id") == TEST_ISSUE_UPDATE_ID


@pytest.mark.vcr()
def test_issues_issues_update(api):
    update_resp = api.issues.issues.v1.update(
        id=TEST_ISSUE_ID, value="SDK TEST Comment", updateType="Comment"
    )
    update_details = api.issues.issues.get_update(
        id=TEST_ISSUE_ID, update_id=update_resp.get("id")
    )
    assert update_details.get("id") == update_resp.get("id")
    assert update_details.get("value") == "SDK TEST Comment"


@pytest.mark.vcr()
def test_issues_issues_get_bulk_update(api):
    value = "SDK Test Comment2"
    updateType = "Comment"
    update = (TEST_ISSUE_ID, value, updateType)
    bulk_resp = api.issues.issues.v1.bulk_update(updates=[update])
    assert bulk_resp.get("meta").get("failureCount") == 0
    assert len(bulk_resp.get("data")) == 1
    assert bulk_resp.get("data")[0].get("status") == "Success"


@pytest.mark.vcr()
def test_issues_issues_csv(api):
    file_name = "insecure_tls.csv"
    assert api.issues.issues.v1.csv(file=file_name, issueTypeId="InsecureTLS")
    assert os.path.isfile(file_name)
    assert os.path.getsize(file_name) > 0
    os.remove(file_name)
