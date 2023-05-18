import sys

from typing import Any, List

from xpanse.const import FilterOperator

if sys.version_info >= (3, 11):
    from typing import TypedDict, NotRequired
else:
    from typing_extensions import TypedDict, NotRequired


class Filter(TypedDict):
    field: str
    """Field on Data Set to Filter"""

    operator: str
    """Filter Operator - Use SortOrder Enum for Values"""

    value: Any
    """Filter Value"""


class Sort(TypedDict):
    field: str
    """Field on Data Set By Which to Sort"""

    keyword: str
    """Sort Direction - Use SortOrder Enum for Values"""


class RequestData(TypedDict):
    filters: NotRequired[List[Filter]]
    """A List of Desired Filter Objects"""

    sort: NotRequired[Sort]
    """Sort Object"""

    search_from: NotRequired[int]
    """Search From Value Representing Offset"""

    search_to: NotRequired[int]
    """Search To Value Representing Limit"""

    use_page_token: NotRequired[bool]
    """Only Used For List Endpoints - Use Token Based Pagination"""

    next_page_token: NotRequired[str]
    """Only Used For List Endpoints - Sets Next Page Token"""
