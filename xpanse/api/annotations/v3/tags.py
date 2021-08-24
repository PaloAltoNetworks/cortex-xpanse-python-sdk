from typing import Any, Dict, Optional

from xpanse.const import V3_PREFIX
from xpanse.endpoint import ExEndpoint
from xpanse.iterator import ExResultIterator


class TagsEndpoint(ExEndpoint):
    """
    Part of the Annotations v3 API for tagging assets.
    See: https://api.expander.expanse.co/api/v1/docs/
    """

    def list(self, **kwargs: Any) -> ExResultIterator:
        """
        Returns the list of tag annotations. Arguments should be passed as keyword args using
        the names below.

        Args:
            limit (int, optional):
                Returns at most this many results in a single api call.
            pageToken (str, optional):
                Returns results starting at this Page Token.
            id (str, optional):
                Comma-separated string; Returns any assets with a tagId in the provided set.
            name (str, optional):
                Comma-separated string; Returns any assets with a tagName in the provided set.
            disabled (bool, optional):
                Boolean representing if the tag is currently disabled.

        Returns:
            :obj:`ExResultIterator`:
                An iterator containing all of the tag results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Prints all tag objects:
            >>> for res in client.annotations.tags.v3.list():
            ...     for tag in res:
            ...         print(tag)
        """
        return ExResultIterator(self._api, f"{V3_PREFIX}/annotations/tags", kwargs)

    def get(self, tag_id: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Returns the details for a given tag ID. Arguments should be passed as keyword args using
        the names below.

        Args:
            tagId (str):
                The tag ID. This will be a uuid.

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about the tag.

        Examples:
            >>> # Returns a Tag.
            >>> domain = client.annotations.tags.v3.get(<tag_id>)
        """
        return self._api.get(
            f"{V3_PREFIX}/annotations/tags/{tag_id}", params=kwargs
        ).json()

    def create(
        self, name: str, description: Optional[str] = None, disabled: bool = False
    ) -> Dict[str, Any]:
        """
        Create a new tag.

        Args:
            name (str):
                Name of the tag. Limit of 128 characters.
            description (str, optional):
                Tag description. Limit of 512 characters.

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about the newly created tag.

        Examples:
            >>> # Create a new tag
            >>> tag = client.annotations.tags.v3.create(name="DMZ")
        """
        payload = {"name": name, "description": description, "disabled": disabled}
        return self._api.post(f"{V3_PREFIX}/annotations/tags", json=payload).json()

    def update(self, tag_id: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Updates a tag, see keyword args for fields that can be updated.

        Note: You cannot delete tags, only disable them.

        Args:
            tag_id (str):
                UUID of the tag to be updated
            description (str, optional):
                Tag description. Limit of 512 characters.
            disabled (bool, optional):
                Whether the tag should be enabled or disabled.

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about the updated tag.

        Examples:
            >>> # Update a tag's disabled status
            >>> tag = client.annotations.tags.v3.update(disabled=True)
        """
        return self._api.put(
            f"{V3_PREFIX}/annotations/tags/{tag_id}", json={**kwargs}
        ).json()
