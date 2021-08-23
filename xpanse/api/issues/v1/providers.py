from typing import Any

from xpanse.const import V1_PREFIX
from xpanse.endpoint import ExEndpoint
from xpanse.iterator import ExResultIterator


class ProvidersEndpoint(ExEndpoint):
    """
    Part of the Issues V1 API.
    See: https://api.expander.expanse.co/api/v1/docs/
    """

    def list(self, **kwargs: Any) -> ExResultIterator:
        """
        This endpoint will return a paginated list of issues providers.

        Args:
            limit (int, optional):
                Returns at most this many results in a single api call.
                Default is 100, max is 10000.
            pageToken (str, optional):
                Page token for pagination.

        Returns:
            :obj:`ExResultIterator`:
                An iterator containing all of the issues providers results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Return all issues providers dumped to a list:
            >>> providers =  client.issues.providers.v1.list().dump()
        """
        return ExResultIterator(self._api, f"{V1_PREFIX}/issues/providers", kwargs)
