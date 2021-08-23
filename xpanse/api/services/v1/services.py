from typing import Any, Dict, List
from xpanse.const import V1_PREFIX
from xpanse.endpoint import ExEndpoint
from xpanse.iterator import ExResultIterator


class ServicesEndpoint(ExEndpoint):
    """
    Part of the Services V1 API.
    See: https://api.expander.expanse.co/api/v1/docs/
    """

    def list(self, **kwargs: Any) -> ExResultIterator:
        """
        This endpoint will return a paginated list of services.

        Args:
            limit (int, optional):
                Returns at most this many results in a single api call.
                Default is 100, max is 10000.
            pageToken (str, optional):
                Page token for pagination.
            queryId (str, optional):
                ID of previously stored query.
            providerId (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
                Cannot be used with providerName_neq or providerId_neq.
            providerId_neq (str, optional):
                Comma-separated string; Returns only results that were found on providers other than the given ones.
                Cannot be used with providerName or providerId.
            providerName (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
                Cannot be used with providerName_neq or providerId_neq.
            providerName_neq (str, optional):
                Comma-separated string; Returns only results that were found on providers other than the given ones.
                Cannot be used with providerName or providerId.
            businessUnitId (str, optional):
                Comma-separated string; Returns only results whose Business Unit's ID falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
                Cannot be used with businessUnitId_neq or businessUnitName_neq.
            businessUnitId_neq (str, optional):
                Comma-separated string; Returns only results whose Business Unit's ID are other than the provided list.
                NOTE: If omitted, the API will return results for all Business Units the user has permissions to view.
                Cannot be used with businessUnitId or businessUnitName.
            businessUnitName (str, optional):
                Comma-separated string; Returns only results whose Business Unit's name falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
                Cannot be used with businessUnitId_neq or businessUnitName_neq.
            businessUnitName_neq (str, optional):
                Comma-separated string; Returns only results whose Business Unit's Name are other than the provided list.
                NOTE: If omitted, the API will return results for all Business Units the user has permissions to view.
                Cannot be used with businessUnitId or businessUnitName.
            tagId (str, optional):
                Comma-separated string; Returns only results that are associated with the provided tags.
                The tag id should be used here rather than the tag name.
                Cannot be used with tagId_neq or tagName_neq.
            tagId_neq (str, optional):
                Comma-separated string; Returns any assets with a tagId other than the provided set.
                The tag id should be used here rather than the tag name.
                Cannot be used with tagId or tagName.
            tagName (str, optional):
                Comma-separated string; Returns only results that are associated with the provided tags.
                The tag name should be used here rather than the tag id.
                Cannot be used with tagId_neq or tagName_neq.
            tagName_neq (str, optional):
                Comma-separated string; Returns any assets with a tagName other than the provided set.
                The tag name should be used here rather than the tag id.
                Cannot be used with tagId or tagName.
            classificationId (str, optional):
                Comma-separated string; Returns records with the specified service classifications.
                Cannot be used with classificationId_neq.
            classificationId_neq (str, optional):
                Comma-separated string; Returns records with service classification other than the ones specified.
                Cannot be used with classificationId.
            ipSearch (str, optional):
                Search for records with ip values in the specified subnets.
                Cannot be used with ipSearch_neq.
            ipSearch_neq (str, optional):
                Search for records with ip values not in the specified subnets.
                Cannot be used with ipSearch.
            domainSearch (str, optional):
                Comma-separated string; Search for given domain values via substring match.
                Cannot be used with domainSearch_neq.
            domainSearch_neq (str, optional):
                Comma-separated string; Search for results with domains that do not match (by substring) these values.
                Cannot be used with domainSearch.
            contentSearch (str, optional):
                Search for assets via content match.
            countryCode (str, optional):
                Comma-separated string of ISO-3166 two character country codes;
                Returns any assets with an IP located in a country in the provided set.
                Cannot be used with countryCode_neq.
            countryCode_neq (str, optional):
                Comma-separated string of ISO-3166 two character country codes;
                Returns any assets with an IP located in a country other than in the provided set.
                Cannot be used with countryCode.
            activityStatus (str, optional):
                Comma-separated string; Returns only results whose activity status matches one of the given values.
                Allowed values are `Active` and `Inactive`.
                Cannot be used with activityStatus_neq.
            activityStatus_neq (str, optional):
                Comma-separated string; Returns only results whose activity status not matching one of the given values.
                Allowed values are `Active` and `Inactive`.
                Cannot be used with activityStatus.
            discoveryType (str, optional):
                Describes the way a service was discovered (ColocatedOnIp, DirectlyDiscovered).
                Cannot be used with discoveryType_neq.
            discoveryType_neq (str, optional):
                Describes the way a service was discovered (ColocatedOnIp, DirectlyDiscovered).
                Cannot be used with discoveryType.
            portNumber (str, optional):
                Comma separated string; Returns assets located on the specified port.
                Cannot be used with portNumber_neq.
            portNumber_neq (str, optional):
                Comma separated string; Returns assets located on a port other than the specified port(s).
                Cannot be used with portNumber.
            include (str, optional):
                Comma-separated string; Include the provided fields as part of the serialized result.
                Values can include (allClassificationDetails, latestClassificationDetails)
            cloudManagementStatus (str, optional):
                Comma-separated string; Returns only results whose cloud management status matches one of the given values.
                Cannot be used with cloudManagementStatus_neq.
                Allowed values are `NotApplicable`, `ManagedCloud`, `UnmanagedCloud`.
            cloudManagementStatus_neq (str, optional):
                Comma-separated string; Returns only services whose cloud management status is other than given value(s).
                Cannot be used with cloudManagementStatus.
                Allowed values are `NotApplicable`, `ManagedCloud`, `UnmanagedCloud`.
            hostingEnvironment (str, optional):
                Comma-separated string; Returns only services whose hosting environment matches one of the given value(s).
                Cannot be used with hostingEnvironment!.
                Allowed values are 'OnPrem', 'Cloud'.
            hostingEnvironment_neg (str, optional):
                Comma-separated string; Returns only services whose hosting environment is other than the given value(s).
                Cannot be used with hostingEnvironment.
                Allowed values are 'OnPrem', 'Cloud'.
            sort (str, optional):
                Sort by specified properties.

        Returns:
            :obj:`ExResultIterator`:
                An iterator containing all of the services results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Return all services dumped to a list:
            >>> bus =  client.services.v1.services.list().dump()
        """
        return ExResultIterator(self._api, f"{V1_PREFIX}/services/services", kwargs)

    def count(self, **kwargs: Any) -> Dict[str, Any]:
        """
        This endpoint will return a paginated list of services.

        Args:
            limit (int, optional):
                Returns at most this many results in a single api call.
                Default is 100, max is 10000.
            pageToken (str, optional):
                Page token for pagination.
            queryId (str, optional):
                ID of previously stored query.
            providerId (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
                Cannot be used with providerName_neq or providerId_neq.
            providerId_neq (str, optional):
                Comma-separated string; Returns only results that were found on providers other than the given ones.
                Cannot be used with providerName or providerId.
            providerName (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
                Cannot be used with providerName_neq or providerId_neq.
            providerName_neq (str, optional):
                Comma-separated string; Returns only results that were found on providers other than the given ones.
                Cannot be used with providerName or providerId.
            businessUnitId (str, optional):
                Comma-separated string; Returns only results whose Business Unit's ID falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
                Cannot be used with businessUnitId_neq or businessUnitName_neq.
            businessUnitId_neq (str, optional):
                Comma-separated string; Returns only results whose Business Unit's ID are other than the provided list.
                NOTE: If omitted, the API will return results for all Business Units the user has permissions to view.
                Cannot be used with businessUnitId or businessUnitName.
            businessUnitName (str, optional):
                Comma-separated string; Returns only results whose Business Unit's name falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
                Cannot be used with businessUnitId_neq or businessUnitName_neq.
            businessUnitName_neq (str, optional):
                Comma-separated string; Returns only results whose Business Unit's Name are other than the provided list.
                NOTE: If omitted, the API will return results for all Business Units the user has permissions to view.
                Cannot be used with businessUnitId or businessUnitName.
            tagId (str, optional):
                Comma-separated string; Returns only results that are associated with the provided tags.
                The tag id should be used here rather than the tag name.
                Cannot be used with tagId_neq or tagName_neq.
            tagId_neq (str, optional):
                Comma-separated string; Returns any assets with a tagId other than the provided set.
                The tag id should be used here rather than the tag name.
                Cannot be used with tagId or tagName.
            tagName (str, optional):
                Comma-separated string; Returns only results that are associated with the provided tags.
                The tag name should be used here rather than the tag id.
                Cannot be used with tagId_neq or tagName_neq.
            tagName_neq (str, optional):
                Comma-separated string; Returns any assets with a tagName other than the provided set.
                The tag name should be used here rather than the tag id.
                Cannot be used with tagId or tagName.
            assigneeUsername (str, optional):
                Comma-separated string; Returns only results whose assignee's username matches one of the given usernames.
                Use "Unassigned" to fetch issues that are not assigned to any user.
            classificationId (str, optional):
                Comma-separated string; Returns records with the specified service classifications.
                Cannot be used with classificationId_neq.
            classificationId_neq (str, optional):
                Comma-separated string; Returns records with service classification other than the ones specified.
                Cannot be used with classificationId.
            ipSearch (str, optional):
                Search for records with ip values in the specified subnets.
                Cannot be used with ipSearch_neq.
            ipSearch_neq (str, optional):
                Search for records with ip values not in the specified subnets.
                Cannot be used with ipSearch.
            domainSearch (str, optional):
                Comma-separated string; Search for given domain values via substring match.
                Cannot be used with domainSearch_neq.
            domainSearch_neq (str, optional):
                Comma-separated string; Search for results with domains that do not match (by substring) these values.
                Cannot be used with domainSearch.
            contentSearch (str, optional):
                Search for assets via content match.
            countryCode (str, optional):
                Comma-separated string of ISO-3166 two character country codes;
                Returns any assets with an IP located in a country in the provided set.
                Cannot be used with countryCode_neq.
            countryCode_neq (str, optional):
                Comma-separated string of ISO-3166 two character country codes;
                Returns any assets with an IP located in a country other than in the provided set.
                Cannot be used with countryCode.
            activityStatus (str, optional):
                Comma-separated string; Returns only results whose activity status matches one of the given values.
                Allowed values are `Active` and `Inactive`.
                Cannot be used with activityStatus_neq.
            activityStatus_neq (str, optional):
                Comma-separated string; Returns only results whose activity status not matching one of the given values.
                Allowed values are `Active` and `Inactive`.
                Cannot be used with activityStatus.
            discoveryType (str, optional):
                Describes the way a service was discovered (ColocatedOnIp, DirectlyDiscovered).
                Cannot be used with discoveryType_neq.
            discoveryType_neq (str, optional):
                Describes the way a service was discovered (ColocatedOnIp, DirectlyDiscovered).
                Cannot be used with discoveryType.
            portNumber (str, optional):
                Comma separated string; Returns assets located on the specified port.
                Cannot be used with portNumber_neq.
            portNumber_neq (str, optional):
                Comma separated string; Returns assets located on a port other than the specified port(s).
                Cannot be used with portNumber.
            cloudManagementStatus (str, optional):
                Comma-separated string; Returns only results whose cloud management status matches one of the given values.
                Cannot be used with cloudManagementStatus_neq.
                Allowed values are `NotApplicable`, `ManagedCloud`, `UnmanagedCloud`.
            cloudManagementStatus_neq (str, optional):
                Comma-separated string; Returns only services whose cloud management status is other than given value(s).
                Cannot be used with cloudManagementStatus.
                Allowed values are `NotApplicable`, `ManagedCloud`, `UnmanagedCloud`.
            hostingEnvironment (str, optional):
                Comma-separated string; Returns only services whose hosting environment matches one of the given value(s).
                Cannot be used with hostingEnvironment!.
                Allowed values are 'OnPrem', 'Cloud'.
            hostingEnvironment_neg (str, optional):
                Comma-separated string; Returns only services whose hosting environment is other than the given value(s).
                Cannot be used with hostingEnvironment.
                Allowed values are 'OnPrem', 'Cloud'.

        Returns:
            :obj:`dict`:
                An dictionary containing services count information

        Examples:
            >>> # Return the count of all services
            >>> count =  client.services.v1.services.count()
        """
        return self._api.get(
            f"{V1_PREFIX}/services/services/count", params=kwargs
        ).json()

    def get(self, id: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Returns the details for a given Service. Arguments should be passed as keyword args using
        the names below.

        Args:
            id (str):
                ID of the requested service.

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about the service.

        Examples:
            >>> # Return service.
            >>> service = client.services.services.get(<id>)
        """
        return self._api.get(
            f"{V1_PREFIX}/services/services/{id}", params=kwargs
        ).json()

    def csv(self, file: str, **kwargs: Any) -> bool:
        """
        This endpoint will export a filtered list of services to csv.

        Args:
            file (str):
                The name of the returned CSV file.
            limit (int, optional):
                Returns at most this many results in a single api call.
                Default is 100, max is 10000.
            pageToken (str, optional):
                Page token for pagination.
            queryId (str, optional):
                ID of previously stored query.
            providerId (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
                Cannot be used with providerName_neq or providerId_neq.
            providerId_neq (str, optional):
                Comma-separated string; Returns only results that were found on providers other than the given ones.
                Cannot be used with providerName or providerId.
            providerName (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
                Cannot be used with providerName_neq or providerId_neq.
            providerName_neq (str, optional):
                Comma-separated string; Returns only results that were found on providers other than the given ones.
                Cannot be used with providerName or providerId.
            businessUnitId (str, optional):
                Comma-separated string; Returns only results whose Business Unit's ID falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
                Cannot be used with businessUnitId_neq or businessUnitName_neq.
            businessUnitId_neq (str, optional):
                Comma-separated string; Returns only results whose Business Unit's ID are other than the provided list.
                NOTE: If omitted, the API will return results for all Business Units the user has permissions to view.
                Cannot be used with businessUnitId or businessUnitName.
            businessUnitName (str, optional):
                Comma-separated string; Returns only results whose Business Unit's name falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
                Cannot be used with businessUnitId_neq or businessUnitName_neq.
            businessUnitName_neq (str, optional):
                Comma-separated string; Returns only results whose Business Unit's Name are other than the provided list.
                NOTE: If omitted, the API will return results for all Business Units the user has permissions to view.
                Cannot be used with businessUnitId or businessUnitName.
            tagId (str, optional):
                Comma-separated string; Returns only results that are associated with the provided tags.
                The tag id should be used here rather than the tag name.
                Cannot be used with tagId_neq or tagName_neq.
            tagId_neq (str, optional):
                Comma-separated string; Returns any assets with a tagId other than the provided set.
                The tag id should be used here rather than the tag name.
                Cannot be used with tagId or tagName.
            tagName (str, optional):
                Comma-separated string; Returns only results that are associated with the provided tags.
                The tag name should be used here rather than the tag id.
                Cannot be used with tagId_neq or tagName_neq.
            tagName_neq (str, optional):
                Comma-separated string; Returns any assets with a tagName other than the provided set.
                The tag name should be used here rather than the tag id.
                Cannot be used with tagId or tagName.
            assigneeUsername (str, optional):
                Comma-separated string; Returns only results whose assignee's username matches one of the given usernames.
                Use "Unassigned" to fetch issues that are not assigned to any user.
            classificationId (str, optional):
                Comma-separated string; Returns records with the specified service classifications.
                Cannot be used with classificationId_neq.
            classificationId_neq (str, optional):
                Comma-separated string; Returns records with service classification other than the ones specified.
                Cannot be used with classificationId.
            ipSearch (str, optional):
                Search for records with ip values in the specified subnets.
                Cannot be used with ipSearch_neq.
            ipSearch_neq (str, optional):
                Search for records with ip values not in the specified subnets.
                Cannot be used with ipSearch.
            domainSearch (str, optional):
                Comma-separated string; Search for given domain values via substring match.
                Cannot be used with domainSearch_neq.
            domainSearch_neq (str, optional):
                Comma-separated string; Search for results with domains that do not match (by substring) these values.
                Cannot be used with domainSearch.
            contentSearch (str, optional):
                Search for assets via content match.
            countryCode (str, optional):
                Comma-separated string of ISO-3166 two character country codes;
                Returns any assets with an IP located in a country in the provided set.
                Cannot be used with countryCode_neq.
            countryCode_neq (str, optional):
                Comma-separated string of ISO-3166 two character country codes;
                Returns any assets with an IP located in a country other than in the provided set.
                Cannot be used with countryCode.
            activityStatus (str, optional):
                Comma-separated string; Returns only results whose activity status matches one of the given values.
                Allowed values are `Active` and `Inactive`.
                Cannot be used with activityStatus_neq.
            activityStatus_neq (str, optional):
                Comma-separated string; Returns only results whose activity status not matching one of the given values.
                Allowed values are `Active` and `Inactive`.
                Cannot be used with activityStatus.
            discoveryType (str, optional):
                Describes the way a service was discovered (ColocatedOnIp, DirectlyDiscovered).
                Cannot be used with discoveryType_neq.
            discoveryType_neq (str, optional):
                Describes the way a service was discovered (ColocatedOnIp, DirectlyDiscovered).
                Cannot be used with discoveryType.
            portNumber (str, optional):
                Comma separated string; Returns assets located on the specified port.
                Cannot be used with portNumber_neq.
            portNumber_neq (str, optional):
                Comma separated string; Returns assets located on a port other than the specified port(s).
                Cannot be used with portNumber.
            cloudManagementStatus (str, optional):
                Comma-separated string; Returns only results whose cloud management status matches one of the given values.
                Cannot be used with cloudManagementStatus_neq.
                Allowed values are `NotApplicable`, `ManagedCloud`, `UnmanagedCloud`.
            cloudManagementStatus_neq (str, optional):
                Comma-separated string; Returns only services whose cloud management status is other than given value(s).
                Cannot be used with cloudManagementStatus.
                Allowed values are `NotApplicable`, `ManagedCloud`, `UnmanagedCloud`.
            hostingEnvironment (str, optional):
                Comma-separated string; Returns only services whose hosting environment matches one of the given value(s).
                Cannot be used with hostingEnvironment!.
                Allowed values are 'OnPrem', 'Cloud'.
            hostingEnvironment_neg (str, optional):
                Comma-separated string; Returns only services whose hosting environment is other than the given value(s).
                Cannot be used with hostingEnvironment.
                Allowed values are 'OnPrem', 'Cloud'.
            sort (str, optional):
                Sort by specified properties.


        Returns:
            :obj:`boolean`:
                `True` if the download was successful, otherwise `False`.

        Examples:
            >>> # Download a csv of all services
            >>> client.services.services.csv(file="services.csv")
        """
        kwargs["filename"] = file
        return self._api.csv(
            path=f"{V1_PREFIX}/services/services/csv", file_=file, **kwargs
        )

    def updates(self, **kwargs: Any) -> ExResultIterator:
        """
        This endpoint will return a paginated list of services updates.

        Args:
            limit (int, optional):
                Returns at most this many results in a single api call.
                Default is 100, max is 10000.
            pageToken (str, optional):
                Page token for pagination.
            include (str, optional):
                Comma-separated string; Include the provided fields as part of the serialized result.
                `service` is the only allowed value and can be provided to include the service object in the update response.
            createdAfter (str, optional):
                Returns only results created after the provided timestamp (YYYY-MM-DDTHH:MM:SSZ).
            createdBefore (str, optional):
                Returns only results created before the provided timestamp (YYYY-MM-DDTHH:MM:SSZ).

        Returns:
            :obj:`ExResultIterator`:
                An iterator containing all of the service update results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Return all services updates between two dates:
            >>> for res in client.services.v1.services.updates(createdAfter="2020-12-20T00:00:00Z", createdBefore="2020-12-21T00:00:00Z")
            ...     for service_update in res:
            ...         print(service_update)
        """
        return ExResultIterator(self._api, f"{V1_PREFIX}/services/updates", kwargs)
