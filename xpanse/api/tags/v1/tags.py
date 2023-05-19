from typing import List

from xpanse.const import V1_PREFIX, TaggableDataType, PublicApiFields
from xpanse.endpoint import XpanseEndpoint


from xpanse.response import XpanseResponse
from xpanse.types import Filter
from xpanse.utils import build_request_payload


class TagsApi(XpanseEndpoint):
    """
    Part of the Public API for handling Tags.
    See: TODO:// https://jira-hq.paloaltonetworks.local/browse/EXPANDR-3062
    """

    ASSIGN_ENDPOINT = f"{V1_PREFIX}/assets/tags/{{data_type}}/assign"
    REMOVE_ENDPOINT = f"{V1_PREFIX}/assets/tags/{{data_type}}/remove"
    ASSIGN_DATA_KEY = "assign_tags"
    REMOVE_DATA_KEY = "remove_tags"

    def assign(
        self,
        data_type: TaggableDataType,
        tags: List[str],
        filters: List[Filter],
        **kwargs,
    ) -> XpanseResponse:
        return self._request(
            endpoint=self.ASSIGN_ENDPOINT,
            data_key=self.ASSIGN_DATA_KEY,
            data_type=data_type,
            tags=tags,
            filters=filters,
            **kwargs,
        )

    def remove(
        self,
        data_type: TaggableDataType,
        tags: List[str],
        filters: List[Filter],
        **kwargs,
    ) -> XpanseResponse:
        return self._request(
            endpoint=self.REMOVE_ENDPOINT,
            data_key=self.REMOVE_DATA_KEY,
            data_type=data_type,
            tags=tags,
            filters=filters,
            **kwargs,
        )

    def _request(
        self,
        endpoint: str,
        data_key: str,
        data_type: TaggableDataType,
        tags: List[str],
        filters: List[Filter],
        **kwargs,
    ) -> XpanseResponse:
        """
        Helper method to assign and remove tags on Assets and External IP Ranges.
        Args:
            endpoint: Either the assign or remove endpoint
            data_type: The data type being used from TaggableDataType enum
            tags: A list of str representing the tag names to be assigned or removed
            filters: A list of filter objects to determine the set of objects to be updated
            **kwargs: Any keyword arguments to pass to the requests library

        Returns:
            :XpanseResponse: An Xpanse response object
        """
        if data_type not in TaggableDataType:
            raise ValueError(f"Invalid TaggableDataType: {data_type}")

        extra_request_data = {PublicApiFields.TAGS: tags}
        kwargs = build_request_payload(
            filters=filters, extra_request_data=extra_request_data, **kwargs
        )
        response = self._api.post(endpoint.format(data_type=data_type.value), **kwargs)
        return XpanseResponse(response, data_key=data_key)
