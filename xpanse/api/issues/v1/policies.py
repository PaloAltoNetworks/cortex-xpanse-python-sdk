from typing import Any, Dict, Optional
from xpanse.const import V1_PREFIX
from xpanse.endpoint import ExEndpoint
from xpanse.error import UnexpectedValueError
from xpanse.iterator import ExResultIterator


class PoliciesEndpoint(ExEndpoint):
    """
    Part of the Issues V1 API.
    See: https://api.expander.expanse.co/api/v1/docs/
    """

    DEFAULT_ASSIGNEE = "Unassigned"
    DEFAULT_PRIORITY = "Low"
    DEFAULT_ENABLED_STATUS = "Off"
    ALLOWED_PRIORITIES = {"Low", "Medium", "High", "Critical"}
    ALLOWED_ENABLED_STATUSES = {"On", "Off"}

    def list(self, **kwargs: Any) -> ExResultIterator:
        """
        This endpoint will return a paginated list of issue policies.

        Args:
            limit (int, optional):
                Returns at most this many results in a single api call.
                Default is 100, max is 10000.
            pageToken (str, optional):
                Page token for pagination.
            contentSearch (str, optional):
                Returns only results whose contents match the given query.
            priority (str, optional):
                Comma-separated string; Returns only results whose priority matches one of the given values.
                Allowed values are `Critical`, `High`, `Medium`, and `Low`.
            assigneeUsername (str, optional):
                Comma-separated string; Returns only results whose assignee's username matches one of the given usernames.
                Use "Unassigned" to fetch issues that are not assigned to any user.
            enabledStatus (str, optional):
                Comma-separated string; Returns only results with enabled status matching the provided value.
                Allowed values are `Off`, `On`.
            category (str, optional):
                Comma-separated string; Returns only results whose category matches one of the given categories.
            sort (str, optional):
                The field to use to sort the returned records. Prefix with '-' to reverse the normal sort order.
                Allowed values are `issueTypeName`, `-issueTypeName`,`issueTypeId`, `-issueTypeId`, `category`, `-category`,
                `created`, `-created`, `modified`, `-modified`, `modifiedBy`, `-modifiedBy`, `priority`, `-priority`,
                `assigneeUsername`, `-assigneeUsername`, `enabledStatus`, `-enabledStatus`.

        Returns:
            :obj:`ExResultIterator`:
                An iterator containing all of the issue policy results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Return all issue policies dumped to a list:
            >>> bus =  client.issues.policies.list().dump()
        """
        return ExResultIterator(self._api, f"{V1_PREFIX}/issues/policies", kwargs)

    def count(self, **kwargs: Any) -> Dict[str, Any]:
        """
        This endpoint will return a count of all issues that match the specified filters.

        Args:
            contentSearch (str, optional):
                Returns only results whose contents match the given query.
            priority (str, optional):
                Comma-separated string; Returns only results whose priority matches one of the given values.
                Allowed values are `Critical`, `High`, `Medium`, and `Low`.
            assigneeUsername (str, optional):
                Comma-separated string; Returns only results whose assignee's username matches one of the given usernames.
                Use "Unassigned" to fetch issues that are not assigned to any user.
            enabledStatus (str, optional):
                Comma-separated string; Returns only results with enabled status matching the provided value.
                Allowed values are `Off`, `On`.
            category (str, optional):
                Comma-separated string; Returns only results whose category matches one of the given categories.

        Returns:
            :obj:`dict`:
                A dictionary containing count and overflow details.

        Examples:
            >>> # Return total policy count for enabled policies.
            >>> bus =  client.issues.policies.count(enabledStatus=)
        """
        return self._api.get(f"{V1_PREFIX}/issues/policies/count", params=kwargs).json()

    def get(self, id: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Returns the details for a given Policy. Arguments should be passed as keyword args using
        the names below.

        Args:
            id (str):
                ID of the requested policy. This will be its `issueTypeId`.

        Returns:
            :obj:`dict`:
                A dictionary containing all of the details about the policy.

        Examples:
            >>> # Return Policy.
            >>> issue = client.issues.policies.get(<id>)
        """
        return self._api.get(f"{V1_PREFIX}/issues/policies/{id}", params=kwargs).json()

    def update(
        self,
        id: str,
        assignee: Optional[str] = None,
        priority: Optional[str] = None,
        enabled: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Updates a policy.
        NOTE: This is an overwrite operation. Please specify all desired values when updating a policy, even if the value is not changing.

        Args:
            id (str):
                ID of the requested policy. This will be its `issueTypeId`.
            assignee (str, optional):
                The new default assigneeUsername for the policy. If unused it will default to `Unassigned`.
            priority (str, optional):
                The new default priority for the policy. If unused it will default to `Low`.
                Allowed values are `Critical`, `High`, `Medium`, and `Low`.
            enabled (str, optional):
                The new default enabledStatus. If unused it will default to `Off`.
                Allowed values are `Off`, `On`.

        Returns:
            :obj:`dict`:
                A dictionary containing all of the updated details about the policy.

        Examples:
            >>> # Update the Microsoft DNS Server Policy to be enabled and set to Medium.
            >>> issue = client.issues.policies.update(id="MicrosoftDnsServer", priority="Medium", enabled="On")
        """
        if priority is not None and priority not in self.ALLOWED_PRIORITIES:
            raise UnexpectedValueError(
                f"priority '{priority}' was not found in list of allowed types: {self.ALLOWED_PRIORITIES}"
            )
        if enabled is not None and enabled not in self.ALLOWED_ENABLED_STATUSES:
            raise UnexpectedValueError(
                f"enabled '{enabled}' was not found in list of allowed types: {self.ALLOWED_ENABLED_STATUSES}"
            )
        payload = {
            "assigneeUsername": assignee or self.DEFAULT_ASSIGNEE,
            "priority": priority or self.DEFAULT_PRIORITY,
            "enabledStatus": enabled or self.DEFAULT_ENABLED_STATUS,
        }
        return self._api.put(f"{V1_PREFIX}/issues/policies/{id}", json=payload).json()
