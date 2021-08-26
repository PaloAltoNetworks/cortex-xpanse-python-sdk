from xpanse.base_api import ExApi
from xpanse.api.connectors.v1.services import ConnectorsServicesEndpoint
from xpanse.api.connectors.v1.accounts import ConnectorsAccountsEndpoint


class ConnectorsServicesAPI(ExApi, ConnectorsServicesEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v1"

    @property
    def v1(self):
        return ConnectorsServicesEndpoint(self._api)


class ConnectorsAccountsAPI(ExApi, ConnectorsAccountsEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v1"

    @property
    def v1(self):
        return ConnectorsAccountsEndpoint(self._api)


class ConnectorsApi(ExApi):
    @property
    def services(self):
        return ConnectorsServicesAPI(self._api)

    @property
    def accounts(self):
        return ConnectorsAccountsAPI(self._api)
