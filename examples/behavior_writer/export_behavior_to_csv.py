from sys import exit
from csv import DictWriter

import click
from xpanse.client import ExClient


def flatten_rf(flow):
    """
    Flattens the Risky Flow objects into a flat dict to write to CSV.
    """
    return {
        "id": flow.get("id"),
        "businessUnit": flow.get("businessUnit", {}).get("name"),
        "riskRule": flow.get("riskRule", {}).get("name"),
        "internalAddress": flow.get("internalAddress"),
        "internalPort": flow.get("internalPort"),
        "externalAddress": flow.get("externalAddress"),
        "externalPort": flow.get("externalPort"),
        "flowDirection": flow.get("flowDirection"),
        "acked": flow.get("acked"),
        "protocol": flow.get("protocol"),
        "externalCountryCode": flow.get("externalCountryCode"),
        "internalCountryCode": flow.get("internalCountryCode"),
        "observationTimestamp": flow.get("observationTimestamp"),
        "created": flow.get("created"),
        "internalExposureTypes": ",".join(flow.get("internalExposureTypes")),
        "internalDomains": ",".join(flow.get("internalDomains")),
    }

@click.command()
@click.argument('file_name', type=click.File('w'))
@click.option('--created-before', 'created_before', default=None,
    help='Returns risky flows created before this timestamp. Formatted as YYYY-MM-DDTHH:MM:SS.mmmZ')
@click.option('--created-after', 'created_after', default=None,
    help='Returns risky flows created after this timestamp. Formatted as YYYY-MM-DDTHH:MM:SS.mmmZ')
@click.option('--tags', 'tags', default=None,
    help='Comma-separated string; Returns only results that are associated with the provided tags.')
@click.option('--ip', 'ip', default=None,
    help='Returns the risky flows that match the specified internal CIDR/IP Range/Address.')
def cli(file_name, created_before, created_after, tags, ip):

    # Initialize the Xpanse Client
    client = ExClient()

    # Filter and dump all Risky Flows into a list
    behavior = client.behavior.risky_flows.list(created_after=created_after,
                                                       created_before=created_before,
                                                       tag_names=tags,
                                                       internal_ip_range=ip).dump()

    # If we have o records returned, exit early
    if len(behavior) < 1:
        exit("0 Behavior flows returned for specified filters. No output file created.")

    # Extract the header fields by looking at the keys first dict in the list
    fields = list(flatten_rf(behavior[0]).keys())

    # Declare our CSV DictWriter instance
    writer = DictWriter(file_name, fieldnames=fields)

    # Writer row headers to file
    writer.writeheader()

    # For each flow collected, write it to the CSV file.
    for flow in behavior:
        writer.writerow(flatten_rf(flow))


if __name__ == "__main__":
    cli()
