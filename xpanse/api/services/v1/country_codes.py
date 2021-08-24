from typing import Any

from xpanse.const import V1_PREFIX
from xpanse.endpoint import ExEndpoint
from xpanse.iterator import ExResultIterator


class CountryCodesEndpoint(ExEndpoint):
    """
    Part of the Services V1 API.
    See: https://api.expander.expanse.co/api/v1/docs/
    """

    def list(self, **kwargs: Any) -> ExResultIterator:
        """
        This endpoint will return a paginated list of services country codes.

        Args:
            limit (int, optional):
                Returns at most this many results in a single api call.
                Default is 100, max is 10000.
            pageToken (str, optional):
                Page token for pagination.

        Returns:
            :obj:`ExResultIterator`:
                An iterator containing all of the services country codes results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Return all services country codes dumped to a list:
            >>> codes =  client.services.v1.country_codes.list().dump()
        """
        return ExResultIterator(self._api, f"{V1_PREFIX}/services/countryCodes", kwargs)
