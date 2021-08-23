from typing import Any

from xpanse.const import V1_PREFIX
from xpanse.endpoint import ExEndpoint
from xpanse.iterator import ExResultIterator


class RiskRulesEndpoint(ExEndpoint):
    """
    Part of the Behvaior v1 API for access risk rules.
    See: https://api.expander.expanse.co/api/v1/docs/
    """

    def list(self, **kwargs: Any) -> ExResultIterator:
        """
        Returns the list of risk-rules matching the given criteria. Arguments should be passed as keyword args using
        the names below.

        Args:
            limit (int, optional):
                Returns at most this many results in a single api call.
            offset (int, optional):
                Returns results starting at this offset.
                Default is 0.
            business_unit (str, optional):
                Returns risk rules assigned to a specified Business Unit. This should
                be the Business Unit ID rather than the name.

        Returns:
            :obj:`ExResultIterator`:
                An iterator containing all risk rules results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Prints all configured risk rules
            >>> rules = client.behavior.risk_rules.v1.list().dump()
            >>> print(rules)
        """
        arg_list = "?"
        if kwargs:
            for k, v in kwargs.items():
                if v is not None:
                    if k in ("limit", "offset"):
                        arg_list += f"page[{k}]={v}&"
                    else:
                        if isinstance(v, list):
                            arg_list += f"filter[{k.replace('_', '-')}]={','.join(v)}&"
                        else:
                            arg_list += f"filter[{k.replace('_', '-')}]={v}&"
        return ExResultIterator(
            self._api, f"{V1_PREFIX}/behavior/risk-rules{arg_list}", {}
        )
