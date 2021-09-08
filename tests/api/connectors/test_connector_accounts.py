import os
import pytest

from xpanse.iterator import ExResultIterator
from conftest import TEST_CONNECTOR_ACCOUNT_ID


@pytest.mark.vcr()
def test_connectors_accounts_list(api):
    services = api.connectors.accounts.list()
    assert isinstance(
        services, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."
    first = services.next()
    assert isinstance(first, list)

@pytest.mark.vcr()
def test_connectors_accounts_get(api):
    connector_account = api.connectors.accounts.v1.get(id=TEST_CONNECTOR_ACCOUNT_ID)
    assert connector_account.get("id") == TEST_CONNECTOR_ACCOUNT_ID