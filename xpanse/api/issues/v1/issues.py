from typing import Any, Dict, List, Tuple

from xpanse.const import V1_PREFIX
from xpanse.endpoint import ExEndpoint
from xpanse.error import UnexpectedValueError
from xpanse.iterator import ExResultIterator

VALID_UPDATE_TYPES = {
    "Assignee",
    "Comment",
    "Priority",
    "ProgressStatus",
}


class IssuesEndpoint(ExEndpoint):
    """
    Part of the Issues V1 API.
    See: https://api.expander.expanse.co/api/v1/docs/
    """

    def list(self, **kwargs: Any) -> ExResultIterator:
        """
        This endpoint will return a paginated list of issues.

        Args:
            limit (int, optional):
                Returns at most this many results in a single api call.
                Default is 100, max is 10000.
            pageToken (str, optional):
                Page token for pagination.
            contentSearch (str, optional):
                Returns only results whose contents match the given query.
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
                Comma-separated string; Returns only results whose Business Unit's name falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
            assigneeUsername (str, optional):
                Comma-separated string; Returns only results whose assignee's username matches one of the given usernames.
                Use "Unassigned" to fetch issues that are not assigned to any user.
            issueTypeId (str, optional):
                Comma-separated string; Returns only results whose issue type name matches one of the given types.
            issueTypeName (str, optional):
                Comma-separated string; Returns only results whose issue type name matches one of the given types.
            inetSearch (str, optional):
                Search for results in a given IP/CIDR block using a single IP (d.d.d.d), a dashed IP range (d.d.d.d-d.d.d.d),
                a CIDR block (d.d.d.d/m), a partial CIDR (d.d.), or a wildcard (d.d.*.d).
                Returns results whose identifier includes an IP matching the query.
            domainSearch (str, optional):
                Search for a a given domain value via substring match.
                Returns results whose identifier includes a domain matching the query.
            portNumber (str, optional):
                Comma-separated string; Returns only results whose identifier includes one of the given port numbers.
            progressStatus (str, optional):
                Comma-separated string; Returns only results whose progress status matches one of the given values.
                Allowed values are `New`, `Investigating`, `InProgress`, `AcceptableRisk`, `Resolved`.
            activityStatus (str, optional):
                Comma-separated string; Returns only results whose activity status matches one of the given values.
                Allowed values are `Active` and `Inactive`.
            priority (str, optional):
                Comma-separated string; Returns only results whose priority matches one of the given values.
                Allowed values are `Critical`, `High`, `Medium`, and `Low`.
            tagName (str, optional):
                Comma-separated string; Returns only results that are associated with the provided tags.
                The tag name should be used here rather than the tag id.
            tagId (str, optional):
                Comma-separated string; Returns only results that are associated with the provided tags.
                The tag id should be used here rather than the tag name.
            createdAfter (str, optional):
                Returns only results created after the provided timestamp (YYYY-MM-DDTHH:MM:SSZ).
            createdBefore (str, optional):
                Returns only results created before the provided timestamp (YYYY-MM-DDTHH:MM:SSZ).
            modifiedAfter (str, optional):
                Returns only results modified after the provided timestamp (YYYY-MM-DDTHH:MM:SSZ).
            modifiedBefore (str, optional):
                Returns only results modified before the provided timestamp (YYYY-MM-DDTHH:MM:SSZ).
            countryCode (str, optional):
                Comma-separated string of ISO-3166 two character country codes; Returns any assets with an IP located in a country in the provided set.
            cloudManagementStatus (str, optional):
                Comma-separated string; Returns only results whose cloud management status matches one of the given values.
                Allowed values are `NotApplicable`, `ManagedCloud`, `UnmanagedCloud`.
            sort (str, optional):
                Sort by specified properties.
                Allowed values are `created`, `-created`, `modified`, `-modified`, `assigneeUsername`, `-assigneeUsername`,
                `priority`, `-priority`, `progressStatus`, `-progressStatus`, `activityStatus`, `-activityStatus`, `headline`, and `-headline`.

        Returns:
            :obj:`ExResultIterator`:
                An iterator containing all of the issues results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Return all issues dumped to a list:
            >>> bus =  client.issues.issues.list().dump()
        """
        return ExResultIterator(self._api, f"{V1_PREFIX}/issues/issues", kwargs)

    def count(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Get a count of issues. Returns the total count of issues matching the provided filters, up to 10K.

        Args:
            contentSearch (str, optional):
                Returns only results whose contents match the given query.
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
                Comma-separated string; Returns only results whose Business Unit's name falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
            assigneeUsername (str, optional):
                Comma-separated string; Returns only results whose assignee's username matches one of the given usernames.
                Use "Unassigned" to fetch issues that are not assigned to any user.
            issueTypeId (str, optional):
                Comma-separated string; Returns only results whose issue type name matches one of the given types.
            issueTypeName (str, optional):
                Comma-separated string; Returns only results whose issue type name matches one of the given types.
            inetSearch (str, optional):
                Search for results in a given IP/CIDR block using a single IP (d.d.d.d), a dashed IP range (d.d.d.d-d.d.d.d),
                a CIDR block (d.d.d.d/m), a partial CIDR (d.d.), or a wildcard (d.d.*.d).
                Returns results whose identifier includes an IP matching the query.
            domainSearch (str, optional):
                Search for a a given domain value via substring match.
                Returns results whose identifier includes a domain matching the query.
            portNumber (str, optional):
                Comma-separated string; Returns only results whose identifier includes one of the given port numbers.
            progressStatus (str, optional):
                Comma-separated string; Returns only results whose progress status matches one of the given values.
                Allowed values are `New`, `Investigating`, `InProgress`, `AcceptableRisk`, `Resolved`.
            activityStatus (str, optional):
                Comma-separated string; Returns only results whose activity status matches one of the given values.
                Allowed values are `Active` and `Inactive`.
            priority (str, optional):
                Comma-separated string; Returns only results whose priority matches one of the given values.
                Allowed values are `Critical`, `High`, `Medium`, and `Low`.
            tag (str, optional):
                Comma-separated string; Returns only results that are associated with the provided tags.
                The tag name should be used here rather than the tag id.
            createdAfter (str, optional):
                Returns only results created after the provided timestamp (YYYY-MM-DDTHH:MM:SSZ).
            createdBefore (str, optional):
                Returns only results created before the provided timestamp (YYYY-MM-DDTHH:MM:SSZ).
            modifiedAfter (str, optional):
                Returns only results modified after the provided timestamp (YYYY-MM-DDTHH:MM:SSZ).
            modifiedBefore (str, optional):
                Returns only results modified before the provided timestamp (YYYY-MM-DDTHH:MM:SSZ).
            cloudManagementStatus (str, optional):
                Comma-separated string; Returns only results whose cloud management status matches one of the given values.
                Allowed values are `NotApplicable`, `ManagedCloud`, `UnmanagedCloud`.

        Returns:
            :obj:`dict`:
                A dictionary containing count and overflow details.

        Examples:
            >>> # Return total issue count for assets with the `validated` tag.
            >>> bus =  client.issues.issues.v1.count(tag="validated")
        """
        return self._api.get(f"{V1_PREFIX}/issues/issues/count", params=kwargs).json()

    def counts(self, include="issueTypeId", **kwargs):
        """
        Get bulk counts of issues. Returns the counts of issues matching the provided filters for each value of the fields specified by the include parameter,
        up to 100 per value. At this time, the only supported value for the include parameter is issueTypeId.
        Filters for the field specified by the include parameter are ignored when computing counts for that field.

        Args:
            include (str):
                Comma-separated string; Include counts for all possible values of the provided fields.
                Allowed values are `issueTypeId`.
            contentSearch (str, optional):
                Returns only results whose contents match the given query.
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
                Comma-separated string; Returns only results whose Business Unit's name falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
            assigneeUsername (str, optional):
                Comma-separated string; Returns only results whose assignee's username matches one of the given usernames.
                Use "Unassigned" to fetch issues that are not assigned to any user.
            issueTypeId (str, optional):
                Comma-separated string; Returns only results whose issue type name matches one of the given types.
            issueTypeName (str, optional):
                Comma-separated string; Returns only results whose issue type name matches one of the given types.
            inetSearch (str, optional):
                Search for results in a given IP/CIDR block using a single IP (d.d.d.d), a dashed IP range (d.d.d.d-d.d.d.d),
                a CIDR block (d.d.d.d/m), a partial CIDR (d.d.), or a wildcard (d.d.*.d).
                Returns results whose identifier includes an IP matching the query.
            domainSearch (str, optional):
                Search for a a given domain value via substring match.
                Returns results whose identifier includes a domain matching the query.
            portNumber (str, optional):
                Comma-separated string; Returns only results whose identifier includes one of the given port numbers.
            progressStatus (str, optional):
                Comma-separated string; Returns only results whose progress status matches one of the given values.
                Allowed values are `New`, `Investigating`, `InProgress`, `AcceptableRisk`, `Resolved`.
            activityStatus (str, optional):
                Comma-separated string; Returns only results whose activity status matches one of the given values.
                Allowed values are `Active` and `Inactive`.
            priority (str, optional):
                Comma-separated string; Returns only results whose priority matches one of the given values.
                Allowed values are `Critical`, `High`, `Medium`, and `Low`.
            tag (str, optional):
                Comma-separated string; Returns only results that are associated with the provided tags.
                The tag name should be used here rather than the tag id.
            createdAfter (str, optional):
                Returns only results created after the provided timestamp (YYYY-MM-DDTHH:MM:SSZ).
            createdBefore (str, optional):
                Returns only results created before the provided timestamp (YYYY-MM-DDTHH:MM:SSZ).
            modifiedAfter (str, optional):
                Returns only results modified after the provided timestamp (YYYY-MM-DDTHH:MM:SSZ).
            modifiedBefore (str, optional):
                Returns only results modified before the provided timestamp (YYYY-MM-DDTHH:MM:SSZ).
            cloudManagementStatus (str, optional):
                Comma-separated string; Returns only results whose cloud management status matches one of the given values.
                Allowed values are `NotApplicable`, `ManagedCloud`, `UnmanagedCloud`.


        Returns:
            :obj:`dict`:
                A dictionary containing field count and overflow details.

        Examples:
            >>> # Return total issue counts
            >>> bus =  client.issues.issues.v1.counts()
        """
        kwargs["include"] = include
        return self._api.get(f"{V1_PREFIX}/issues/issues/counts", params=kwargs).json()

    def get(self, id, **kwargs):
        """
        Returns the details for a given Issue. Arguments should be passed as keyword args using
        the names below.

        Args:
            id (str):
                ID of the requested issue.

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about the issue.

        Examples:
            >>> # Return Issue.
            >>> issue = client.issues.issues.get(<id>)
        """
        return self._api.get(f"{V1_PREFIX}/issues/issues/{id}", params=kwargs).json()

    def get_updates(self, id: str, **kwargs: Any) -> ExResultIterator:
        """
        Returns the issue updates for a specified issue. Arguments should be passed as keyword args using
        the names below.

        Args:
            id (str):
                ID of the requested issue.
            limit (int, optional):
                Returns at most this many results in a single api call.
                Default is 100, max is 10000.
            pageToken (str, optional):
                Page token for pagination.

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about the issue's updates.

        Examples:
            >>> # Return updates for issue and dump to list.
            >>> issue_updates = client.issues.issues.get_updates(<id>).dump()
        """
        return ExResultIterator(
            self._api, f"{V1_PREFIX}/issues/issues/{id}/updates", kwargs
        )

    def get_update(self, id: str, update_id: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Returns the update details for a specified issue and update. Arguments should be passed as keyword args using
        the names below.

        Args:
            id (str):
                ID of the requested issue.
            update_id (str):
                ID of the requested issue update.

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about the issue update.

        Examples:
            >>> # Return issue update details
            >>> issue_update = client.issues.issues.get_update(id=<id>, update_id=<update_id>)
        """
        return self._api.get(
            f"{V1_PREFIX}/issues/issues/{id}/updates/{update_id}", params=kwargs
        ).json()

    def update(
        self, id: str, value: str, updateType: str, **kwargs: Any
    ) -> Dict[str, Any]:
        """
        Make an update to an issue. Requires a value and an updateType.
        Valid updateType values include: `Assignee`, `Comment`, `Priority`, or `ProgressStatus`.
        Valid values will vary based on the updateType, with some being limited and others being open text fields.
        Assignee - `value` must be an existing username.
        Comment - `value` can be any plaintext.
        Priority - `value` can be `Low`, `Medium`, `High`, or `Critical`
        ProgressStatus - `value` can be `New`, `Investigating`, `InProgress`, `AcceptableRisk`, or `Resolved`

        Args:
            id (str):
                ID of the requested issue.
            value (str):
                The value to be updated.
            updateType (str):
                The update type to be performed.
                Allowed types are `Assignee`, `Comment`, `Priority`, or `ProgressStatus`.

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about the issue's updates.

        Examples:
            >>> # Return updates for issue and dump to list.
            >>> updates = client.issues.issues.update(id=<id>, value=<username>, updateType="Assignee")
        """
        if id is None or value is None or updateType is None:
            raise UnexpectedValueError("A required update value was missing")
        if updateType not in VALID_UPDATE_TYPES:
            raise UnexpectedValueError(
                f"updateType '{updateType}' was not found in list of allowed types: {VALID_UPDATE_TYPES}"
            )
        payload = {"value": value, "updateType": updateType}
        return self._api.post(
            f"{V1_PREFIX}/issues/issues/{id}/updates", json=payload
        ).json()

    def bulk_update(
        self, updates: List[Tuple[str, str, str]], **kwargs: Any
    ) -> Dict[str, Any]:
        """
        Makes updates to multiple issues. Requires an id, value, and updateType for each issue.
        Valid updateType values include: `Assignee`, `Comment`, `Priority`, or `ProgressStatus`.
        Valid values will vary based on the updateType, with some being limited and others being open text fields.
        Assignee - `value` must be an existing username.
        Comment - `value` can be any plaintext.
        Priority - `value` can be `Low`, `Medium`, `High`, or `Critical`
        ProgressStatus - `value` can be `New`, `Investigating`, `InProgress`, `AcceptableRisk`, or `Resolved`

        Args:
            updates (list):
                A list of tuples containing (`id`, `value`, `updateType`), where id is the issue ID, value is the assigned value
                and updateType is one of the following values `Assignee`, `Comment`, `Priority`, `ProgressStatus`, or `ActivityStatus`.

        Returns:
            :obj:`dict`:
                A dictionary containing details about the bulk update's execution.

        Examples:
            >>> # Return updates for issue and dump to list.
            >>> response = client.issues.issues.bulk_update([('7320d57a-a39f-3bae-beae-9e56b1cf95cc', 'InProgress', 'ProgressStatus')])
        """
        payload = []
        for items in updates:
            id_, value, updateType = items
            if id_ is None or value is None or updateType is None:
                raise UnexpectedValueError(f"A required update value was missing")
            if updateType not in VALID_UPDATE_TYPES:
                raise UnexpectedValueError(
                    f"updateType '{updateType}' was not found in list of allowed types: {VALID_UPDATE_TYPES}"
                )
            payload.append(
                {
                    "issueId": id_,
                    "updateRequest": {"value": value, "updateType": updateType},
                }
            )
        return self._api.post(
            f"{V1_PREFIX}/issues/issues/bulk", json={"operations": payload}
        ).json()

    def csv(self, file: str, **kwargs: Any) -> bool:
        """
        This endpoint will export a filtered list of issues to csv.

        Args:
            file (str):
                The name of the returned CSV file.
            limit (int, optional):
                Returns at most this many results in a single api call.
                Default is 100, max is 10000.
            pageToken (str, optional):
                Page token for pagination.
            contentSearch (str, optional):
                Returns only results whose contents match the given query.
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
                Comma-separated string; Returns only results whose Business Unit's name falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
            assigneeUsername (str, optional):
                Comma-separated string; Returns only results whose assignee's username matches one of the given usernames.
                Use "Unassigned" to fetch issues that are not assigned to any user.
            issueTypeId (str, optional):
                Comma-separated string; Returns only results whose issue type name matches one of the given types.
            issueTypeName (str, optional):
                Comma-separated string; Returns only results whose issue type name matches one of the given types.
            inetSearch (str, optional):
                Search for results in a given IP/CIDR block using a single IP (d.d.d.d), a dashed IP range (d.d.d.d-d.d.d.d),
                a CIDR block (d.d.d.d/m), a partial CIDR (d.d.), or a wildcard (d.d.*.d).
                Returns results whose identifier includes an IP matching the query.
            domainSearch (str, optional):
                Search for a a given domain value via substring match.
                Returns results whose identifier includes a domain matching the query.
            portNumber (str, optional):
                Comma-separated string; Returns only results whose identifier includes one of the given port numbers.
            progressStatus (str, optional):
                Comma-separated string; Returns only results whose progress status matches one of the given values.
                Allowed values are `New`, `Investigating`, `InProgress`, `AcceptableRisk`, `Resolved`.
            activityStatus (str, optional):
                Comma-separated string; Returns only results whose activity status matches one of the given values.
                Allowed values are `Active` and `Inactive`.
            priority (str, optional):
                Comma-separated string; Returns only results whose priority matches one of the given values.
                Allowed values are `Critical`, `High`, `Medium`, and `Low`.
            tag (str, optional):
                Comma-separated string; Returns only results that are associated with the provided tags.
                The tag name should be used here rather than the tag id.
            createdAfter (str, optional):
                Returns only results created after the provided timestamp (YYYY-MM-DDTHH:MM:SSZ).
            createdBefore (str, optional):
                Returns only results created before the provided timestamp (YYYY-MM-DDTHH:MM:SSZ).
            modifiedAfter (str, optional):
                Returns only results modified after the provided timestamp (YYYY-MM-DDTHH:MM:SSZ).
            modifiedBefore (str, optional):
                Returns only results modified before the provided timestamp (YYYY-MM-DDTHH:MM:SSZ).
            cloudManagementStatus (str, optional):
                Comma-separated string; Returns only results whose cloud management status matches one of the given values.
                Allowed values are `NotApplicable`, `ManagedCloud`, `UnmanagedCloud`.
            sort (str, optional):
                Sort by specified properties.
                Allowed values are `created`, `-created`, `modified`, `-modified`, `assigneeUsername`, `-assigneeUsername`,
                `priority`, `-priority`, `progressStatus`, `-progressStatus`, `activityStatus`, `-activityStatus`, `headline`, and `-headline`.

        Returns:
            :obj:`boolean`:
                `True` if the download was successful, otherwise `False`.

        Examples:
            >>> # Download a csv named `insecure_tls.csv` for all 'InsecureTLS' issues.
            >>> client.issues.issues.csv(file="insecure_tls.csv", issueTypeId="InsecureTLS")
        """
        return self._api.csv(
            path=f"{V1_PREFIX}/issues/issues/csv", file_=file, **kwargs
        )
