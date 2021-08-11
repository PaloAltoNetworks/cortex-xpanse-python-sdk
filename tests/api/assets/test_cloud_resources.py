import pytest

from expanse.iterator import ExResultIterator


@pytest.mark.vcr()
def test_assets_cloud_resources_list(api):
    pass


@pytest.mark.vcr()
def test_assets_cloud_resources_count(api):
    pass


@pytest.mark.vcr()
def test_assets_cloud_resources_get(api):
    pass


@pytest.mark.vcr()
def test_assets_cloud_resources_csv(api):
    pass


@pytest.mark.vcr()
def test_assets_cloud_resources_types(api):
    types = api.assets.cloud_resources.v2.types()
    assert isinstance(types, list)
    assert all(attribute in type_ for attribute in ("id", "name") for type_ in types)


@pytest.mark.vcr()
def test_assets_cloud_resources_bulk_tag(api):
    pass


@pytest.mark.vcr()
def test_assets_cloud_resources_bulk_poc(api):
    pass


@pytest.mark.vcr()
def test_assets_cloud_resources_annotation_update(api):
    pass
