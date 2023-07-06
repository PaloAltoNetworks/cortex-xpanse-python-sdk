import click

from xpanse.client import XpanseClient
from xpanse.const import PublicApiFields, FilterOperator, TaggableDataType
from xpanse.error import UnexpectedResponseError

ALLOWED_DATA_TYPES = [t.name for t in TaggableDataType]


@click.command()
@click.option(
    "--data-type",
    "data_type",
    default=None,
    type=click.Choice(ALLOWED_DATA_TYPES),
    help="Data type to tag",
)
@click.option(
    "--tags",
    "tags",
    multiple=True,
    default=[],
    help="Tags to be assigned and removed from data type.",
)
def cli(data_type, tags):
    if not data_type:
        raise ValueError("An '--data-type' must be provided in the CLI.")
    if not len(tags):
        raise ValueError("At least one '--tag' must be provided in the CLI.")

    # Initialize the Xpanse Client
    # Set CORTEX_FQDN, CORTEX_API_KEY, and CORTEX_API_KEY_ID environment variables
    client = XpanseClient()

    # Request data to fetch first 100 results
    request_data = {
        PublicApiFields.SEARCH_FROM: 0,
        PublicApiFields.SEARCH_TO: 100,
    }

    if data_type == "ASSETS":
        service = client.assets
    else:
        service = client.owned_ip_ranges

    # Fetch the first 100 results for a given data type
    taggable_data = service.list(request_data=request_data).next()

    # Aggregate ids by data type
    ids = set()
    if data_type == "ASSETS":
        [ids.update(data["asm_ids"]) for data in taggable_data if data["asm_ids"]]
    else:
        ids = {data["range_id"] for data in taggable_data if data["range_id"]}

    if not len(ids):
        print(f"No data found for type '{data_type}'.")
        exit(0)
    else:
        print(f"Found {len(ids)} objects to assign and remove tags '{tags}'.")

    # Data filtering for first 100 results
    filters = [
        {
            PublicApiFields.FIELD: "asm_id_list"
            if data_type == "ASSETS"
            else "range_id_list",
            PublicApiFields.OPERATOR: FilterOperator.IN.value,
            PublicApiFields.VALUE: list(ids),
        },
    ]

    # Assign Tags
    assign_tags = client.tags.assign(
        data_type=TaggableDataType[data_type], tags=tags, filters=filters
    )
    status_code = assign_tags.response.status_code
    if status_code >= 300:
        raise UnexpectedResponseError(f"Unexpected status code {status_code}.")

    print(f"Assigned tags: {assign_tags.data}")

    # Remove Tags
    remove_tags = client.tags.remove(
        data_type=TaggableDataType[data_type], tags=tags, filters=filters
    )
    status_code = remove_tags.response.status_code
    if status_code >= 300:
        raise UnexpectedResponseError(f"Unexpected status code {status_code}.")

    print(f"Remove tags: {remove_tags.data}")


if __name__ == "__main__":
    cli()
