from typing import Any, Dict
from xpanse.const import V1_PREFIX
from xpanse.endpoint import ExEndpoint
from xpanse.iterator import ExResultIterator


class EntityIterator(ExResultIterator):
    """
    Iterator specifically for Entities which can be interacted with in the same way as the
    universal `ExResultIterator`.
    """

    def _get_data(self) -> Dict[str, Any]:
        """
        Returns the next page of data
        """
        if self._pages >= 1:
            resp = self._api.direct_get(self._next_url)
        else:
            resp = self._api.get(self._path, params=self._params)

        resp_as_json = resp.json()

        self._pages += 1
        self._next_url = resp_as_json.get("next", None)
        self._total = resp_as_json.get("count", 0)
        return resp_as_json["results"]


class EntitiesEndpoint(ExEndpoint):
    """
    Part of the Entities v1 API for accessing entities.
    See: https://api.expander.expanse.co/api/v1/docs/
    """

    def id_token(self):
        """
        A JWT is generated by default by this library is a Bearer token is provided. Call this endpoint will
        invalidate the current session and is not supported by this library.
        """
        raise NotImplementedError

    def list(self, **kwargs: Any) -> EntityIterator:
        """
        Returns the list of entities to which the authenticated user has access.

        Args:
            name (str, optional):
                Find an Entity by the given name
            parent (str, optional):
                Find Entities with the given parent Entity
            has_parent (boolean, optional):
                Find Entities that either have or do not have parents.

        Returns:
            :obj:`EntityIterator`:
                An iterator containing all of the entities results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Print all entities with the name `Company X`
            >>> for ents in client.entities.entities.v1.list(name="Company X"):
            ...     for ent in ents:
            ...         print(ent)
        """
        return EntityIterator(self._api, f"{V1_PREFIX}/Entity/", kwargs)

    def get(self, id: str) -> Dict[str, Any]:
        """
        Returns the details for a given Entity.
        WARNING! Fetching IP Ranges from this endpoint is now deprecated and may return incorrect data.

        Args:
            id (str):
                ID for the entity. Should be a UUID.

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about an Entity.

        Examples:
            >>> # Returns an Entity
            >>> company_x = client.entities.entities.v1.get(<id>)
        """
        return self._api.get(f"{V1_PREFIX}/Entity/{id}/").json()
