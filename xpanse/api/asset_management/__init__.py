from xpanse.api.asset_management.v1.assets import AssetsEndpoint
from xpanse.api.asset_management.v1.external_ip_ranges import ExternalIpRangesEndpoint
from xpanse.api.asset_management.v1.services import ServicesEndpoint


class AssetsApi(AssetsEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v1"

    @property
    def v1(self):
        return AssetsEndpoint(self._api)


class ExternalIpRangesApi(ExternalIpRangesEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v1"

    @property
    def v1(self):
        return ExternalIpRangesEndpoint(self._api)


class ServicesApi(ServicesEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v1"

    @property
    def v1(self):
        return ServicesEndpoint(self._api)
