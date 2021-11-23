import pytest
import os

from xpanse.client import ExClient
from xpanse.error import UnexpectedValueError


@pytest.mark.vcr()
def test_ExClient_invalid_bearer_token():
    with pytest.raises(UnexpectedValueError) as e:
        ExClient(bearer_token="wrong-token", url="https://expander.staging.qadium.com")
    assert "Could not get an id token based on the given refresh token" in str(e)


@pytest.mark.vcr()
def test_ExClient_refresh_jwt():
    api = ExClient(jwt=os.getenv("XPANSE_TEST_EXPIRED_JWT", "wwwwwwwwwwwwwwwwwwwwwwwwwwwww"),
                   bearer_token=os.getenv("XPANSE_BEARER_TOKEN", "wwwwwwwwwwwwwwwwwwwwwwww"))
    resp = api.get("api/v2/assets/domains/count")
    assert resp.status_code == 200

# @pytest.mark.vcr()
# def test_ExClient_refresh_jwt_cc():
#     api = ExClient(jwt=os.getenv("XPANSE_TEST_EXPIRED_JWT", "wwwwwwwwwwwwwwwwwwwwwwwwwwwww"),
#                    client_id=os.getenv("XPANSE_TEST_CLIENT_ID", "wwwwwwwwwwwwwwwwwwwwwwwwwwwww"),
#                    client_secret=os.getenv("XPANSE_TEST_CLIENT_SECRET", "wwwwwwwwwwwwwwwwwwwwwwwwwwwww"),
#                    url="https://expander.staging.qadium.com")
#     resp = api.get("api/v2/assets/domains/count")
#     assert resp.status_code == 200
