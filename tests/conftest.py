import os

import pytest

from xpanse.client import ExClient

TEST_POC_ID = "378de518-28c6-4600-ad6d-3ccc6bbbe35f"
TEST_POC_EMAIL = "QA@testing.com"
TEST_TAG_ID = "2f56c9d4-308c-3331-9c08-030ee5847901"
TEST_ASSETS_TAG_ID = "e6306635-9f96-37d2-bbe6-6d741569bc34"
TEST_TAG_NAME = "sdk_test_cc"
TEST_TAG_NAME_ASSET_ANNOTATIONS = "sdk_test_client_credentials_asset_annotations"
TEST_ISSUE_ID = "3188ba60-4472-37a8-8a4f-ad8e2407b771"
TEST_ISSUE_UPDATE_ID = "c97038fc-c7a9-4100-8f9c-b8e4fed48d88"
TEST_SERVICE_ID = "5cf28734-68da-3483-96f1-3901df311f06"
TEST_CONNECTOR_ACCOUNT_ID="fe8e842c-3e7b-4cce-bfbb-b7ff4169b3f4"


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("Authorization", "bearer wwwwwwwwwwwwwwwwwwwwwwwwwwwww")],
    }


@pytest.fixture
def api():
    return ExClient(
        jwt=os.getenv("XPANSE_TEST_JWT", "wwwwwwwwwwwwwwwwwwwwwwwwwwwww"),
        url="https://expander.staging.qadium.com"
    )
