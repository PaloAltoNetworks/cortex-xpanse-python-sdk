import os

import pytest

from xpanse.iterator import ExResultIterator


@pytest.mark.vcr()
def test_assets_ips_list(api):
    i = api.assets.ips.v2.list()
    assert isinstance(
        i, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."
    assert isinstance(i.next(), list), "Expected that next should return a list."


@pytest.mark.vcr()
def test_assets_ips_csv(api):
    file_name = "cloud-ips.csv"
    assert api.assets.ips.v2.csv(file=file_name, hostingEnvironment="CLOUD")
    assert os.path.isfile(file_name)
    assert os.path.getsize(file_name) > 0
    os.remove(file_name)
