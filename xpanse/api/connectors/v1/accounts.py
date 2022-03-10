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
                ID of the requested connector account. Should be a UUID.

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about the connector account.

        Examples:
            >>> # Return Issue.
            >>> connector = client.connector.accounts.get(<id>)
        """
        return self._api.get(
            f"{V1_PREFIX}/connectors/accounts/{id}", params=kwargs
        ).json()

    def create(
        self, businessUnitId: str, name: str, dataSourceId: str, credentials: str
    ) -> Dict[str, Any]:
        """
        Creates a new Connector Account

        Args:
            businessUnitId (str):
                The ID of the business unit that this should be associated with. Should be a UUID.
            name (str):
                The name of the new account.
            dataSourceId (str):
                The ID of the data source that you would like to connect.
            credentials (dict):
                The credentials should be in JSON format withcontent that is dependent on the Connector Service

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about the new connector account.

        Examples:
            >>> # Return updates for issue and dump to list.
            >>> connector_account = client.connectors.accounts.create(businessUnitId=<id>, name=<account_name>, dataSourceId=<data_source_id>, credentials=<{"api_key": 'test_key'}>)
        """
        if (
            businessUnitId is None
            or name is None
            or dataSourceId is None
            or credentials is None
        ):
            raise UnexpectedValueError("A required connector account value was missing")
        payload = {
            "businessUnitId": businessUnitId,
            "name": name,
            "dataSourceId": dataSourceId,
            "credentials": credentials,
        }
        return self._api.post(f"{V1_PREFIX}/connectors/accounts", json=payload).json()

    def update(self, id: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Updates a Connector Account

        Args:
            id (str):
                The ID of the connector account that should be updated. Should be a UUID.
            businessUnitId (str, optional):
                The ID of the business unit that this should be associated with.
            name (str, optional):
                The name of the new account.
            dataSourceId (str, optional):
                The ID of the data source that you would like to connect.
            credentials (dict, optional):
                The credentials should be in JSON format withcontent that is dependent on the Connector Service

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about the new connector account.

        Examples:
            >>> # Return updates for issue and dump to list.
            >>> connector_account = client.connectors.accounts.update(id=<id>, name=<new_name>)
        """
        return self._api.put(
            f"{V1_PREFIX}/connectors/accounts/{id}", json={**kwargs}
        ).json()

    def delete(self, id: str) -> bool:
        """
        Delete the given Connector Account.

        Args:
            id (str):
                ID for the connector account. Should be a UUID.

        Returns:
            :obj:`boolean`:
                `True` if the range was successfully deleted, otherwise `False`.

        Examples:
            >>> # Deletes a connector account
            >>> client.connectors.accounts.delete("test_id")
        """
        return (
            True
            if self._api.delete(f"{V1_PREFIX}/connectors/accounts/{id}").status_code
            == 204
            else False
        )
