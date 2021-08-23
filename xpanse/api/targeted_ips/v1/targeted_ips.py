from typing import Any, Dict
from xpanse.const import V1_PREFIX
from xpanse.endpoint import ExEndpoint


class TargetedIPsEndpoint(ExEndpoint):
    """
    Part of the Targeted IPs v1 API for accessing scan origination IPs.
    See: https://api.expander.expanse.co/api/v1/docs/
    """

    def list(self) -> Dict[str, Any]:
        """
        Returns a list of IPs used in Xpanse Scanning.

        Returns:
            :obj:`dict`:
                An dictionary containing a `lastUpdated` which related to when the list was last updated
                and a `prefixes` which is a list of dicts containing the scanner IP prefix.

        Examples:
            >>> # Prints all scanner prefixes:
            >>> for prefix in client.targeted_ips.targeted_ips.list().get("prefixes"):
            ...     print(prefix.get("prefix"))
        """
        return self._api.get(f"{V1_PREFIX}/targetedIps", params={}).json()
