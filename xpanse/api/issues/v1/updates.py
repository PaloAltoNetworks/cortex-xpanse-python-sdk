from typing import Any

from xpanse.const import V1_PREFIX
from xpanse.endpoint import ExEndpoint
from xpanse.iterator import ExResultIterator


class UpdatesEndpoint(ExEndpoint):
    """
    Part of the Issues V1 API.
    See: https://api.expander.expanse.co/api/v1/docs/
    """

    def list(self, **kwargs: Any) -> ExResultIterator:
        """
        This endpoint will return a paginated list of issues updates. An issue update is published each time a modification is made to an issue.
        These modifications could include any of the following categories: ProgressStatus, ActivityStatus, Priority, Assignee, and Comment.

        Args:
            limit (int, optional):
                Returns at most this many results in a single api call.
                Default is 100, max is 10000.
            pageToken (str, optional):
                Page token for pagination.
            include (str, optional):
                Comma-separated string; Include the provided fields as part of the serialized result.
                `issue` is the only allowed value and can be provided to include the issue object in the update response.
            createdAfter (str, optional):
                Returns only results created after the provided timestamp (YYYY-MM-DDTHH:MM:SSZ).
            createdBefore (str, optional):
                Returns only results created before the provided timestamp (YYYY-MM-DDTHH:MM:SSZ).
            sort (str, optional):
                Sort by specified properties. Allowed values are `created`, `-created`

        Returns:
            :obj:`ExResultIterator`:
                An iterator containing all of the issue update results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Return all issues updates between two dates:
            >>> for res in client.issues.updates.v1.list(createdAfter="2020-07-20T00:00:00Z", createdBefore="2020-07-21T00:00:00Z")
            ...     for issue_update in res:
            ...         print(issue_update)
        """
        return ExResultIterator(self._api, f"{V1_PREFIX}/issues/updates", kwargs)
