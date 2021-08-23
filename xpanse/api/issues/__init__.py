from xpanse.base_api import ExApi
from xpanse.api.issues.v1.assignees import AssigneesEndpoint
from xpanse.api.issues.v1.business_units import BusinessUnitsEndpoint
from xpanse.api.issues.v1.issues import IssuesEndpoint
from xpanse.api.issues.v1.issue_types import IssueTypesEndpoint
from xpanse.api.issues.v1.policies import PoliciesEndpoint
from xpanse.api.issues.v1.providers import ProvidersEndpoint
from xpanse.api.issues.v1.updates import UpdatesEndpoint


class IssuesAssigneesAPI(ExApi, AssigneesEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v1"

    @property
    def v1(self):
        return AssigneesEndpoint(self._api)


class IssuesBusinessUnitsAPI(ExApi, BusinessUnitsEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v1"

    @property
    def v1(self):
        return BusinessUnitsEndpoint(self._api)


class IssuesIssuesAPI(ExApi, IssuesEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v1"

    @property
    def v1(self):
        return IssuesEndpoint(self._api)


class IssuesIssueTypesAPI(ExApi, IssueTypesEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v1"

    @property
    def v1(self):
        return IssueTypesEndpoint(self._api)


class IssuesPoliciesAPI(ExApi, PoliciesEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v1"

    @property
    def v1(self):
        return PoliciesEndpoint(self._api)


class IssuesProvidersAPI(ExApi, ProvidersEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v1"

    @property
    def v1(self):
        return ProvidersEndpoint(self._api)


class IssuesUpdatesAPI(ExApi, UpdatesEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v1"

    @property
    def v1(self):
        return UpdatesEndpoint(self._api)


class IssuesApi(ExApi):
    @property
    def assignees(self):
        return IssuesAssigneesAPI(self._api)

    @property
    def business_units(self):
        return IssuesBusinessUnitsAPI(self._api)

    @property
    def issues(self):
        return IssuesIssuesAPI(self._api)

    @property
    def issue_types(self):
        return IssuesIssueTypesAPI(self._api)

    @property
    def policies(self):
        return IssuesPoliciesAPI(self._api)

    @property
    def providers(self):
        return IssuesProvidersAPI(self._api)

    @property
    def updates(self):
        return IssuesUpdatesAPI(self._api)
