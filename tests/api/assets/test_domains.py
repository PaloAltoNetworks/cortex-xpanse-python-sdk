import os

import pytest

from xpanse.iterator import ExResultIterator
from conftest import TEST_POC_ID, TEST_POC_EMAIL, TEST_TAG_ID, TEST_TAG_NAME


@pytest.mark.vcr()
def test_assets_domains_list(api):
    i = api.assets.domains.v2.list()
    assert isinstance(
        i, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."
    assert isinstance(i.next(), list), "Expected that next should return a list."


@pytest.mark.vcr()
def test_assets_domains_count(api):
    count = api.assets.domains.v2.count()
    assert isinstance(count, int)
    assert count > 0


@pytest.mark.vcr()
def test_assets_domains_get(api):
    domain = api.assets.domains.v2.get("link.toysrus.com")
    assert isinstance(domain, dict)
    assert domain.get("domain") == "link.toysrus.com"


@pytest.mark.vcr()
def test_assets_domains_csv(api):
    file_name = "api-domains.csv"
    assert api.assets.domains.v2.csv(file=file_name, domainSearch="api")
    assert os.path.isfile(file_name)
    assert os.path.getsize(file_name) > 0
    os.remove(file_name)


@pytest.mark.vcr()
def test_assets_domains_bulk_tag(api):
    assert api.assets.domains.v2.bulk_tag(
        operation="ASSIGN",
        asset_ids=["6b389e0e-a8ce-3821-b534-b2c7cd490efb"],
        tag_ids=["23eb806c-f99e-3f0f-8dd1-f6ded17d7d13"],
    )
    assert api.assets.domains.v2.bulk_tag(
        operation="UNASSIGN",
        asset_ids=["6b389e0e-a8ce-3821-b534-b2c7cd490efb"],
        tag_ids=["23eb806c-f99e-3f0f-8dd1-f6ded17d7d13"],
    )


@pytest.mark.vcr()
def test_assets_domains_bulk_poc(api):
    assert api.assets.domains.v2.bulk_poc(
        operation="ASSIGN",
        asset_ids=["6b389e0e-a8ce-3821-b534-b2c7cd490efb"],
        contact_ids=[TEST_POC_ID],
    )
    assert api.assets.domains.v2.bulk_poc(
        operation="UNASSIGN",
        asset_ids=["6b389e0e-a8ce-3821-b534-b2c7cd490efb"],
        contact_ids=[TEST_POC_ID],
    )


@pytest.mark.vcr()
def test_assets_domains_annotation_update(api):
    resp = api.assets.domains.v2.annotation_update(
        domain_id="e5bdc732-522a-3864-8ff3-307d35f0f0a0",
        contacts=[TEST_POC_EMAIL],
        tags=[TEST_TAG_NAME],
        note="SDK NOTE TEST",
    )
    assert isinstance(resp, dict)
    assert len(resp["contacts"]) == 1
    assert resp["contacts"][0]["email"] == TEST_POC_EMAIL

    domain = api.assets.domains.v2.get("e5bdc732-522a-3864-8ff3-307d35f0f0a0")
    assert domain["annotations"] is not None
    assert domain["annotations"]["contacts"][0]["email"] == TEST_POC_EMAIL
