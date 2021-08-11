import os
import pytest

from expanse.iterator import ExResultIterator
from conftest import TEST_SERVICE_ID


@pytest.mark.vcr()
def test_services_services_list(api):
    i = api.services.services.v1.list()
    assert isinstance(
        i, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."
    first = i.next()
    assert isinstance(first, list)


@pytest.mark.vcr()
def test_services_services_count(api):
    count = api.services.services.v1.count(providerId="AWS")
    assert isinstance(count.get("count"), int)
    assert isinstance(count.get("overflow"), bool)


@pytest.mark.vcr()
def test_services_services_get(api):
    issue = api.services.services.v1.get(id=TEST_SERVICE_ID)
    assert issue.get("id") == TEST_SERVICE_ID


@pytest.mark.vcr()
def test_services_services_updates(api):
    i = api.services.services.v1.updates()
    assert isinstance(
        i, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."
    first = i.next()
    assert isinstance(first, list)


@pytest.mark.vcr()
def test_services_services_csv(api):
    file_name = "dns_server_service.csv"
    assert api.services.services.v1.csv(file=file_name, classificationId="DnsServer")
    assert os.path.isfile(file_name)
    os.remove(file_name)
