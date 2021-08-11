import os

import pytest

from expanse.iterator import ExResultIterator
from conftest import TEST_POC_ID, TEST_POC_EMAIL, TEST_TAG_ID, TEST_TAG_NAME


@pytest.mark.vcr()
def test_assets_certificates_list(api):
    i = api.assets.certificates.v2.list()
    assert isinstance(
        i, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."
    assert isinstance(i.next(), list), "Expected that next should return a list."


@pytest.mark.vcr()
def test_assets_certificates_count(api):
    count = api.assets.certificates.v2.count()
    assert isinstance(count, int)
    assert count > 0


@pytest.mark.vcr()
def test_assets_certificates_get(api):
    cert = api.assets.certificates.v2.get("1MZVcFeLBLab3jC-_z9t5Q==")
    assert isinstance(cert, dict)
    assert cert.get("id") == "cc5de40e-286f-303b-be57-d155b3bd4611"
    assert cert.get("certificate").get("md5Hash") == "1MZVcFeLBLab3jC-_z9t5Q=="


@pytest.mark.vcr()
def test_assets_certificates_csv(api):
    file_name = "api-certs.csv"
    assert api.assets.certificates.v2.csv(file=file_name, commonNameSearch="api")
    assert os.path.isfile(file_name)
    assert os.path.getsize(file_name) > 0
    os.remove(file_name)


@pytest.mark.vcr()
def test_assets_certificates_bulk_tag(api):
    assert api.assets.certificates.v2.bulk_tag(
        operation="ASSIGN",
        asset_ids=["cc5de40e-286f-303b-be57-d155b3bd4611"],
        tag_ids=[TEST_TAG_ID],
    )
    assert api.assets.certificates.v2.bulk_tag(
        operation="UNASSIGN",
        asset_ids=["cc5de40e-286f-303b-be57-d155b3bd4611"],
        tag_ids=[TEST_TAG_ID],
    )


@pytest.mark.vcr()
def test_assets_certificates_bulk_poc(api):
    assert api.assets.certificates.v2.bulk_poc(
        operation="ASSIGN",
        asset_ids=["cc5de40e-286f-303b-be57-d155b3bd4611"],
        contact_ids=[TEST_POC_ID],
    )
    assert api.assets.certificates.v2.bulk_poc(
        operation="UNASSIGN",
        asset_ids=["cc5de40e-286f-303b-be57-d155b3bd4611"],
        contact_ids=[TEST_POC_ID],
    )


@pytest.mark.vcr()
def test_assets_certificates_annotation_update(api):
    resp = api.assets.certificates.v2.annotation_update(
        certificate_id="cc5de40e-286f-303b-be57-d155b3bd4611",
        contacts=[TEST_POC_EMAIL],
        tags=[TEST_TAG_NAME],
        note="SDK NOTE TEST",
    )
    assert isinstance(resp, dict)
    assert len(resp["contacts"]) == 1
    assert resp["contacts"][0]["email"] == TEST_POC_EMAIL

    cert = api.assets.certificates.v2.get("1MZVcFeLBLab3jC-_z9t5Q==")
    assert cert["annotations"] is not None
    assert cert["annotations"]["contacts"][0]["email"] == TEST_POC_EMAIL
