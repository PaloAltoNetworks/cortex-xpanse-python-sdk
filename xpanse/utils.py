from typing import Any, Dict, List, Optional

from xpanse.const import PublicApiFields, DEFAULT_REQUEST_PAYLOAD_FIELD
from xpanse.types import RequestData, Filter


def normalize_param_names(kwargs: Dict[str, Any]) -> Dict[str, Any]:
    """
    Replace underscores in kwarg names with hyphens.

    Args:
        kwargs:
            Any set of key-value pairs used for request query parameters.

    Returns:
        :obj: The original reference to the kwargs object with its arguments normalized.
    """
    normalized_args = {}
    if "params" in kwargs:
        for k, v in kwargs.get("params", {}).items():
            normalized_args[k.replace("_neq", "!").replace("_", "-")] = v
        kwargs["params"] = normalized_args
    return kwargs


def build_request_payload(
    request_data: Optional[RequestData] = None,
    filters: Optional[List[Filter]] = None,
    extra_request_data: Optional[dict] = None,
    payload_field: str = DEFAULT_REQUEST_PAYLOAD_FIELD,
    **kwargs
) -> Dict:
    """
    Updates the existing `request_data` to include overridden or appended data to the request payload.

    Args:
        request_data (RequestData, Optional):
                Any supplemental request_data to be included with your request. This is needed to
                implement any additional filters, offsets, limits, or sort ordering.
        filters (List[Filter]):
            A list of filter objects to be added to the request payload.
        extra_request_data (dict, Optional):
            A dictionary of any extra root level "request_data" to be provided in the payload.
        payload_field (str):
            The name of the kwarg used by the requests library when making the request.
            Default is "json", but can be set to "data".
        **kwargs:
            Any extraneous parameters you would like to include when executing your
            request with the Requests.request module. Note: By default, all payload data
            is sent under the "json" keyword for your request (see payload_field above).

    Returns:
        :dict: A reference to the original `kwargs` with the updated `request_data` payload.
    """

    kwargs[payload_field] = kwargs.get(payload_field, {})
    kwargs[payload_field][PublicApiFields.REQUEST_DATA] = {
        **kwargs[payload_field].get(PublicApiFields.REQUEST_DATA, {}),
        **(request_data if isinstance(request_data, dict) else {}),
    }

    if isinstance(filters, list):
        kwargs[payload_field][PublicApiFields.REQUEST_DATA][
            PublicApiFields.FILTERS
        ] = kwargs[payload_field][PublicApiFields.REQUEST_DATA].get(
            PublicApiFields.FILTERS, []
        )

        kwargs[payload_field][PublicApiFields.REQUEST_DATA][
            PublicApiFields.FILTERS
        ] += filters

    if isinstance(extra_request_data, dict):
        kwargs[payload_field][PublicApiFields.REQUEST_DATA].update(extra_request_data)

    return kwargs
