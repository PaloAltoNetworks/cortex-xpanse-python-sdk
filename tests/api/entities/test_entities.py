import pytest

from xpanse.api.entities.v1.entities import EntityIterator


@pytest.mark.vcr()
def test_entities_id_token(api):
    with pytest.raises(NotImplementedError):
        api.entities.entities.v1.id_token()


@pytest.mark.vcr()
def test_entities_list(api):
    i = api.entities.entities.v1.list()
    assert isinstance(
        i, EntityIterator
    ), "Expected instance of `EntityIterator` to be returned."
    first = i.next()
    assert isinstance(first, list), "Expected that next should return a list."


@pytest.mark.vcr()
def test_entities_get(api):
    entity = api.entities.entities.v1.get(id="04b5140e-bae2-3e9c-9318-a39a3b547ed5")
    assert entity is not None
    assert isinstance(entity, dict), "Expected a dict to be returned"
