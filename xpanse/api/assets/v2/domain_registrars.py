from typing import Any

from xpanse.const import V2_PREFIX
from xpanse.endpoint import ExEndpoint
from xpanse.iterator import ExResultIterator


class DomainRegistrarsEndpoint(ExEndpoint):
    """
    Part of the Assets v2 API for handling Asset Domain Registrars.
    See: https://api.expander.expanse.co/api/v1/docs/
    """

    def list(self, **kwargs: Any) -> ExResultIterator:
        """
        Returns the list of Domain Registrars. Arguments should be passed as keyword args using
        the names below.

        Args:
            limit (int, optional):
                Returns at most this many results in a single api call.
                Default is 100, max is 10000.
            pageToken (str, optional):
                Returns results starting at this Page Token.
        Returns:
            :obj:`ExResultIterator`:
                An iterator containing all of the domain registrars results. Results can be iterated
                or called by page using `<iterator>.next()`.
        Examples:
            >>> # Return all domain registrars and print each one:
            >>> for props in client.assets.domain_registrars.v2.list():
            ...     for prop in props:
            ...         print(prop)
        """
        return ExResultIterator(
            self._api, f"{V2_PREFIX}/assets/domain-registrars", kwargs
        )
