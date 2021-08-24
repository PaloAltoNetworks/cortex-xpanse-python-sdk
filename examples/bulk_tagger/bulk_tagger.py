from csv import reader

import click
from xpanse.client import ExClient




def fetch_tags(client):
    return client.annotations.tags.list(disabled=False).dump()


def create_tag(client, tag):
    print(f"Creating a new tag named {tag}")
    return client.annotations.tags.create(name=tag)["id"]


def build_tag_id_list(client, tags, tag_map):
    id_list = []
    for tag in tags.split("|"):
        tag = tag.strip()
        if tag in tag_map:
            id_list.append(tag_map[tag])
        else:
            new_tag = create_tag(client, tag)
            tag_map[tag] = new_tag
            id_list.append(new_tag)
    return id_list, tag_map


def assign_tags(client, assetType, assetKey, tags, tag_map, operation):
    """
    Create a bulk assignment request and send to the appropriate endpoint.
    """
    assetID = None
    if assetType == "domain":
        assetID = client.assets.domains.get(name=assetKey).get("id")
    elif assetType == "certificate":
        assetID = client.assets.certificates.get(pemMd5Hash=assetKey).get("id")
    elif assetType == "cloud-resource":
        asseteID == client.assets.cloud_resources.get(cloudResourceId=assetKey).get("id")

    tag_list, tag_map = build_tag_id_list(client, tags, tag_map)

    if assetID is not None:
        print(
            f"Applying {len(tag_list)} tags to {assetType} asset {assetKey} with id {assetID}"
        )
        if assetType == "domain":
            client.assets.domains.bulk_tag(
                operation=operation, asset_ids=[assetID], tag_ids=tag_list
            )
        if assetType == "certificate":
            client.assets.certificates.bulk_tag(
                operation=operation, asset_ids=[assetID], tag_ids=tag_list
            )
        if assetType == "cloud-resource":
            client.assets.cloud_resources.bulk_tag(
                operation=operation, asset_ids=[assetID], tag_ids=tag_list
            )

    return tag_map


@click.command()
@click.argument('file_name', type=click.File('r'))
def cli(file_name):

    # Initialize the Xpanse Client
    client = ExClient()

    # Populate our tag map from name to id
    tag_map = {tag["name"]: tag["id"] for tag in fetch_tags(client)}

    # Wrap the input file in a csv reader
    csvreader = reader(file_name)

    # Skip the header column
    next(csvreader)

    # For row of input do a bulk assignment request
    for row in csvreader:
        assetType, assetKey, tagNames, operation = row
        tag_map = assign_tags(
            client=client,
            assetType=assetType.strip(),
            assetKey=assetKey.strip(),
            tags=tagNames,
            tag_map=tag_map,
            operation=operation,
        )


if __name__ == "__main__":
    cli()
