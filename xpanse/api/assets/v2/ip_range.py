from typing import Any, Dict, List

from xpanse.const import V2_PREFIX
from xpanse.endpoint import ExEndpoint
from xpanse.iterator import ExResultIterator


class IpRangeEndpoint(ExEndpoint):
    """
    Part of the Assets v2 API for handling IP Ranges.
    See: https://api.expander.expanse.co/api/v1/docs/
    """

    def list(self, **kwargs: Any) -> ExResultIterator:
        """
        Returns the list of IP Ranges. Arguments should be passed as keyword args using
        the names below.

        Args:
            limit (int, optional):
                Returns at most this many results in a single api call.
                Default is 100, max is 10000.
            offset (int, optional):
                Returns results starting at this offset.
                Default is 0.
            sort (str, optional):
                Comma-separated string; orders results by the given fields. If the field name is
                prefixed by a -, then the ordering will be descending for that field.
                Use a dotted notation to order by fields that are nested.
            business_units (str, optional):
                Comma-separated string; Returns only results whose Business Unit's ID falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
                Also, cannot be used with the business-unit-names parameter.
            business_unit_names (str, optional):
                Comma-separated string; Returns only results whose Business Unit's name falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
                Also, cannot be used with the business-units parameter.
            inet (str, optional):
                Search for given IP/CIDR block using a single IP (d.d.d.d), a dashed IP range (d.d.d.d-d.d.d.d),
                a CIDR block (d.d.d.d/m), a partial CIDR (d.d.), or a wildcard (d.d.*.d).
                Returns only results whose [startAddress, endAddress] range overlap with the given IP Address or CIDR.
            tags (str, optional):
                Comma-separated string; Returns only results who are associated with the provided Tag IDs.
                Cannot be used with the tag-names parameter.
            tag_names (str, optional):
                Comma-separated string; Returns only results who are associated with the provided Tag names.
                Cannot be used with the tags parameter.
            include (str, optional):
                Comma-separated string; Include the provided fields as part of the serialized result. Allowed values are
                `annotations`, `severityCounts`, `attributionReasons`, `relatedRegistrationInformation`, `certDetails`, and `locationInformation`

        Returns:
            :obj:`ExResultIterator`:
                An iterator containing all of the ip_range results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Return all ip ranges and print each range:
            >>> for res in client.assets.ip_range.v2.list():
            ...     for ip_r in res:
            ...         print(ip_r)
        """
        return ExResultIterator(self._api, f"{V2_PREFIX}/ip-range", kwargs)

    def get(self, id: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Returns the details for a given IP Range. Arguments should be passed as keyword args using
        the names below.

        Args:
            id (str):
                ID for the ip-range. Should be a UUID.
            include (str, optional):
                Comma-separated string; Include the provided fields as part of the serialized result.

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about an IP Range.

        Examples:
            >>> # Return IP Range with severity counts
            >>> my_range = client.assets.ip_range.v2.get(<id>, include="severityCounts")
        """
        return self._api.get(f"{V2_PREFIX}/ip-range/{id}", params=kwargs).json()

    def create(
        self, startAddress: str, endAddress: str, parentId: str, **kwargs: Any
    ) -> Dict[str, Any]:
        """
        Creates a new custom IP Range.
        NOTE: A validation error will be returned if the start and end addresses of the custom range do not fit within a top level range defined by Xpanse.

        Args:
            startAddress (str):
                Start address of custom ip-range.
            endAddress (str):
                End address of custom ip-range.
            parentId (str):
                Id of parent ip-range.
            tags (list, optional):
                A list of tag annotation names.
            additionalNotes (str, optional):
                Any additional notes about the custom ip-range.
            pointOfContactIds (list, optional):
                A lost of point-of-contact annotation ids.

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about the newly created, custom IP Range.

        Examples:
            >>> # Create a new ip-range under a parent range
            >>> new_range = client.assets.ip_range.v2.create("12.175.114.120", "12.175.114.121", "43a5a569-27b0-39b5-98f4-22b9885546d7", additionalNotes="Business Unit X - Marketing website hosts")
        """
        payload: Dict[str, Any] = {
            "startAddress": startAddress,
            "endAddress": endAddress,
            "parentId": parentId,
            "annotations": {},
        }

        if "tags" in kwargs:
            payload["annotations"]["tags"] = kwargs["tags"]
        if "additionalNotes" in kwargs:
            payload["annotations"]["additionalNotes"] = kwargs["additionalNotes"]
        if "pointOfContactIds" in kwargs:
            payload["annotations"]["pointOfContactIds"] = kwargs["pointOfContactIds"]
        return self._api.post(f"{V2_PREFIX}/ip-range", json=payload).json()

    def delete(self, id: str) -> bool:
        """
        Delete the given IP Range, and all connections to other data.
        NOTE: This will only work for user-defined IP Ranges.

        Args:
            id (str):
                ID for the ip-range. Should be a UUID.

        Returns:
            :obj:`boolean`:
                `True` if the range was successfully deleted, otherwise `False`.

        Examples:
            >>> # Deletes a user defined range
            >>> client.assets.ip_range.v2.delete("43a5a569-27b0-39b5-98f4-22b9885546d7")
        """
        return (
            True
            if self._api.delete(f"{V2_PREFIX}/ip-range/{id}").status_code == 204
            else False
        )

    def update(self, id: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Allows the partial update of the given IP Range.

        Args:
            id (str):
                ID for the ip-range. Should be a UUID.
            startAddress (str, optional):
                Start address of custom ip-range.
            endAddress (str, optional):
                End address of custom ip-range.
            parentId (str, optional):
                Id of parent ip-range.
            tags (list, optional):
                A list of tag annotation ids.
            additionalNotes (str, optional):
                Any additional notes about the custom ip-range.
            pointOfContactIds (list, optional):
                A lost of point-of-contact annotation ids.

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about the updated, custom IP Range.

        Examples:
            >>> # Update an ip-range under a parent range
            >>> new_range = client.assets.ip_range.v2.update("43a5a569-27b0-39b5-98f4-22b9885546d7", additionalNotes="Business Unit X - Development Environment")
        """
        payload = {}
        if "startAddress" in kwargs:
            payload["startAddress"] = kwargs["startAddress"]
        if "endAddress" in kwargs:
            payload["endAddress"] = kwargs["endAddress"]
        if "parentId" in kwargs:
            payload["parentId"] = kwargs["parentId"]

        if any(
            arg in ("tags", "additionalNotes", "pointOfContactIds") for arg in kwargs
        ):
            payload["annotations"] = {}
        if "tags" in kwargs:
            payload["annotations"]["tags"] = kwargs["tags"]
        if "additionalNotes" in kwargs:
            payload["annotations"]["additionalNotes"] = kwargs["additionalNotes"]
        if "pointOfContactIds" in kwargs:
            payload["annotations"]["pointOfContactIds"] = kwargs["pointOfContactIds"]
        return self._api.patch(f"{V2_PREFIX}/ip-range/{id}", json=payload).json()

    def tag(self, ranges: List[str], tags: List[str]) -> bool:
        """
        Adds the provided tags to all of the specified ip ranges.
        If the any of the provided tags do not exist, they will be created.

        Args:
            ranges (list):
                A list of ip-range IDs. Should be UUIDs.
            tags (list):
                A list of tag annotation names to add to an ip-range.

        Returns:
            :obj:`boolean`:
                `True` if the ranges were tagged successfully, otherwise `False`.
        """
        payload = {"ipRangeIds": ranges, "tags": tags}
        return self._api.post(f"{V2_PREFIX}/ip-range/tag", json=payload)
