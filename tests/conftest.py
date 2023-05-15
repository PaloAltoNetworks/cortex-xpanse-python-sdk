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


if __name__ == '__main__':
    client = XpanseClient(url='https://ben-expander.crtx-qa2-uat.us.paloaltonetworks.com/',
                          api_key_id=2,
                          api_key='vtyF031c5Gpboh80P657Ocy8UcbTX01mDtZXdim3miIVSyhL1QAs3k5F2Rq0DEHVNzCWR7G4kyONsyKjAnqWWvwgDO3bRTzraZ9PMho8ZbiR5SEeY9K5Fd6SllfBoNkv')

    api = client.assets
    list = api.list(request_data={"search_from": 0, "search_to": 1})
    print(list.next())
    ids = ["2561688d-b632-3681-9cb7-cf49b19de09a"]
    get = api.get(asset_ids=ids)
    print(get.data)
    count = api.count()
    print(count.data)

    api = client.external_ip_ranges
    list = api.list(request_data={"search_from": 0, "search_to": 1})
    print(list.next())
    ids = ["229bdac6-1641-346a-be24-342589903bb5"]
    get = api.get(ip_range_ids=ids)
    print(get.data)
    count = api.count()
    print(count.data)

    api = client.services
    list = api.list(request_data={"search_from": 0, "search_to": 1})
    print(list.next())
    ids = ["a2da74a2-5adb-3c44-bc03-bd8a7a3b1085"]
    get = api.get(service_ids=ids)
    print(get.data)
    count = api.count()
    print(count.data)
