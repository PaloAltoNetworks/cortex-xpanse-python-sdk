from typing import List

from xpanse.const import V1_PREFIX, TaggableDataType, PublicApiFields
from xpanse.endpoint import XpanseEndpoint


from xpanse.response import XpanseResponse
from xpanse.types import Filter
from xpanse.utils import build_request_payload


# TODO:// Add documentation link from https://jira-hq.paloaltonetworks.local/browse/EXPANDR-3062
class TagsEndpoint(XpanseEndpoint):
    """
    Part of the Public API for handling Tags.
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
        """
        This method assigns new or existing tags to a set of taggable data.

        The two taggable data types are Asset Tags (AT) and IP Range Tags (IPR).

        Args:
            data_type (TaggableDataType):
                The data type you would like to tag. Currently only supports tagging
                Assets and Owned IP Ranges
            tags (List[str]):
                A list of the new or existing tag names you would like to attach.
            filters (List[Filter]):
                A list of Filters to determine the filtered set of data to which the tags should be applied.
            **kwargs:
                Any extraneous parameters you would like to include when executing your
                request with the Requests.request module. Note: By default, all payload data
                is sent under the "json" keyword for your request.

        Returns:
            :obj:`XpanseResponse`:
                An object containing the raw requests.Response and parsed data results.
                The raw response can be accessed with `<xpanse_reponse>.response` attribute.
                The parsed results can be accessed with the `<xpanse_response>.data` attribute.

        Examples:
            >>> # Attach "Awesome Tag" and "Boring Tag" to Asset with ID "abc1":
            >>> tags =  client.tags.assign(data_type=TaggableDataType.ASSETS,
            >>>                            tags=["Awesome Tag", "Boring Tag"],
            >>>                            filters=[{"field": "asm_id_list", "operator": "in", "value": ["abc1"]}])
            >>> if tags.response.status_code < 300:
            >>>     succeeded = tags.data
        """
        return self._request(
            path=self.ASSIGN_ENDPOINT,
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
        """
        This method removes existing tags from a set of taggable data.

        The two taggable data types are Asset Tags (AT) and IP Range Tags (IPR).

        Args:
            data_type (TaggableDataType):
                The data type from which you would like to remove tags. Currently only supports removing tags from
                Assets and Owned IP Ranges
            tags (List[str]):
                A list of the existing tag names you would like to remove.
            filters (List[Filter]):
                A list of Filters to determine the filtered set of data from which the tags should be removed.
            **kwargs:
                Any extraneous parameters you would like to include when executing your
                request with the Requests.request module. Note: By default, all payload data
                is sent under the "json" keyword for your request.

        Returns:
            :obj:`XpanseResponse`:
                An object containing the raw requests.Response and parsed data results.
                The raw response can be accessed with `<xpanse_reponse>.response` attribute.
                The parsed results can be accessed with the `<xpanse_response>.data` attribute.

        Examples:
            >>> # Remove "Awesome Tag" and "Boring Tag" to Asset with ID "abc1":
            >>> tags =  client.tags.remove(data_type=TaggableDataType.ASSETS,
            >>>                            tags=["Awesome Tag", "Boring Tag"],
            >>>                            filters=[{"field": "asm_id_list", "operator": "in", "value": ["abc1"]}])
            >>> if tags.response.status_code < 300:
            >>>     succeeded = tags.data
        """
        return self._request(
            path=self.REMOVE_ENDPOINT,
            data_key=self.REMOVE_DATA_KEY,
            data_type=data_type,
            tags=tags,
            filters=filters,
            **kwargs,
        )

    def _request(
        self,
        path: str,
        data_key: str,
        data_type: TaggableDataType,
        tags: List[str],
        filters: List[Filter],
        **kwargs,
    ) -> XpanseResponse:
        """
        Helper method to assign and remove tags on Assets and Owned IP Ranges.

        Args:
            path (str):
                Either the assign or remove endpoint.
            data_key (str):
                The expected response field for the request.
            data_type (TaggableDataType):
                The data type being used from TaggableDataType enum
            tags (List[str]):
                A list of str representing the tag names to be assigned or removed
            filters (List[Filter]):
                A list of filter objects to determine the set of objects to be updated
            **kwargs:
                Any extraneous parameters you would like to include when executing your
                request with the Requests.request module. Note: By default, all payload data
                is sent under the "json" keyword for your request.

        Returns:
            :obj:`XpanseResponse`:
                An object containing the raw requests.Response and parsed data results.
                The raw response can be accessed with `<xpanse_reponse>.response` attribute.
                The parsed results can be accessed with the `<xpanse_response>.data` attribute.
        """
        if data_type not in TaggableDataType:
            raise ValueError(f"Invalid TaggableDataType: {data_type}")

        extra_request_data = {PublicApiFields.TAGS: tags}
        kwargs = build_request_payload(
            filters=filters, extra_request_data=extra_request_data, **kwargs
        )
        response = self._api.post(path.format(data_type=data_type.value), **kwargs)
        return XpanseResponse(response, data_key=data_key)
