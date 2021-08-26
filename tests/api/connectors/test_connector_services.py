import os
import pytest

from xpanse.iterator import ExResultIterator


@pytest.mark.vcr()
def test_connectors_services_list(api):
    services = api.connectors.services.list()
    assert isinstance(
        services, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."
    first = services.next()
    assert isinstance(first, list)
