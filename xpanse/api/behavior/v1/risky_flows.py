from typing import Any, Dict

from xpanse.const import V1_PREFIX
from xpanse.endpoint import ExEndpoint
from xpanse.iterator import ExResultIterator


class RiskyFlowsEndpoint(ExEndpoint):
    """
    Part of the Behvaior v1 API for access risky flows.
    See: https://api.expander.expanse.co/api/v1/docs/
    """

    def list(self, **kwargs: Any) -> ExResultIterator:
        """
        Returns the list of risky flows matching the given criteria. Arguments should be passed as keyword args using
        the names below.

        Args:
            created_after (string, optional):
                Returns risky flows that were created after this timestamp.
                Should be formatted as YYYY-MM-DDTHH:MM:SS.mmmZ
            created_before (string, optional):
                Returns risky flows that were created before this timestamp.
                Should be formatted as YYYY-MM-DDTHH:MM:SS.mmmZ
            limit (int, optional):
                Returns at most this many results in a single api call.
            offset (int, optional):
                Returns results starting at this offset.
                Default is 0.
            business_unit (str, optional):
                Returns risky flows for IPs which belong to the specified Business Unit. This should
                be the Business Unit ID rather than the name.
            risk_rule (string, optional):
                Returns risky flows that match the specified Risk Rule ID.
            tag_names (string, optional):
                Comma-separated string; Returns only results that are associated with the provided tags.
                The tag name should be used here rather than the tag id.
            internal_ip_range (string, optional):
                Returns the riksy flows that match the specified internal CIDR/IP Range/Address.
                Supported IP formats: a.b.c.d, a.b.c.d/e, a.b.c.d-a.b.c.d, a., a.*

        Returns:
            :obj:`ExResultIterator`:
                An iterator containing all of the risky flow results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Prints all risky flow objects for a date range:
            >>> flows = client.behavior.risky_flows.v1.list(created_after="2020-12-20T00:00:00.000Z", created_before="2020-12-21T00:00:00.000Z").dump()
            >>> print(flows)
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
            self._api, f"{V1_PREFIX}/behavior/risky-flows{arg_list}", {}
        )

    def get(self, risky_flow_id: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Returns details about a single risky flow.

        Args:
            risky_flow_id (string):
                ID of a single risky flow.

        Returns:
            :obj:`dict`:
                A dict containing information about a specific risky flow.

        Examples:
            >>> # Print details of a risky flow
            >>> flow = client.behavior.risky_flows.v1.get(risky_flow_id="")
            >>> print(flow)
        """
        return self._api.get(
            f"{V1_PREFIX}/behavior/risky-flows/{risky_flow_id}", params=kwargs
        ).json()
