from typing import Any, List

from xpanse.const import V1_PREFIX
from xpanse.endpoint import XpanseEndpoint
from xpanse.response import XpanseResponse
from xpanse.utils import build_request_payload


class AttackSurfaceRulesApi(XpanseEndpoint):
    """
    Part of the Public API for handling Attack Surface Rules.
    See: TODO:// https://jira-hq.paloaltonetworks.local/browse/EXPANDR-3062
    """

    ENDPOINT = f"{V1_PREFIX}/get_attack_surface_rules/"
    DATA_KEY = "attack_surface_rules"

    def list(self, request_data: Any = None, **kwargs: Any) -> XpanseResponse:
        kwargs = build_request_payload(request_data=request_data, **kwargs)
        response = self._api.post(path=self.ENDPOINT, **kwargs)
        return XpanseResponse(response, self.DATA_KEY)

    def get(
        self, attack_surface_rule_ids: List[str], request_data: Any = None, **kwargs: Any
    ) -> XpanseResponse:
        filters = [{"field": "attack_surface_rule_id", "operator": "in", "value": attack_surface_rule_ids}]
        kwargs = build_request_payload(
            request_data=request_data, filters=filters, **kwargs
        )
        response = self._api.post(self.ENDPOINT, **kwargs)
        return XpanseResponse(response, data_key=self.DATA_KEY)

    def count(self, request_data: Any = None, **kwargs: Any) -> XpanseResponse:
        return super(AttackSurfaceRulesApi, self)._count(
            self.ENDPOINT, request_data=request_data, **kwargs
        )
