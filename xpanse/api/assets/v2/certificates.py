from typing import Any, Dict, List, Union

from xpanse.const import V2_PREFIX
from xpanse.endpoint import ExEndpoint
from xpanse.error import UnexpectedValueError
from xpanse.iterator import ExResultIterator


class CertificatesEndpoint(ExEndpoint):
    """
    Part of the Assets v2 API for handling asset certificates.
    See: https://api.expander.expanse.co/api/v1/docs/
    """

    def list(self, **kwargs: Any) -> ExResultIterator:
        """
        Returns the list of asset certificates. Arguments should be passed as keyword args using
        the names below.

        Args:
            limit (int, optional):
                Returns at most this many results in a single api call.
            pageToken (str, optional):
                Returns results starting at this page Token.
            commonNameSearch (str, optional):
                Search for given domain value via substring match.
            recentIp (str, optional):
                Filter by IP; Returns only assets with a recent IP matching the provided filter.
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
            property (str, optional):
                Comma-separated string; Returns only results whose certificate property falls in the provided list.
                NOTE: If omitted, API will return results for all properties the user has permissions to view.
            minLastObservedDate (str, optional):
                Filter by last observed timestamp. Date formatted string (YYYY-MM-DD).
            certificateAdvertisementStatus (str, optional):
                Comma-separated string; Returns only result whose asset's certificate advertisement statuses fall in the provided list.
                Valid values are `HAS_CERTIFICATE_ADVERTISEMENT` and `NO_CERTIFICATE_ADVERTISEMENT`.
            serviceStatus (str, optional):
                Comma-separated string; Returns only result whose asset's service statuses fall in the provided list.
                Valid values are `HAS_ACTIVE_SERVICE`, `NO_ACTIVE_SERVICE`, `HAS_ACTIVE_CLOUD_SERVICE`, `NO_ACTIVE_CLOUD_SERVICE`,
                `HAS_ACTIVE_ON_PREM_SERVICE`, and `NO_ACTIVE_ON_PREM_SERVICE`.
            hostingEnvironment (str, optional):
                Filter by Hosting Environment. Allowed values are `ON_PREM`, `CLOUD`, `NONE`, `RESERVED_IPS`.
            hasRelatedCloudResources (boolean, optional):
                Filter by whether the asset has a related cloud resource asset.
            tagId (str, optional):
                Comma-separated string; Returns any assets with a tagId in the provided set.
            tagName (str, optional):
                Comma-separated string; Returns any assets with a tagName in the provided set.
            include (str, optional:
                Comma-separated string; Include the provided fields as part of the serialized result.
                Allowed Values:
                    certDetails: populate all elements in data[*].details.
                    Note: If param is not specified, data[*].details will be empty.
            sort (str, optional):
                Comma-separated string; orders results by the given fields. If the field name is
                prefixed by a -, then the ordering will be descending for that field.
                Allowed values are `commonName`, `-commonName`, `dateAdded`, `-dateAdded`, `lastObserved`, `-lastObserved`.

        Returns:
            :obj:`ExResultIterator`:
                An iterator containing all of the certificate results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Prints all certificate objects:
            >>> for res in client.assets.certificates.v2.list():
            ...     for cert in res:
            ...         print(cert)
        """
        return ExResultIterator(self._api, f"{V2_PREFIX}/assets/certificates", kwargs)

    def count(self, **kwargs: Any) -> int:
        """
        Returns the total count of certificates. This will return -1 if for some reason the count attribute
        is not returned in an otherwise valid response payload.

        Args:
            pageToken (str, optional):
                Returns results starting at this page Token.
            commonNameSearch (str, optional):
                Search for given domain value via substring match.
            recentIp (str, optional):
                Filter by IP; Returns only assets with a recent IP matching the provided filter.
            providerId (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
            providerName (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
            formattedIssuerOrg (str, optional):
                Comma-separated string; Returns only results that were found on the given formatted issuer orgs.
                If not set, filter is ignored.
            businessUnitId (str, optional):
                Comma-separated string; Returns only results whose Business Unit's ID falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
            businessUnitName (str, optional):
                Comma-separated string; Returns only results whose Business Unit's Name falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
            property (str, optional):
                Comma-separated string; Returns only results whose certificate property falls in the provided list.
                NOTE: If omitted, API will return results for all properties the user has permissions to view.
            minLastObservedDate (str, optional):
                Filter by last observed timestamp. Date formatted string (YYYY-MM-DD).
            certificateAdvertisementStatus (str, optional):
                Comma-separated string; Returns only result whose asset's certificate advertisement statuses fall in the provided list.
                Valid values are `HAS_CERTIFICATE_ADVERTISEMENT` and `NO_CERTIFICATE_ADVERTISEMENT`.
            serviceStatus (str, optional):
                Comma-separated string; Returns only result whose asset's service statuses fall in the provided list.
                Valid values are `HAS_ACTIVE_SERVICE`, `NO_ACTIVE_SERVICE`, `HAS_ACTIVE_CLOUD_SERVICE`, `NO_ACTIVE_CLOUD_SERVICE`,
                `HAS_ACTIVE_ON_PREM_SERVICE`, and `NO_ACTIVE_ON_PREM_SERVICE`.
            issueStatus (str, optional):
                Comma-separated string; Returns only result whose asset's issue statuses fall in the provided list.
                Valid values are `New`, `Investigating`, `In Progress`, `No Risk`, `Acceptable Risk`, `Resolved`
            hostingEnvironment (str, optional):
                Filter by Hosting Environment. Allowed values are `ON_PREM`, `CLOUD`, `NONE`, `RESERVED_IPS`.
            hasRelatedCloudResources (boolean, optional):
                Filter by whether the asset has a related cloud resource asset.
            tagId (str, optional):
                Comma-separated string; Returns any assets with a tagId in the provided set.
            tagName (str, optional):
                Comma-separated string; Returns any assets with a tagName in the provided set.

        Returns:
            :int:
                The total count of certificates.

        Examples:
            >>> # Print total count of certificates containing `dev` substring.
            >>> print(client.assets.certificates.v2.count(commonNameSearch="dev"))
        """
        return (
            self._api.get(f"{V2_PREFIX}/assets/certificates/count", params=kwargs)
            .json()
            .get("count", -1)
        )

    def get(self, pemMd5Hash: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Returns the details for a given Certificate. Arguments should be passed as keyword args using
        the names below.

        Args:
            pemMd5Hash (str):
                Fully qualified domain name.
            minRecentIpLastObservedDate (str, optional):
                Filter by last observed timestamp for recent IPs. Date formatted string (YYYY-MM-DD).

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about the domain.

        Examples:
            >>> # Return Domain.
            >>> domain = client.assets.certificates.v2.get(<pemMd5Hash>)
        """
        return self._api.get(
            f"{V2_PREFIX}/assets/certificates/{pemMd5Hash}", params=kwargs
        ).json()

    def csv(self, file: str, **kwargs: Any):
        """
        Downloads filtered certificates as a csv file. Arguments should be passed as keyword args using
        the names below.

        Args:
            file (str):
                A relative path for saving the downloaded csv file.
            limit (int, optional):
                Returns at most this many results.
            commonNameSearch (str, optional):
                Search for given domain value via substring match.
            recentIp (str, optional):
                Filter by IP; Returns only assets with a recent IP matching the provided filter.
            providerId (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
            providerName (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
            formattedIssuerOrg (str, optional):
                Comma-separated string; Returns only results that were found on the given formatted issuer orgs.
                If not set, filter is ignored.
            businessUnitId (str, optional):
                Comma-separated string; Returns only results whose Business Unit's ID falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
            businessUnitName (str, optional):
                Comma-separated string; Returns only results whose Business Unit's Name falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
            property (str, optional):
                Comma-separated string; Returns only results whose certificate property falls in the provided list.
                NOTE: If omitted, API will return results for all properties the user has permissions to view.
            minLastObservedDate (str, optional):
                Filter by last observed timestamp. Date formatted string (YYYY-MM-DD).
            certificateAdvertisementStatus (str, optional):
                Comma-separated string; Returns only result whose asset's certificate advertisement statuses fall in the provided list.
                Valid values are `HAS_CERTIFICATE_ADVERTISEMENT` and `NO_CERTIFICATE_ADVERTISEMENT`.
            serviceStatus (str, optional):
                Comma-separated string; Returns only result whose asset's service statuses fall in the provided list.
                Valid values are `HAS_ACTIVE_SERVICE`, `NO_ACTIVE_SERVICE`, `HAS_ACTIVE_CLOUD_SERVICE`, `NO_ACTIVE_CLOUD_SERVICE`,
                `HAS_ACTIVE_ON_PREM_SERVICE`, and `NO_ACTIVE_ON_PREM_SERVICE`.
            issueStatus (str, optional):
                Comma-separated string; Returns only result whose asset's issue statuses fall in the provided list.
                Valid values are `New`, `Investigating`, `In Progress`, `No Risk`, `Acceptable Risk`, `Resolved`
            hostingEnvironment (str, optional):
                Filter by Hosting Environment. Allowed values are `ON_PREM`, `CLOUD`, `NONE`, `RESERVED_IPS`.
            hasRelatedCloudResources (boolean, optional):
                Filter by whether the asset has a related cloud resource asset.
            tagId (str, optional):
                Comma-separated string; Returns any assets with a tagId in the provided set.
            tagName (str, optional):
                Comma-separated string; Returns any assets with a tagName in the provided set.

        Returns:
            :obj:`boolean`:
                `True` if the download was successful, otherwise `False`.

        Examples:
            >>> # Download a csv named `api-certs.csv` for all certificates that contain `api` in their name:
            >>> cli.assets.certificates.v2.csv(file="api-certs.csv", commonNameSearch="api")
        """
        return self._api.csv(
            path=f"{V2_PREFIX}/assets/certificates/csv", file_=file, **kwargs
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
            >>> # Assign a tag to a certificate
            >>> cli.assets.certificates.bulk_tag("ASSIGN",
            ...                                  ["8e589910-c1af-3c32-ae88-9a4b2dbcfe76"],
            ...                                  ["f6164347-86d1-30cc-baf2-28bbb395403d"])
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
            f"{V2_PREFIX}/assets/certificates/tag-assignments/bulk", json=payload
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
            >>> # Assign a poc to a certificate
            >>> cli.assets.certificates.bulk_poc("ASSIGN",
            ...                                  ["8e589910-c1af-3c32-ae88-9a4b2dbcfe76"],
            ...                                  ["f6164347-86d1-30cc-baf2-28bbb395403d"])
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
            f"{V2_PREFIX}/assets/certificates/contact-assignments/bulk", json=payload
        ).json()
        if not return_raw:
            return resp.get("meta", {}).get("failureCount") == 0
        return resp

    def annotation_update(
        self,
        certificate_id: str,
        contacts: List[str] = [],
        tags: List[str] = [],
        note: str = "",
    ) -> Dict[str, Any]:
        """
        Updates the annotations for a single certificate.

        Note: This will overwrite the existing annotations for an asset.
              If any arguments are omitted, that annotation type will be
              cleared for the asset.

        Args:
            certificate_id (str):
                The uuid of the certificate.
            contacts (list, optional):
                A list of poc emails to apply to the certificate.
            tags (list, optional):
                A list of tag names to apply to the certificate.
            note (str, optional):
                An optional note that can be added to the certificate.

        Returns:
            :obj:`dict`:
                A dictionary containing the current annotations for the certificate.

        Examples:
            >>> # Update annotations for a certificate
            >>> cli.assets.certificates.annotation_update(
            ...     certificate_id="e5bdc732-522a-3864-8ff3-307d35f0f0a0",
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
            f"{V2_PREFIX}/assets/certificates/{certificate_id}/annotations",
            json=payload,
        ).json()
