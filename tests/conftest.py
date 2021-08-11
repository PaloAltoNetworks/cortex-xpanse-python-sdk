import os

import pytest

from expanse.client import ExClient

TEST_POC_ID = "378de518-28c6-4600-ad6d-3ccc6bbbe35f"
TEST_POC_EMAIL = "QA@testing.com"
TEST_TAG_ID = "53ae5bbb-01fc-3095-9a5a-2cd73dcbebaf"
TEST_TAG_NAME = "sdk_test"
TEST_ISSUE_ID = "fe40de75-5e66-3b1f-a49d-898205b52a50"
TEST_ISSUE_UPDATE_ID = "e3cf20be-ac1e-4d56-bf79-78c1161a7425"
TEST_SERVICE_ID = "6c57a874-5f78-348f-ab87-08ffd249ccff"


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("Authorization", "JWT wwwwwwwwwwwwwwwwwwwwwwwwwwwww"),],
    }


@pytest.fixture
def api():
    return ExClient(
        jwt=os.getenv("EXPANSE_TEST_JWT_TOKEN", "wwwwwwwwwwwwwwwwwwwwwwwwwwwww")
    )
