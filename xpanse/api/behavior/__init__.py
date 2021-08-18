from xpanse.base_api import ExApi
from xpanse.api.behavior.v1.risky_flows import RiskyFlowsEndpoint
from xpanse.api.behavior.v1.risk_rules import RiskRulesEndpoint


class RiskyFlowsApi(ExApi, RiskyFlowsEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v1"

    @property
    def v1(self):
        return RiskyFlowsEndpoint(self._api)


class RiskRulesApi(ExApi, RiskRulesEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v1"

    @property
    def v1(self):
        return RiskRulesEndpoint(self._api)


class BehaviorApi(ExApi):
    @property
    def risky_flows(self):
        return RiskyFlowsApi(self._api)

    @property
    def risk_rules(self):
        return RiskRulesApi(self._api)
