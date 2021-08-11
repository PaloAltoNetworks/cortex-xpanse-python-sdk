import pytest

from expanse.iterator import ExResultIterator


@pytest.mark.vcr()
def test_behavior_risky_flows(api):
    i = api.behavior.risky_flows.v1.list()
    assert isinstance(
        i, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."
    assert isinstance(i.next(), list), "Expected that next should return a list."

@pytest.mark.vcr()
def test_behavior_risky_flow(api):
    i = api.behavior.risky_flows.v1.get("6b73ef6c-b230-3797-b321-c4a340169eb7")
    assert isinstance(i, dict)
