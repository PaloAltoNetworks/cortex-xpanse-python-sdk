from typing import Any, Dict

from xpanse.const import V2_PREFIX
from xpanse.endpoint import ExEndpoint
from xpanse.iterator import ExResultIterator


class AccountIntegrationsEndpoint(ExEndpoint):
    """
    Part of the Assets v2 API for handling Asset Account Integrations.
    See: https://api.expander.expanse.co/api/v1/docs/
    """

    def list(self, **kwargs: Any) -> ExResultIterator:
        """
        Returns the list of Account Integrations. Arguments should be passed as keyword args using
        the names below.

        Args:
            limit (int, optional):
                Returns at most this many results in a single api call.
                Default is 100, max is 10000.
            pageToken (str, optional):
                Returns results starting at this Page Token.
        Returns:
            :obj:`ExResultIterator`:
                An iterator containing all of the account integration results. Results can be iterated
                or called by page using `<iterator>.next()`.
        Examples:
            >>> # Return all account integrations and print each one:
            >>> for integrations in client.assets.account_integrations.v2.list():
            ...     for integration in integrations:
            ...         print(integration)
        """
        return ExResultIterator(
            self._api, f"{V2_PREFIX}/assets/account-integrations", kwargs
        )
