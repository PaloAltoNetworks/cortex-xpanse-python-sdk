from typing import Any
from xpanse.const import V2_PREFIX
from xpanse.endpoint import ExEndpoint
from xpanse.iterator import ExResultIterator


class AssetEntitiesEndpoint(ExEndpoint):
    """
    Part of the Assets v2 API for handling Asset Entities.
    See: https://api.expander.expanse.co/api/v1/docs/
    """

    def list(self, **kwargs: Any) -> ExResultIterator:
        """
        Returns the list of Entities. Arguments should be passed as keyword args using
        the names below.

        Args:
            limit (int, optional):
                Returns at most this many results in a single api call.
                Default is 100, max is 10000.
            pageToken (str, optional):
                Returns results starting at this Page Token.

        Returns:
            :obj:`ExResultIterator`:
                An iterator containing all of the entities results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>>  # Return all entities and print each one:
            >>>  for entities in client.assets.entities.v2.list():
            ...     for entity in entities:
            ...     print(entity)
        """
        return ExResultIterator(self._api, f"{V2_PREFIX}/assets/entities", kwargs)
