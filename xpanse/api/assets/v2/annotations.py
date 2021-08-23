from typing import Any, Dict

from xpanse.const import V2_PREFIX
from xpanse.endpoint import ExEndpoint
from xpanse.iterator import ExResultIterator


class AnnotationsEndpoint(ExEndpoint):
    """
    Part of the Assets v2 API for handling Annotations.
    See: https://api.expander.expanse.co/api/v1/docs/
    """

    def list_poc(self, **kwargs: Any) -> ExResultIterator:
        """
        Returns a list of points-of-contact.

        Args:
            limit (int, optional):
                Returns at most this many results in a single api call (default: 100, max: 10,000).
            offset (int, optional):
                Returns results starting at this offset (default: 0).
            sort (str, optional):
                Comma-separated string; orders results by the given fields.
                If the field name is prefixed by a -, then the ordering will be descending for that field.
                Allowed values are `id`, `-id`, `created`, `-created`.
            is_assigned (boolean, optional):
                Boolean flag filter to return objects that are assigned to an IP range

        Returns:
            :obj:`ExResultIterator`:
                An iterator containing all of the point-of-contact annotation results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Return all poc annotations and print each range:
            >>> for res in client.assets.annotations.v2.list_poc():
            ...     for poc in res:
            ...         print(poc)
        """
        return ExResultIterator(
            self._api, f"{V2_PREFIX}/annotation/point-of-contact", kwargs
        )

    def create_poc(self, email: str, **kwargs: Any) -> Dict[str, str]:
        """
        Create a new point-of-contact.

        Args:
            email (str):
                Email address for new point-of-contact.
            firstName (str, optional):
                First name for new point-of-contact.
            lastName (str, optional):
                Last name for new point-of-contact.
            phone (str, optional):
                Phone for new point-of-contact.
            role (str, optional):
                Role for new point-of-contact.

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about the newly created point-of-contact.

        Examples:
            >>> # Create a new point-of-contact
            >>> poc = client.assets.annotations.v2.create_poc("admin@expanse.co", firstName="Luke", lastName="Skywalker", phone="123-456-7890", role="sysadmin")
        """
        payload = {"email": email}

        if "firstName" in kwargs:
            payload["firstName"] = kwargs["firstName"]
        if "lastName" in kwargs:
            payload["lastName"] = kwargs["lastName"]
        if "phone" in kwargs:
            payload["phone"] = kwargs["phone"]
        if "role" in kwargs:
            payload["role"] = kwargs["role"]
        return self._api.post(
            f"{V2_PREFIX}/annotation/point-of-contact", json=payload
        ).json()

    def delete_poc(self, id: str) -> bool:
        """
        Delete the given point-of-contact, and all connections to other data.

        Args:
            id (str):
                ID for the point-of-contact. Should be a UUID.

        Returns:
            :obj:`boolean`:
                `True` if the point-of-contact was successfully deleted, otherwise `False`.

        Examples:
            >>> # Deletes a point-of-contact
            >>> client.assets.annotations.v2.delete_poc(<id>)
        """
        return (
            True
            if self._api.delete(
                f"{V2_PREFIX}/annotation/point-of-contact/{id}"
            ).status_code
            == 204
            else False
        )

    def get_poc(self, id: str) -> Dict[str, str]:
        """
        Returns the details for the given point-of-contact.

        Args:
            id (str):
                ID for the point-of-contact. Should be a UUID.

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about a point-of-contact.

        Examples:
            >>> # Return a point-of-contact
            >>> my_range = client.assets.annotations.v2.get_poc(<id>)
        """
        return self._api.get(
            f"{V2_PREFIX}/annotation/point-of-contact/{id}", params={}
        ).json()

    def list_tag(self, **kwargs: Any) -> ExResultIterator:
        """
        Returns a list of tags. Arguments should be passed as keyword args using
        the names below.

        Args:
            limit (int, optional):
                Returns at most this many results in a single api call (default: 100, max: 10,000).
            offset (int, optional):
                Returns results starting at this offset (default: 0).
            sort (str, optional):
                Comma-separated string; orders results by the given fields.
                If the field name is prefixed by a -, then the ordering will be descending for that field.
                Allowed values are `id`, `-id`, `created`, `-created`.
            is_assigned (boolean, optional):
                Boolean flag filter to return objects that are assigned to an IP range
            business_units (str, optional):
                Comma-separated string; Returns only results whose Business Unit's ID falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
                Also, cannot be used with the business-unit-names parameter.
            business_unit_names (str, optional):
                Comma-separated string; Returns only results whose Business Unit's name falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
                Also, cannot be used with the business-units parameter.

        Returns:
            :obj:`ExResultIterator`:
                An iterator containing all of the tag annotation results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Return all tag annotations and print each range:
            >>> for res in client.assets.annotations.v2.list_poc():
            ...     for tag in res:
            ...         print(tag)
        """
        return ExResultIterator(self._api, f"{V2_PREFIX}/annotation/tag", kwargs)

    def create_tag(self, name: str) -> Dict[str, str]:
        """
        Create a new tag.

        Args:
            name (str):
                Name of the tag.

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about the newly created tag.

        Examples:
            >>> # Create a new tag
            >>> tag = client.assets.annotations.v2.create_tag(name="Wrong registration")
        """
        return self._api.post(f"{V2_PREFIX}/annotation/tag", json={"name": name}).json()

    def delete_tag(self, id: str) -> bool:
        """
        Delete the given tag, and all connections to other data.

        Args:
            id (str):
                ID for the tag. Should be a UUID.

        Returns:
            :obj:`boolean`:
                `True` if the tag was successfully deleted, otherwise `False`.

        Examples:
            >>> # Deletes a taf
            >>> client.assets.annotations.v2.delete_tag(<id>)
        """
        return (
            True
            if self._api.delete(f"{V2_PREFIX}/annotation/tag/{id}").status_code == 204
            else False
        )

    def get_tag(self, id: str) -> Dict[str, str]:
        """
        Returns the details for the given tag.

        Args:
            id (str):
                ID for the tag. Should be a UUID.

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about a tag.

        Examples:
            >>> # Return a tag
            >>> my_range = client.assets.annotations.v2.get_tag(<id>)
        """
        return self._api.get(f"{V2_PREFIX}/annotation/tag/{id}", params={}).json()
