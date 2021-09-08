from xpanse.base_api import ExApi
from xpanse.api.targeted_ips.v1.targeted_ips import TargetedIPsEndpoint


class TargetedIPsInnerApi(ExApi, TargetedIPsEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v1"

    @property
    def v1(self):
        return TargetedIPsEndpoint(self._api)


class TargetedIPsApi(ExApi):
    @property
    def targeted_ips(self):
        return TargetedIPsInnerApi(self._api)
