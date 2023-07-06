from xpanse.api.attack_surface_rules.v1.attack_surface_rules import (
    AttackSurfaceRulesEndpoint,
)


class AttackSurfaceRulesApi(AttackSurfaceRulesEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v1"

    @property
    def v1(self):
        return AttackSurfaceRulesEndpoint(self._api)
