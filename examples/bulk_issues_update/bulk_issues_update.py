from sys import exit

import click
from xpanse.client import ExClient

ALLOWED_PRIORITIES = ["Critical", "High", "Medium", "Low"]
ALLOWED_STATUSES = ["New", "Investigating", "InProgress", "AcceptableRisk", "Resolved"]
PROGRESS_STATUS = "ProgressStatus"
PRIORITY = "Priority"

@click.command()
@click.option('--issue-type', 'issue_type', multiple=True, default=[],
    help='The type of issue to be filtered on. (ex. "MySQL Server"')
@click.option('--tags', 'tags', multiple=True, default=[],
    help='Tag names to be filtered on.')
@click.option('--status', 'status', default=None, type=click.Choice(ALLOWED_STATUSES),
    help="New status to set all matching issues to.")
@click.option('--priority', 'priority', default=None, type=click.Choice(ALLOWED_PRIORITIES),
    help="New priority to set all matching issues to.")
def cli(issue_type, tags, status, priority):

    # Ensure that multiple updates are not being attempted
    if status is not None and priority is not None:
        exit("Script only supports a single update during each run. Supply --priority OR --status.")
    if status is None and priority is None:
        exit("Script was not supplied an update command. Supply --priority OR --status.")
    # Initialize the Xpanse Client
    client = ExClient()

    # Map issue types from friendly name to id and join to str
    issue_type = ",".join([_issue_name_to_id(client, it) for it in issue_type])

    # Join tags to str
    tags = ",".join(tags)

    # fetch issues
    issues_to_update = client.issues.issues.list(issueTypeId=issue_type, tagName=tags).dump()
    print(f"Script will attepmt to update {len(issues_to_update)} issue to set {'status' if status is not None else 'priority'} to {status if status is not None else priority}")

    # Create update commands
    commands = []
    for issue in issues_to_update:
        if status is not None:
            commands.append((issue.get("id"), status, PROGRESS_STATUS))
        else:
            commands.append((issue.get("id"), priority, PRIORITY))

    # Run Bulk update job
    update_results = client.issues.issues.bulk_update(updates=commands)

    for i, result in enumerate(update_results.get("data")):
        print(f"Operation {i+1} returned status {result.get('status')}")


def _issue_name_to_id(cli, name):
    try:
        types = cli.issues.issue_types.list().dump()
        type_map = {t.get("name"): t.get("id") for t in types}
        return type_map[name]
    except KeyError as err:
        exit(f"Specified Issue Type '{name}' filter was not found")


if __name__ == "__main__":
    cli()
