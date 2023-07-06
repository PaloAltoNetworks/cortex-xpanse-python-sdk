import click

from xpanse.client import XpanseClient
from xpanse.const import PublicApiFields, FilterOperator
from xpanse.error import UnexpectedResponseError

ALLOWED_SEVERITIES = ["critical", "high", "medium", "low", "informational"]
ALLOWED_STATUSES = [
    "NEW",
    "UNDER_INVESTIGATION",
    "RESOLVED_TRUE_POSITIVE",
    "RESOLVED_SECURITY_TESTING",
    "RESOLVED_KNOWN_ISSUE",
    "RESOLVED_DUPLICATE",
    "RESOLVED_FALSE_POSITIVE",
    "RESOLVED_OTHER",
]
STATUS = "status"
SEVERITY = "manual_severity"


@click.command()
@click.option(
    "--attack-surface-rules",
    "attack_surface_rules",
    multiple=True,
    default=[],
    help='The type of attack surface rules to be filtered on. (ex. "MySQL Server")',
)
@click.option(
    "--status",
    "status",
    default=None,
    type=click.Choice(ALLOWED_STATUSES),
    help="New status to set all matching incidents to.",
)
@click.option(
    "--severity",
    "severity",
    default=None,
    type=click.Choice(ALLOWED_SEVERITIES),
    help="New severity to set all matching incidents to.",
)
def cli(attack_surface_rules, status, severity):
    if not len(attack_surface_rules):
        raise ValueError(
            "At least 1 '--attack-surface-rules' must be provided in the CLI."
        )

    # Initialize the Xpanse Client
    # Set CORTEX_FQDN, CORTEX_API_KEY, and CORTEX_API_KEY_ID environment variables
    client = XpanseClient()

    # Get attack surface rule names
    rules = client.attack_surface_rules.list(
        request_data={"search_from": 0, "search_to": 500}
    ).dump()

    attack_surface_rule_names = [rule["attack_surface_rule_name"] for rule in rules]
    for rule in attack_surface_rules:
        if rule not in attack_surface_rule_names:
            raise ValueError(
                f"No attack surface rule found with name '{attack_surface_rules}'."
            )

    # Request data
    request_data = {
        PublicApiFields.FILTERS: [
            {
                PublicApiFields.FIELD: "attack_surface_rule_name",
                PublicApiFields.OPERATOR: FilterOperator.IN.value,
                PublicApiFields.VALUE: attack_surface_rule_names,
            },
        ],
    }

    # Fetch alerts with specified attack surface rules
    alerts_with_rules = client.alerts.list(request_data=request_data).dump()

    # Aggregate affected incidents
    incidents_to_update = {
        alert["case_id"] for alert in alerts_with_rules if alert["case_id"] is not None
    }

    if not len(incidents_to_update):
        print(f"No alerts with rules {attack_surface_rule_names} found.")
        exit(0)
    else:
        print(
            f"Script will attempt to update {len(incidents_to_update)} incident to set:\n"
            f"{f'Status to {status}' if status is not None else ''}\n"
            f"{f'Severity to {severity}' if severity is not None else ''}"
        )

    # Update data
    update_data = {
        **({STATUS: status} if status else {}),
        **({SEVERITY: severity} if severity else {}),
    }

    # Run bulk update
    for incident_id in incidents_to_update:
        update_results = client.incidents.update(
            incident_id=incident_id, update_data=update_data
        )
        status_code = update_results.response.status_code
        if status_code >= 300:
            raise UnexpectedResponseError(f"Unexpected status code {status_code}.")

        print(
            f"Update for incident_id={incident_id} {'succeeded' if update_results.data else 'failed'}."
        )


if __name__ == "__main__":
    cli()
