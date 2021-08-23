import pytest

from expanse.client import ExClient
from xpanse.error import UnexpectedValueError


@pytest.mark.vcr()
def test_ExClient_invalid_bearer_token():
    with pytest.raises(UnexpectedValueError) as e:
        ExClient(bearer_token="wrong-token")
    assert "Could not get an id token based on the given refresh token" in str(e)


@pytest.mark.vcr()
def test_ExClient_refresh_jwt():
    api = ExClient(jwt="expired-jwt", bearer_token="bearer-token")
    resp = api.get("api/v2/assets/domains/count")
    assert resp
    assert api._jwt == "new-jwt"
