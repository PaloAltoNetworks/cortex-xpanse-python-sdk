from typing import Any, Dict, List, Union

from xpanse.const import V2_PREFIX
from xpanse.endpoint import ExEndpoint
from xpanse.error import UnexpectedValueError
from xpanse.iterator import ExResultIterator


class CloudResourcesEndpoint(ExEndpoint):
    """
    Part of the Assets v2 API for handling cloud resources.
    See: https://api.expander.expanse.co/api/v1/docs/
    """

    def list(self, **kwargs: Any) -> ExResultIterator:
        """
        Returns the list of Cloud Resources. Arguments should be passed as keyword args using
        the names below.

        Args:
            limit (int, optional):
                Returns at most this many results in a single api call.
                Default is 100, max is 10000.
            pageToken (str, optional):
                Returns results starting at this Page Token.
            accountIntegrationIds (str, optional):
                Filter by provider account integrations by IDs.
            inetSearch (str, optional):
                Search for given inet range.
            domainSearch (str, optional):
                Search for given domain value via substring match.
            providerId (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
            providerName (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
            businessUnitId (str, optional):
                Comma-separated string; Returns only results whose Business Unit's ID falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
            businessUnitName (str, optional):
                Comma-separated string; Returns only results whose Business Unit's Name falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
            type_ (str, optional):
                Comma-separated string; Returns only results that were found on the given resource type.
                If not set, results will include anything regardless of resource type.
            region (str, optional):
                Comma-separated string; Returns only results that were found on the given region.
                If not set, results will include anything regardless of region.
            minLastObservedDate (str, optional):
                Filter by last observed timestamp. Date formatted string (YYYY-MM-DD).
            tagId (str, optional):
                Comma-separated string; Returns any assets with a tagId in the provided set.
            tagName (str, optional):
                Comma-separated string; Returns any assets with a tagName in the provided set.
            serviceStatus (str, optional):
                Comma-separated string; Returns only result whose asset's service statuses fall in the provided list.
                Valid values are `HAS_ACTIVE_SERVICE`, `NO_ACTIVE_SERVICE`, `HAS_ACTIVE_CLOUD_SERVICE`, `NO_ACTIVE_CLOUD_SERVICE`,
                `HAS_ACTIVE_ON_PREM_SERVICE`, and `NO_ACTIVE_ON_PREM_SERVICE`.
            issueStatus (str, optional):
                Comma-separated string; Returns only result whose asset's issue statuses fall in the provided list.
                Valid values are `New`, `Investigating`, `In Progress`, `No Risk`, `Acceptable Risk`, `Resolved`
            sort (str, optional):
                Sort by specified properties.

        Returns:
            :obj:`ExResultIterator`:
                An iterator containing all of the cloud_resources results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Return all cloud_resources and print each resource:
            >>> for res in client.assets.cloud_resources.v2.list():
            ...     for resource in res:
            ...         print(resource)
        """
        return ExResultIterator(
            self._api, f"{V2_PREFIX}/assets/cloud-resources", kwargs
        )

    def count(self, **kwargs: Any) -> int:
        """
        Returns the total count of Cloud Resources. This will return -1 if for some reason the count attribute
        is not returned in an otherwise valid response payload.

        Args:
            accountIntegrationIds (str, optional):
                Filter by provider account integrations by IDs.
            inetSearch (str, optional):
                Search for given inet range.
            domainSearch (str, optional):
                Search for given domain value via substring match.
            providerId (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
            providerName (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
            businessUnitId (str, optional):
                Comma-separated string; Returns only results whose Business Unit's ID falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
            businessUnitName (str, optional):
                Comma-separated string; Returns only results whose Business Unit's Name falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
            type_ (str, optional):
                Comma-separated string; Returns only results that were found on the given resource type.
                If not set, results will include anything regardless of resource type.
            region (str, optional):
                Comma-separated string; Returns only results that were found on the given region.
                If not set, results will include anything regardless of region.
            minLastObservedDate (str, optional):
                Filter by last observed timestamp. Date formatted string (YYYY-MM-DD).
            tagId (str, optional):
                Comma-separated string; Returns any assets with a tagId in the provided set.
            tagName (str, optional):
                Comma-separated string; Returns any assets with a tagName in the provided set.
            serviceStatus (str, optional):
                Comma-separated string; Returns only result whose asset's service statuses fall in the provided list.
                Valid values are `HAS_ACTIVE_SERVICE`, `NO_ACTIVE_SERVICE`, `HAS_ACTIVE_CLOUD_SERVICE`, `NO_ACTIVE_CLOUD_SERVICE`,
                `HAS_ACTIVE_ON_PREM_SERVICE`, and `NO_ACTIVE_ON_PREM_SERVICE`.
            issueStatus (str, optional):
                Comma-separated string; Returns only result whose asset's issue statuses fall in the provided list.
                Valid values are `New`, `Investigating`, `In Progress`, `No Risk`, `Acceptable Risk`, `Resolved`

        Returns:
            :int:
                The total count of cloud resources.

        Examples:
            >>> # Print total count of cloud_resources containing `dev` substring.
            >>> print(client.assets.cloud_resources.v2.count(domainSearch="dev"))
        """
        return (
            self._api.get(f"{V2_PREFIX}/assets/cloud-resources/count", params=kwargs)
            .json()
            .get("count", -1)
        )

    def get(self, cloudResourceId: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Returns the details for a given Cloud Resource. Arguments should be passed as keyword args using
        the names below.

        Args:
            cloudResourceId (str):
                Internal Asset ID
            minRecentIpLastObservedDate (str, optional):
                Filter by last observed timestamp for recent IPs. Date formatted string (YYYY-MM-DD).

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about the cloud resource.

        Examples:
            >>> # Return Cloud Resource.
            >>> resource = client.assets.cloud_resources.v2.get(<cloudResourceId>)
        """
        return self._api.get(
            f"{V2_PREFIX}/assets/cloud-resources/{cloudResourceId}", params=kwargs
        ).json()

    def csv(self, file: str, **kwargs: Any) -> bool:
        """
        Downloads filtered Cloud Resources as a csv file. Arguments should be passed as keyword args using
        the names below.

        Args:
            file (str):
                A relative path for saving the downloaded csv file.
            limit (int, optional):
                Returns at most this many results.
            accountIntegrationIds (str, optional):
                Filter by provider account integrations by IDs.
            inetSearch (str, optional):
                Search for given inet range.
            domainSearch (str, optional):
                Search for given domain value via substring match.
            providerId (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
            providerName (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
            businessUnitId (str, optional):
                Comma-separated string; Returns only results whose Business Unit's ID falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
            businessUnitName (str, optional):
                Comma-separated string; Returns only results whose Business Unit's Name falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
            type_ (str, optional):
                Comma-separated string; Returns only results that were found on the given resource type.
                If not set, results will include anything regardless of resource type.
            region (str, optional):
                Comma-separated string; Returns only results that were found on the given region.
                If not set, results will include anything regardless of region.
            minLastObservedDate (str, optional):
                Filter by last observed timestamp. Date formatted string (YYYY-MM-DD).
            tagId (str, optional):
                Comma-separated string; Returns any assets with a tagId in the provided set.
            tagName (str, optional):
                Comma-separated string; Returns any assets with a tagName in the provided set.
            serviceStatus (str, optional):
                Comma-separated string; Returns only result whose asset's service statuses fall in the provided list.
                Valid values are `HAS_ACTIVE_SERVICE`, `NO_ACTIVE_SERVICE`, `HAS_ACTIVE_CLOUD_SERVICE`, `NO_ACTIVE_CLOUD_SERVICE`,
                `HAS_ACTIVE_ON_PREM_SERVICE`, and `NO_ACTIVE_ON_PREM_SERVICE`.
            issueStatus (str, optional):
                Comma-separated string; Returns only result whose asset's issue statuses fall in the provided list.
                Valid values are `New`, `Investigating`, `In Progress`, `No Risk`, `Acceptable Risk`, `Resolved`

        Returns:
            :obj:`boolean`:
                `True` if the download was successful, otherwise `False`.

        Examples:
            >>> # Download a csv named `cloud-resources.csv` for all cloud resources that are `AWS Certificate Manager` types:
            >>> cli.assets.cloud_resources.v2.csv(file="cloud-resources.csv", type_="ACM")
        """
        return self._api.csv(
            path=f"{V2_PREFIX}/assets/cloud-resources/csv", file=file, **kwargs
        )

    def types(self, **kwargs: Any) -> List[Dict[str, str]]:
        """
        Returns a list of the possible Cloud Resource types.
        NOTE: While pagination is supported here, this list is small enough that it is unnecessary, and therefore unimplemented.

        Args:
            limit (int, optional):
                Returns at most this many results in a single api call.
            pageToken (str, optional):
                Returns results starting at this Page Token.

        Returns:
            :obj:`list`:
                The different types of cloud resources.

        Examples:
            >>> # Returns supported types.
            >>> types =  client.assets.cloud_resources.v2.types()
        """
        return (
            self._api.get(f"{V2_PREFIX}/assets/cloud-resource-types", params=kwargs)
            .json()
            .get("data", [])
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
            >>> # Assign a tag to a cloud resource
            >>> cli.assets.cloud_resources.bulk_tag("ASSIGN",
            ...                                     ["8e589910-c1af-3c32-ae88-9a4b2dbcfe76"],
            ...                                     ["f6164347-86d1-30cc-baf2-28bbb395403d"])
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
            f"{V2_PREFIX}/assets/cloud-resources/tag-assignments/bulk", json=payload
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
            >>> # Assign a poc to a cloud-resource
            >>> cli.assets.cloud_resources.bulk_poc("ASSIGN",
            ...                                     ["8e589910-c1af-3c32-ae88-9a4b2dbcfe76"],
            ...                                     ["f6164347-86d1-30cc-baf2-28bbb395403d"])
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
            f"{V2_PREFIX}/assets/cloud-resources/contact-assignments/bulk", json=payload
        ).json()
        if not return_raw:
            return resp.get("meta", {}).get("failureCount") == 0
        return resp

    def annotation_update(
        self,
        cloud_resource_id: str,
        contacts: List[str] = [],
        tags: List[str] = [],
        note: str = "",
    ) -> Dict[str, Any]:
        """
        Updates the annotations for a single cloud resource.

        Note: This will overwrite the existing annotations for an asset.
              If any arguments are omitted, that annotation type will be
              cleared for the asset.

        Args:
            cloud_resource_id (str):
                The uuid of the cloud resource.
            contacts (list, optional):
                A list of poc emails to apply to the cloud resource.
            tags (list, optional):
                A list of tag names to apply to the cloud resource.
            note (str, optional):
                An optional note that can be added to the cloud resource.

        Returns:
            :obj:`dict`:
                A dictionary containing the current annotations for the cloud resource.

        Examples:
            >>> # Update annotations for a cloud resource
            >>> cli.assets.cloud_resources.annotation_update(
            ...     cloud_resource_id="e5bdc732-522a-3864-8ff3-307d35f0f0a0",
            ...     contacts=["QA@testing.com"],
            ...     tags=["sdk_test"],
            ...     note="SDK Note")
        """
        payload: Dict[str, Any] = {"tags": [], "note": note or "", "contacts": []}
        for contact in contacts:
            payload["contacts"].append({"email": contact})
        for tag in tags:
            payload["tags"].append({"name": tag})
        return self._api.put(
            f"{V2_PREFIX}/assets/cloud-resources/{cloud_resource_id}/annotations",
            json=payload,
        ).json()
