from typing import Any
from xpanse.const import V1_PREFIX
from xpanse.endpoint import ExEndpoint
from xpanse.iterator import ExResultIterator


class ConnectorsServicesEndpoint(ExEndpoint):
    """
    Part of the Connectors V1 API.
    See: https://api.expander.expanse.co/api/v1/docs/
    """

    def list(self, **kwargs: Any) -> ExResultIterator:
        """
           This endpoint will return a paginated list of connector services.

           Args:
               limit (int, optional):
                   Returns at most this many results in a single api call.
                   Default is 100, max is 10000.
               pageToken (str, optional):
                   Page token for pagination.

        Returns:
            :obj:`ExResultIterator`:
                An iterator containing all of the connector services results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Return all connector services dumped to a list:
            >>> bus =  client.connectors.services.list().dump()
        """
        return ExResultIterator(self._api, f"{V1_PREFIX}/connectors/services", kwargs)
