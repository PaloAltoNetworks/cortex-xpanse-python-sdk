from typing import Any, Dict
from xpanse.const import V1_PREFIX
from xpanse.endpoint import ExEndpoint
from xpanse.iterator import ExResultIterator


class ConnectorsAccountsEndpoint(ExEndpoint):
    """
    Part of the Connectors V1 API.
    See: https://api.expander.expanse.co/api/v1/docs/
    """

    def list(self, **kwargs: Any) -> ExResultIterator:
        """
           This endpoint will return a paginated list of connector accounts.

           Args:
               limit (int, optional):
                   Returns at most this many results in a single api call.
                   Default is 100, max is 10000.
               pageToken (str, optional):
                   Page token for pagination.

        Returns:
            :obj:`ExResultIterator`:
                An iterator containing all of the connector accounts results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Return all connector sercices dumped to a list:
            >>> bus =  client.connectors.accounts.list().dump()
        """

        return ExResultIterator(self._api, f"{V1_PREFIX}/connectors/accounts", kwargs)

    def get(self, id: str, **kwargs: Any) -> Dict[str, Any]:
        """
        This endpoint will return details for a given connector account. Arguments should be passed as keyword args using
        the names below.

        Args:
            id (str):
                ID of the requested connector account.

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about the connector account.

        Examples:
            >>> # Return Issue.
            >>> issue = client.connector.accounts.get(<id>)
        """
        return self._api.get(
            f"{V1_PREFIX}/connectors/accounts/{id}", params=kwargs
        ).json()
