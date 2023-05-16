import os

import pytest

from xpanse.client import XpanseClient


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("Authorization", "wwwwwwwwwwwwwwwwwwwwwwwwwwwww"),
                           ("x-xdr-auth-id", 1),
                           ("x-xdr-nonce", "yyyyyyyyyyyyyyyyyyyyyyyyyyy"),
                           ("x-xdr-timestamp", "1000000000000")],
    }


@pytest.fixture
def api():
    return XpanseClient(
        url=os.getenv("TEST_CORTEX_FQDN", "ben-expander.crtx-qa2-uat.us.paloaltonetworks.com"),
        api_key_id=os.getenv("TEST_CORTEX_API_KEY_ID", 1),
        api_key=os.getenv("TEST_CORTEX_API_KEY", "wwwwwwwwwwwwwwwwwwwwwwwwwwwww"),
    )
