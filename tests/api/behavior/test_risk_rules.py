import pytest

from expanse.iterator import ExResultIterator


@pytest.mark.vcr()
def test_behavior_risk_rules(api):
    i = api.behavior.risk_rules.v1.list()
    assert isinstance(
        i, ExResultIterator
    ), "Expected instance of `ExResultIterator` to be returned."
    assert isinstance(i.next(), list), "Expected that next should return a list."