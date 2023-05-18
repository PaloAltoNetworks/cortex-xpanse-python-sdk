from xpanse.api.incident_management.v1.incidents import IncidentsEndpoint
from xpanse.api.incident_management.v2.alerts import AlertsEndpoint


class IncidentsApi(IncidentsEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v1"

    @property
    def v1(self):
        return IncidentsEndpoint(self._api)


class AlertsApi(AlertsEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v2"

    @property
    def v2(self):
        return AlertsEndpoint(self._api)
