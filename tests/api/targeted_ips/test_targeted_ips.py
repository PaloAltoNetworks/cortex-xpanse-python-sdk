import pytest


@pytest.mark.vcr()
def test_targeted_ips_list(api):
    ips = api.targeted_ips.targeted_ips.v1.list()
    assert isinstance(
        ips, dict
    ), "Expected a dict to be returned."
    assert "lastUpdated" in ips
    assert "prefixes" in ips
