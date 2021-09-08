from typing import Any, Dict, List, Union

from xpanse.const import V2_PREFIX
from xpanse.endpoint import ExEndpoint
from xpanse.error import UnexpectedValueError
from xpanse.iterator import ExResultIterator


class DomainsEndpoint(ExEndpoint):
    """
    Part of the Assets v2 API for handling asset domains.
    See: https://api.expander.expanse.co/api/v1/docs/
    """

    def list(self, **kwargs: Any) -> ExResultIterator:
        """
        Returns the list of asset domains. Arguments should be passed as keyword args using
        the names below.

        Args:
            limit (int, optional):
                Returns at most this many results in a single api call.
            pageToken (str, optional):
                Returns results starting at this Page Token.
            domainSearch (str, optional):
                Search for given domain value via substring match.
            recentIp (str, optional):
                Filter by IP; Returns only assets with a recent IP matching the provided filter.
            providerId (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
            providerName (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
            formattedRegistrarName (str, optional):
                Comma-separated string; Returns only results that were found on the given formatted registrar names.
                If not set, filter is ignored.
            businessUnitId (str, optional):
                Comma-separated string; Returns only results whose Business Unit's ID falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
            businessUnitName (str, optional):
                Comma-separated string; Returns only results whose Business Unit's Name falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
            minLastObservedDate (str, optional):
                Filter by last observed timestamp. Date formatted string (YYYY-MM-DD).
            dnsResolutionStatus (str, optional):
                Comma-separated string; Returns only result whose asset's resolution statuses fall in the provided list.
                Valid values are `HAS_DNS_RESOLUTION`, `NO_DNS_RESOLUTION`.
            serviceStatus (str, optional):
                Comma-separated string; Returns only result whose asset's service statuses fall in the provided list.
                Valid values are `HAS_ACTIVE_SERVICE`, `NO_ACTIVE_SERVICE`, `HAS_ACTIVE_CLOUD_SERVICE`, `NO_ACTIVE_CLOUD_SERVICE`,
                `HAS_ACTIVE_ON_PREM_SERVICE`, `NO_ACTIVE_ON_PREM_SERVICE`.
            issueStatus (str, optional):
                Comma-separated string; Returns only result whose asset's issue statuses fall in the provided list.
                Valid values are `New`, `Investigating`, `In Progress`, `No Risk`, `Acceptable Risk`, `Resolved`
            hostingEnvironment (str, optional):
                Filter by Hosting Environment. Allowed values are `ON_PREM`, `CLOUD`, `NONE`, `RESERVED_IPS`.
            hasRelatedCloudResources (str, optional):
                Filter by whether the asset has a related cloud resource asset
            sort (str, optional):
                Comma-separated string; orders results by the given fields. If the field name is
                prefixed by a -, then the ordering will be descending for that field.
                Allowed values are `domain`, `-domain`, `dateAdded`, `-dateAdded`, `lastObserved`, `-lastObserved`.
            tagId (str, optional):
                Comma-separated string; Returns any assets with a tagId in the provided set.
            tagName (str, optional):
                Comma-separated string; Returns any assets with a tagName in the provided set.
            isPaidLevelDomain (bool, optional):
                `True` will return only top-level or paid level domains (i.e. example.com), `False` will return any
                subdomains(i.e. api.example.com). If omitted all domains will be returned.

        Returns:
            :obj:`ExResultIterator`:
                An iterator containing all of the domain results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Prints all domain objects:
            >>> for res in client.assets.domains.v2.list():
            ...     for domain in res:
            ...         print(domain)
        """
        return ExResultIterator(self._api, f"{V2_PREFIX}/assets/domains", kwargs)

    def count(self, **kwargs: Any) -> int:
        """
        Returns the total count of Domains. This will return -1 if for some reason the count attribute
        is not returned in an otherwise valid response payload.

        Args:
            domainSearch (str, optional):
                Search for given domain value via substring match.
            recentIp (str, optional):
                Filter by IP; Returns only assets with a recent IP matching the provided filter.
            providerId (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
            providerName (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
            formattedRegistrarName (str, optional):
                Comma-separated string; Returns only results that were found on the given formatted registrar names.
                If not set, filter is ignored.
            businessUnitId (str, optional):
                Comma-separated string; Returns only results whose Business Unit's ID falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
            businessUnitName (str, optional):
                Comma-separated string; Returns only results whose Business Unit's Name falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
            minLastObservedDate (str, optional):
                Filter by last observed timestamp. Date formatted string (YYYY-MM-DD).
            dnsResolutionStatus (str, optional):
                Comma-separated string; Returns only result whose asset's resolution statuses fall in the provided list.
                Valid values are `HAS_DNS_RESOLUTION`, `NO_DNS_RESOLUTION`.
            serviceStatus (str, optional):
                Comma-separated string; Returns only result whose asset's service statuses fall in the provided list.
                Valid values are `HAS_ACTIVE_SERVICE`, `NO_ACTIVE_SERVICE`, `HAS_ACTIVE_CLOUD_SERVICE`, `NO_ACTIVE_CLOUD_SERVICE`,
                `HAS_ACTIVE_ON_PREM_SERVICE`, `NO_ACTIVE_ON_PREM_SERVICE`.
            issueStatus (str, optional):
                Comma-separated string; Returns only result whose asset's issue statuses fall in the provided list.
                Valid values are `New`, `Investigating`, `In Progress`, `No Risk`, `Acceptable Risk`, `Resolved`.
            hostingEnvironment (str, optional):
                Filter by Hosting Environment. Allowed values are `ON_PREM`, `CLOUD`, `NONE`, `RESERVED_IPS`.
            hasRelatedCloudResources (str, optional):
                Filter by whether the asset has a related cloud resource asset.
            sort (str, optional):
                Comma-separated string; orders results by the given fields. If the field name is
                prefixed by a -, then the ordering will be descending for that field.
                Allowed values are `domain`, `-domain`, `dateAdded`, `-dateAdded`, `lastObserved`, `-lastObserved`.
            tagId (str, optional):
                Comma-separated string; Returns any assets with a tagId in the provided set.
            tagName (str, optional):
                Comma-separated string; Returns any assets with a tagName in the provided set.
            isPaidLevelDomain (bool, optional):
                `True` will return only top-level or paid level domains (i.e. example.com), `False` will return any
                subdomains(i.e. api.example.com). If omitted all domains will be returned.

        Returns:
            :int:
                The total count of domains.

        Examples:
            >>> # Print total count of domains containing `dev` substring.
            >>> print(client.assets.domains.v2.count(domainSearch="dev"))
        """
        return (
            self._api.get(f"{V2_PREFIX}/assets/domains/count", params=kwargs)
            .json()
            .get("count", -1)
        )

    def get(self, name: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Returns the details for a given Domain. Arguments should be passed as keyword args using
        the names below.

        Args:
            name (str):
                Fully qualified domain name.
            minRecentIpLastObservedDate (str, optional):
                Filter by last observed timestamp for recent IPs. Date formatted string (YYYY-MM-DD).

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about the domain.

        Examples:
            >>> # Return Domain.
            >>> domain = client.assets.domains.v2.get(<name>)
        """
        return self._api.get(f"{V2_PREFIX}/assets/domains/{name}", params=kwargs).json()

    def csv(self, file: str, **kwargs: Any) -> bool:
        """
        Downloads filtered domains as a csv file. Arguments should be passed as keyword args using
        the names below.

        Args:
            file (str):
                A relative path for saving the downloaded csv file.
            limit (int, optional):
                Returns at most this many results.
            domainSearch (str, optional):
                Search for given domain value via substring match.
            recentIp (str, optional):
                Filter by IP; Returns only assets with a recent IP matching the provided filter.
            providerId (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
            providerName (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
            formattedRegistrarName (str, optional):
                Comma-separated string; Returns only results that were found on the given formatted registrar names.
                If not set, filter is ignored.
            businessUnitId (str, optional):
                Comma-separated string; Returns only results whose Business Unit's ID falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
            businessUnitName (str, optional):
                Comma-separated string; Returns only results whose Business Unit's Name falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
            minLastObservedDate (str, optional):
                Filter by last observed timestamp. Date formatted string (YYYY-MM-DD).
            dnsResolutionStatus (str, optional):
                Comma-separated string; Returns only result whose asset's resolution statuses fall in the provided list.
                Valid values are `HAS_DNS_RESOLUTION`, `NO_DNS_RESOLUTION`.
            serviceStatus (str, optional):
                Comma-separated string; Returns only result whose asset's service statuses fall in the provided list.
                Valid values are `HAS_ACTIVE_SERVICE`, `NO_ACTIVE_SERVICE`, `HAS_ACTIVE_CLOUD_SERVICE`, `NO_ACTIVE_CLOUD_SERVICE`,
                `HAS_ACTIVE_ON_PREM_SERVICE`, `NO_ACTIVE_ON_PREM_SERVICE`.
            issueStatus (str, optional):
                Comma-separated string; Returns only result whose asset's issue statuses fall in the provided list.
                Valid values are `New`, `Investigating`, `In Progress`, `No Risk`, `Acceptable Risk`, `Resolved`.
            hostingEnvironment (str, optional):
                Filter by Hosting Environment. Allowed values are `ON_PREM`, `CLOUD`, `NONE`, `RESERVED_IPS`.
            hasRelatedCloudResources (str, optional):
                Filter by whether the asset has a related cloud resource asset.
            isPaidLevelDomain (bool, optional):
                `True` will return only top-level or paid level domains (i.e. example.com), `False` will return any
                subdomains(i.e. api.example.com). If omitted all domains will be returned.
            tagId (str, optional):
                Comma-separated string; Returns any assets with a tagId in the provided set.
            tagName (str, optional):
                Comma-separated string; Returns any assets with a tagName in the provided set.

        Returns:
            :obj:`boolean`:
                `True` if the download was successful, otherwise `False`.

        Examples:
            >>> # Download a csv named `api-domains.csv` for all domains that contain `api`:
            >>> client.assets.domains.v2.csv(file="api-domains.csv", domainSearch="api")
        """
        return self._api.csv(
            path=f"{V2_PREFIX}/assets/domains/csv", file_=file, **kwargs
        )

    def bulk_tag(
        self,
        operation: str,
        asset_ids: List[str],
        tag_ids: List[str],
        return_raw: bool = False,
    ) -> Union[bool, Dict[str, Any]]:
        """
        Assigns or unassigns tags to assets.

        Args:
            operation (str):
                Operation type. Must be ASSIGN or UNASSIGN.
            asset_ids (list):
                A list of asset uuids to assign or unassign tags from.
            tag_ids (list):
                A list of tag uuids to assign or unassign to assets.
            return_raw (bool, optional):
                If False this will return a boolean response that reflects whether
                all of the operations were successful. If True the raw json response
                will be returned. Defaults to False.

        Returns:
            :bool:
                Returns a bool reflecting the operations success unless `return_raw`
                is true, in which case a dict is returned.

        Examples:
            >>> # Assign a tag to a domain
            >>> cli.assets.domains.bulk_tag("ASSIGN",
            ...                            ["8e589910-c1af-3c32-ae88-9a4b2dbcfe76"],
            ...                            ["f6164347-86d1-30cc-baf2-28bbb395403d"])
        """
        if operation not in ["ASSIGN", "UNASSIGN"]:
            raise UnexpectedValueError(
                f"The operation type '{operation}' is not valid.'"
            )
        payload: Dict[str, Any] = {"operations": []}
        for asset_id in asset_ids:
            payload["operations"].append(
                {"operationType": operation, "assetId": asset_id, "tagIds": tag_ids}
            )
        resp = self._api.post(
            f"{V2_PREFIX}/assets/domains/tag-assignments/bulk", json=payload
        ).json()
        if not return_raw:
            return resp.get("meta", {}).get("failureCount") == 0
        return resp

    def bulk_poc(
        self,
        operation: str,
        asset_ids: List[str],
        contact_ids: List[str],
        return_raw: bool = False,
    ) -> Union[bool, Dict[str, Any]]:
        """
        Assigns or unassigns Point-of-Contacts to assets.

        Args:
            operation (str):
                Operation type. Must be ASSIGN or UNASSIGN.
            asset_ids (list):
                A list of asset uuids to assign or unassign pocs from.
            contact_ids (list):
                A list of poc uuids to assign or unassign to assets.
            return_raw (bool, optional):
                If False this will return a boolean response that reflects whether
                all of the operations were successful. If True the raw json response
                will be returned. Defaults to False.

        Returns:
            :bool:
                Returns a bool reflecting the operations success unless `return_raw`
                is true, in which case a dict is returned.

        Examples:
            >>> # Assign a poc to a domain
            >>> cli.assets.domains.bulk_poc("ASSIGN",
            ...                            ["8e589910-c1af-3c32-ae88-9a4b2dbcfe76"],
            ...                            ["f6164347-86d1-30cc-baf2-28bbb395403d"])
        """
        if operation not in ["ASSIGN", "UNASSIGN"]:
            raise UnexpectedValueError(
                f"The operation type '{operation}' is not valid.'"
            )
        payload: Dict[str, Any] = {"operations": []}
        for asset_id in asset_ids:
            payload["operations"].append(
                {
                    "operationType": operation,
                    "assetId": asset_id,
                    "contactIds": contact_ids,
                }
            )
        resp = self._api.post(
            f"{V2_PREFIX}/assets/domains/contact-assignments/bulk", json=payload
        ).json()
        if not return_raw:
            return resp.get("meta", {}).get("failureCount") == 0
        return resp

    def annotation_update(
        self,
        domain_id: str,
        contacts: List[str] = [],
        tags: List[str] = [],
        note: str = "",
    ) -> Dict[str, Any]:
        """
        Updates the annotations for a single domain.

        Note: This will overwrite the existing annotations for an asset.
              If any arguments are omitted, that annotation type will be
              cleared for the asset.

        Args:
            domain_id (str):
                The uuid of the domain.
            contacts (list, optional):
                A list of poc emails to apply to the domain.
            tags (list, optional):
                A list of tag names to apply to the domain.
            note (str, optional):
                An optional note that can be added to the domain.

        Returns:
            :obj:`dict`:
                A dictionary containing the current annotations for the domain.

        Examples:
            >>> # Update annotations for a domain
            >>> cli.assets.domains.annotation_update(
            ...     domain_id="e5bdc732-522a-3864-8ff3-307d35f0f0a0",
            ...     contacts=["QA@testing.com"],
            ...     tags=["sdk_test"],
            ...     note="SDK Note")
        """
        payload: Dict[str, Any] = {"tags": [], "note": note or "", "contacts": []}
        for contact in contacts:
            payload["contacts"].append({"email": contact})
        for tag in [t.lower() for t in tags]:
            payload["tags"].append({"name": tag})
        return self._api.put(
            f"{V2_PREFIX}/assets/domains/{domain_id}/annotations", json=payload
        ).json()
