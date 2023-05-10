import pytest
import os

from xpanse.client import XpanseClient
from xpanse.error import InvalidApiCredentials


@pytest.mark.vcr()
def test_XpanseClient_invalid_advanced_auth():
    with pytest.raises(InvalidApiCredentials) as e:
        XpanseClient(url=os.getenv("TEST_CORTEX_FQDN", "ben-expander.crtx-qa2-uat.us.paloaltonetworks.com"),
                     api_key_id=os.getenv("TEST_CORTEX_API_KEY_ID", 1),
                     api_key=os.getenv("TEST_CORTEX_API_KEY", "wwwwwwwwwwwwwwwwwwwwwwww"))
    assert "Failed to authenticate with the provided 'api_key' and 'api_key_id' using 'Advanced' authentication." \
           in str(e.value)


@pytest.mark.vcr()
def test_XpanseClient_invalid_standard_auth():
    with pytest.raises(InvalidApiCredentials) as e:
        XpanseClient(use_advanced_auth=False,
                     url=os.getenv("TEST_CORTEX_FQDN", "ben-expander.crtx-qa2-uat.us.paloaltonetworks.com"),
                     api_key_id=os.getenv("TEST_CORTEX_API_KEY_ID", 1),
                     api_key=os.getenv("TEST_CORTEX_API_KEY", "wwwwwwwwwwwwwwwwwwwwwwww"))
    assert "Failed to authenticate with the provided 'api_key' and 'api_key_id' using 'Standard' authentication." \
           in str(e.value)


def test_XpanseClient_missing_host():
    with pytest.raises(ValueError) as e:
        XpanseClient(api_key_id=os.getenv("TEST_CORTEX_API_KEY_ID", 1),
                     api_key=os.getenv("TEST_CORTEX_API_KEY", "wwwwwwwwwwwwwwwwwwwwwwww"))
    assert "A 'url' must be provided. Set the 'url' client parameter or set the 'CORTEX_FQDN' environment variable." \
           in str(e.value)


@pytest.mark.vcr()
def test_XpanseClient_valid_standard_auth_via_params():
    XpanseClient(use_advanced_auth=False,
                 url=os.getenv("TEST_CORTEX_FQDN", "ben-expander.crtx-qa2-uat.us.paloaltonetworks.com"),
                 api_key_id=os.getenv("TEST_CORTEX_API_KEY_ID", 1),
                 api_key=os.getenv("TEST_CORTEX_API_KEY", "wwwwwwwwwwwwwwwwwwwwwwww"))


@pytest.mark.vcr()
def test_XpanseClient_valid_advanced_auth_via_params():
    XpanseClient(url=os.getenv("TEST_CORTEX_FQDN", "ben-expander.crtx-qa2-uat.us.paloaltonetworks.com"),
                 api_key_id=os.getenv("TEST_CORTEX_API_KEY_ID", 1),
                 api_key=os.getenv("TEST_CORTEX_API_KEY", "wwwwwwwwwwwwwwwwwwwwwwww"))


@pytest.mark.vcr()
def test_XpanseClient_valid_advanced_auth_via_env():
    os.environ["CORTEX_FQDN"] = "ben-expander.crtx-qa2-uat.us.paloaltonetworks.com"
    os.environ["CORTEX_API_KEY_ID"] = "1"
    os.environ["CORTEX_API_KEY"] = "wwwwwwwwwwwwwwwwwwwwwwww"
    XpanseClient()
