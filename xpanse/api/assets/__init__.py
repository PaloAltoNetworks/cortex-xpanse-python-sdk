from xpanse.base_api import ExApi
from xpanse.api.assets.v2.account_integrations import AccountIntegrationsEndpoint
from xpanse.api.assets.v2.annotations import AnnotationsEndpoint
from xpanse.api.assets.v2.entities import AssetEntitiesEndpoint
from xpanse.api.assets.v2.certificates import CertificatesEndpoint
from xpanse.api.assets.v2.certificate_properties import CertificatePropertiesEndpoint
from xpanse.api.assets.v2.cloud_resources import CloudResourcesEndpoint
from xpanse.api.assets.v2.domains import DomainsEndpoint
from xpanse.api.assets.v2.ip_range import IpRangeEndpoint
from xpanse.api.assets.v2.ips import IpsEndpoint
from xpanse.api.assets.v2.providers import ProvidersEndpoint
from xpanse.api.assets.v2.regions import RegionsEndpoint
from xpanse.api.assets.v2.certificate_issuers import CertificateIssuersEndpoint
from xpanse.api.assets.v2.domain_registrars import DomainRegistrarsEndpoint


class AccountIntegrationsApi(ExApi, AccountIntegrationsEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v2"

    @property
    def v2(self):
        return AccountIntegrationsEndpoint(self._api)


class AnnotationsApi(ExApi, AnnotationsEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v2"

    @property
    def v2(self):
        return AnnotationsEndpoint(self._api)


class AssetEntitiesApi(ExApi, AssetEntitiesEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v2"

    @property
    def v2(self):
        return AssetEntitiesEndpoint(self._api)


class CertificatesApi(ExApi, CertificatesEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v2"

    @property
    def v2(self):
        return CertificatesEndpoint(self._api)


class CertificatePropertiesApi(ExApi, CertificatePropertiesEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v2"

    @property
    def v2(self):
        return CertificatePropertiesEndpoint(self._api)


class CloudResourcesApi(ExApi, CloudResourcesEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v2"

    @property
    def v2(self):
        return CloudResourcesEndpoint(self._api)


class DomainsApi(ExApi, DomainsEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v2"

    @property
    def v2(self):
        return DomainsEndpoint(self._api)


class IPRangeApi(ExApi, IpRangeEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v2"

    @property
    def v2(self):
        return IpRangeEndpoint(self._api)


class IpsApi(ExApi, IpsEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v2"

    @property
    def v2(self):
        return IpsEndpoint(self._api)


class ProvidersApi(ExApi, ProvidersEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v2"

    @property
    def v2(self):
        return ProvidersEndpoint(self._api)


class RegionsApi(ExApi, RegionsEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v2"

    @property
    def v2(self):
        return RegionsEndpoint(self._api)


class CertificateIssuersApi(ExApi, CertificateIssuersEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v2"

    @property
    def v2(self):
        return CertificateIssuersEndpoint(self._api)


class DomainRegistrarsApi(ExApi, DomainRegistrarsEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v2"

    @property
    def v2(self):
        return DomainRegistrarsEndpoint(self._api)


class AssetsApi(ExApi):
    @property
    def domain_registrars(self):
        return DomainRegistrarsApi(self._api)

    @property
    def certificate_issuers(self):
        return CertificateIssuersApi(self._api)

    @property
    def account_integrations(self):
        return AccountIntegrationsApi(self._api)

    @property
    def annotations(self):
        return AnnotationsApi(self._api)

    @property
    def certificates(self):
        return CertificatesApi(self._api)

    @property
    def certificate_properties(self):
        return CertificatePropertiesApi(self._api)

    @property
    def cloud_resources(self):
        return CloudResourcesApi(self._api)

    @property
    def domains(self):
        return DomainsApi(self._api)

    @property
    def entities(self):
        return AssetEntitiesApi(self._api)

    @property
    def ip_range(self):
        return IPRangeApi(self._api)

    @property
    def ips(self):
        return IpsApi(self._api)

    @property
    def providers(self):
        return ProvidersApi(self._api)

    @property
    def regions(self):
        return RegionsApi(self._api)
