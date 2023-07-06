from typing import Callable, List, Any

import click

from xpanse.client import XpanseClient
from xpanse.const import PublicApiFields, FilterOperator, AssetType
from xpanse.error import UnexpectedResponseError
from xpanse.response import XpanseResponse

ALLOWED_ASSET_TYPES = [t.value for t in AssetType]


@click.command()
@click.option(
    "--asset-type",
    "asset_type",
    default=None,
    type=click.Choice(ALLOWED_ASSET_TYPES),
    help="Asset Types to filter services from underlying assets.",
)
def cli(asset_type):
    if not asset_type:
        raise ValueError("An '--asset-type' must be provided in the CLI.")

    # Initialize the Xpanse Client
    # Set CORTEX_FQDN, CORTEX_API_KEY, and CORTEX_API_KEY_ID environment variables
    client = XpanseClient()

    # Request data to find underlying assets with external services
    request_data = {
        PublicApiFields.FILTERS: [
            {
                PublicApiFields.FIELD: "type",
                PublicApiFields.OPERATOR: FilterOperator.IN.value,
                PublicApiFields.VALUE: [asset_type],
            },
            {
                PublicApiFields.FIELD: "has_active_external_services",
                PublicApiFields.OPERATOR: FilterOperator.IN.value,
                PublicApiFields.VALUE: ["yes"],
            },
        ],
    }

    # Fetch assets with type and external services
    assets_with_type_and_service = client.assets.list(request_data=request_data).dump()

    # Aggregate asset ids for details query
    asset_ids = set()
    [
        asset_ids.update(asset["asm_ids"])
        for asset in assets_with_type_and_service
        if asset["asm_ids"]
    ]

    if not len(asset_ids):
        print(f"No assets found with active services and type '{asset_type}'.")
        exit(0)
    else:
        print(f"Found {len(asset_ids)} assets with type '{asset_type}'.")

    # Aggregate asset details for active service ids
    asset_details = _paginate_details(
        id_list=list(asset_ids),
        get_details=lambda ids: client.assets.get(asset_ids=ids),
    )
    service_ids = set()
    [
        service_ids.update(asset["active_service_ids"])
        for asset in asset_details
        if asset["active_service_ids"]
    ]

    if not len(service_ids):
        print(f"No active services found with the specified underlying assets.")
        exit(0)
    else:
        print(
            f"Found {len(service_ids)} active services with underlying asset type '{asset_type}'."
        )

    # Query services
    services = _paginate_details(
        id_list=list(service_ids),
        get_details=lambda ids: client.services.get(service_ids=ids),
    )
    print(f"Services details: {services}")


def _paginate_details(
    id_list: List[str],
    get_details: Callable[[List[str]], XpanseResponse],
    max_chunk_size: int = 20,
) -> List[Any]:
    # Cortex Public API currently only supports 20 ids for detail endpoints.
    id_chunks = [
        id_list[i : i + max_chunk_size] for i in range(0, len(id_list), max_chunk_size)
    ]

    # Paginate the chunk sizes
    details = []
    for chunk in id_chunks:
        detail = get_details(chunk)
        status_code = detail.response.status_code
        if status_code >= 300:
            raise UnexpectedResponseError(f"Unexpected status code {status_code}.")
        details += detail.data

    return details


if __name__ == "__main__":
    cli()
