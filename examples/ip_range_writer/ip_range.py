from csv import DictWriter
from json import dump

import click
from xpanse.client import ExClient


def flatten(obj):
    """
    Flattens a json object into a single level using dot notation.
    """
    out = {}

    def _flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                _flatten(x[a], f"{name}{a}.")
        elif type(x) is list:
            for i, a in enumerate(x):
                _flatten(a, f"{name}{i}.")
        else:
            out[name[:-1]] = x

    _flatten(obj)
    return out


@click.command()
@click.argument('file_name', type=click.File('w'))
@click.option('--tags', 'tags', default=None,
    help='Comma-separated string; Returns only results that are associated with the provided tags.')
@click.option('--ip', 'ip', default=None,
    help='Returns the IP  Ranges that match the specified internal CIDR/IP Range/Address.')
@click.option('--include-attribution', 'include_attribution', is_flag=True,
    help='Whether or not attribution details should be included with results.')
@click.option('--include-location', 'include_location', is_flag=True,
    help='Whether or not location details should be included with results.')
@click.option('--include-annotation', 'include_annotation', is_flag=True,
    help='Whether or not annotation details should be included with results.')
@click.option('--include-registration', 'include_registration', is_flag=True,
    help='Whether or not registration details should be included with results.')
@click.option('--include-severity', 'include_severity', is_flag=True,
    help='Whether or not severity details should be included with results.')
def cli(file_name, tags, ip, include_attribution, include_location, include_annotation, include_registration, include_severity):

    # Initialize the Xpanse Client
    client = ExClient()

    # Prepare arguments
    include = []
    if include_attribution:
        include.append("attributionReasons")
    if include_location:
        include.append("locationInformation")
    if include_annotation:
        include.append("annotations")
    if include_registration:
        include.append("relatedRegistrationInformation")
    if include_severity:
        include.append("severityCounts")
    include = ','.join(include) or None

    # Filter and dump all IP Ranges into a list
    ranges = client.assets.ip_range.list(inet=ip,
                                         tag_names=tags,
                                         include=include).dump()

    # Determine the correct output type
    file_type = file_name.name.split(".")[-1]
    if file_type == "json":
        # Dump to json with pretty printing
        dump(ranges, file_name, indent=4, sort_keys=True)
    elif file_type == "csv":
        # Extract the header fields by looking at all of the possible keys
        # Some objects may contain more values than others
        seen_keys = []
        for ip_range in ranges:
            for key in list(flatten(ip_range).keys()):
                if key not in seen_keys:
                    seen_keys.append(key)
        seen_keys.sort()
        # Declare our CSV DictWriter instance
        writer = DictWriter(file_name, fieldnames=seen_keys)

        # Writer row headers to file
        writer.writeheader()

        # For each range, write it to the CSV file.
        for ip_range in ranges:
            writer.writerow(flatten(ip_range))
    else:
        print("Unexpected file type, please use csv or json.")


if __name__ == "__main__":
    cli()
