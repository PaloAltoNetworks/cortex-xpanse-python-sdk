from typing import Any, Dict


def normalize_param_names(kwargs: Dict[str, Any]):
    """
    Replace underscores in kwarg names with hyphens.
    """
    normalized_args = {}
    if "params" in kwargs:
        for k, v in kwargs.get("params", {}).items():
            normalized_args[k.replace("_neq", "!").replace("_", "-")] = v
        kwargs["params"] = normalized_args
    return kwargs
