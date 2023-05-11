from typing import Any, Dict, List, Optional

from xpanse.const import PublicApiFields, DEFAULT_REQUEST_PAYLOAD_FIELD


def normalize_param_names(request_data: Dict[str, Any]):
    """
    Replace underscores in kwarg names with hyphens.
    """
    normalized_args = {}
    if "params" in request_data:
        for k, v in request_data.get("params", {}).items():
            normalized_args[k.replace("_neq", "!").replace("_", "-")] = v
        request_data["params"] = normalized_args
    return request_data


def build_request_payload(
    request_data: Optional[dict] = None,
    filters: Optional[List[dict]] = None,
    extra_request_data: Optional[dict] = None,
    payload_field: str = DEFAULT_REQUEST_PAYLOAD_FIELD,
    **kwargs
) -> Dict:
    """
    Updates the existing request_data to include overridden or appended data to the request payload.
    Args:
        request_data: User specified "request_data" payload
        filters: A list of Public API filters
        extra_request_data: A dictionary of any extra root level "request_data" to be provided in the payload.
        payload_field: The name of the kwarg used by the requests library when making the request.
                       Default is "json", but is sometimes set to "data".
        **kwargs: The user specified kwargs

    Returns:
        :dict: A reference to the original request_data with the updated payload.
    """

    kwargs[payload_field] = kwargs.get(payload_field, {})
    kwargs[payload_field][PublicApiFields.REQUEST_DATA] = {
        **kwargs[payload_field].get(PublicApiFields.REQUEST_DATA, {}),
        **(request_data if isinstance(request_data, dict) else {}),
    }

    if filters is not None:
        kwargs[payload_field][PublicApiFields.REQUEST_DATA][
            PublicApiFields.FILTERS
        ] = kwargs[payload_field][PublicApiFields.REQUEST_DATA].get(
            PublicApiFields.FILTERS, []
        )

        kwargs[payload_field][PublicApiFields.REQUEST_DATA][
            PublicApiFields.FILTERS
        ] += filters

    if extra_request_data is not None:
        kwargs[payload_field][PublicApiFields.REQUEST_DATA].update(extra_request_data)

    return kwargs
