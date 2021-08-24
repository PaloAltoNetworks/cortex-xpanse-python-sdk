from xpanse.base_api import ExApi
from xpanse.api.entities.v1.entities import EntitiesEndpoint


class EntitiesInnerApi(ExApi, EntitiesEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v1"

    @property
    def v1(self):
        return EntitiesEndpoint(self._api)


class EntitiesApi(ExApi):
    @property
    def entities(self):
        return EntitiesInnerApi(self._api)
