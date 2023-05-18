from typing import Any, List

from xpanse.const import V1_PREFIX
from xpanse.endpoint import XpanseEndpoint
from xpanse.response import XpanseResponse
from xpanse.utils import build_request_payload


class AttackSurfaceRulesEndpoint(XpanseEndpoint):
    """
    Part of the Public API for handling Attack Surface Rules.
    See: TODO:// https://jira-hq.paloaltonetworks.local/browse/EXPANDR-3062
    """

    ENDPOINT = f"{V1_PREFIX}/get_attack_surface_rules/"
    DATA_KEY = "attack_surface_rules"

    def list(self, request_data: Any = None, **kwargs: Any) -> XpanseResponse:
        """
        This endpoint will return a paginated list of Attack Surface Rules.

        Args:
            request_data (RequestData, Optional):
                Any supplemental request_data to be included with your request. This is needed to
                implement any additional filters, offsets, limits, or sort ordering.
            **kwargs:
                Any extraneous parameters you would like to include when executing your
                request with the `requests` module. Note: By default, all payload data
                is sent under the "json" keyword for your request.

        Returns:
            :obj:`XpanseIterator`:
                An iterator containing all of the Attack Surface Rules results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Return all attack surface rules dumped to a list:
            >>> attack_surface_rules =  client.attack_surface_rules.list().dump()
        """
        kwargs = build_request_payload(request_data=request_data, **kwargs)
        response = self._api.post(path=self.ENDPOINT, **kwargs)
        return XpanseResponse(response, data_key=self.DATA_KEY)

    def get(
        self,
        attack_surface_rule_ids: List[str],
        request_data: Any = None,
        **kwargs: Any,
    ) -> XpanseResponse:
        """
        This endpoint will return details for a list of Attack Surface Rule ids. Arguments should be passed as keyword args using
        the names below.

        Args:
            attack_surface_rule_ids (List[str]):
                The lists of Attack Surface Rule ids to retrieve with your request.
            request_data (RequestData, Optional):
                Any supplemental request_data to be included with your request. This is needed to
                implement any additional filters, offsets, limits, or sort ordering.
            **kwargs:
                Any extraneous parameters you would like to include when executing your
                request with the Requests.request module. Note: By default, all payload data
                is sent under the "json" keyword for your request.

        Returns:
            :obj:`XpanseResponse`:
                An object containing the raw requests.Response and parsed data results.
                The raw response can be accessed with `<xpanse_reponse>.response` attribute.
                The parsed results can be accessed with the `<xpanse_response>.data` attribute.

        Examples:
            >>> # Get attack surface rules with specified ids to a list:
            >>> attack_surface_rules =  client.attack_surface_rules.get(attack_surface_rule_ids=["id1", "id2"])
            >>> if attack_surface_rules.response.status_code < 300:
            >>>     results = attack_surface_rules.data
        """
        filters = [
            {
                "field": "attack_surface_rule_id",
                "operator": "in",
                "value": attack_surface_rule_ids,
            }
        ]
        kwargs = build_request_payload(
            request_data=request_data, filters=filters, **kwargs
        )
        response = self._api.post(self.ENDPOINT, **kwargs)
        return XpanseResponse(response, data_key=self.DATA_KEY)

    def count(self, request_data: Any = None, **kwargs: Any) -> XpanseResponse:
        """
        This endpoint will return a count of Attack Surface Rules.

        Args:
            request_data (RequestData, Optional):
                Any supplemental request_data to be included with your request. This is needed to
                implement any additional filters, offsets, limits, or sort ordering.
            **kwargs:
                Any extraneous parameters you would like to include when executing your
                request with the Requests.request module. Note: By default, all payload data
                is sent under the "json" keyword for your request.

        Returns:
            :obj:`XpanseResponse`:
                An object containing the raw requests.Response and parsed data results.
                The raw response can be accessed with `<xpanse_reponse>.response` attribute.
                The parsed results can be accessed with the `<xpanse_response>.data` attribute.

        Examples:
            >>> # Get attack surface rules total count:
            >>> attack_surface_rules =  client.attack_surface_rules.count()
            >>> if attack_surface_rules.response.status_code < 300:
            >>>     count = attack_surface_rules.data
        """
        return super(AttackSurfaceRulesEndpoint, self)._count(
            self.ENDPOINT, request_data=request_data, **kwargs
        )
