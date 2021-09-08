from xpanse.base_api import ExApi
from xpanse.api.services.v1.classifications import ClassificationsEndpoint
from xpanse.api.services.v1.country_codes import CountryCodesEndpoint
from xpanse.api.services.v1.services import ServicesEndpoint


class ClassificationsAPI(ExApi, ClassificationsEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v1"

    @property
    def v1(self):
        return ClassificationsEndpoint(self._api)


class CountryCodesAPI(ExApi, CountryCodesEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v1"

    @property
    def v1(self):
        return CountryCodesEndpoint(self._api)


class ServicesAPI(ExApi, ServicesEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v1"

    @property
    def v1(self):
        return ServicesEndpoint(self._api)


class ServicesApi(ExApi):
    @property
    def classifications(self):
        return ClassificationsAPI(self._api)

    @property
    def country_codes(self):
        return CountryCodesAPI(self._api)

    @property
    def services(self):
        return ServicesAPI(self._api)
