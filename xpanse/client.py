import hashlib
import logging
import os
import platform
import secrets
import string
import sys
from datetime import datetime, timezone
from typing import Any, List, Optional, Union, MutableMapping
from urllib.parse import urlparse

import requests
from requests.exceptions import ConnectionError
from urllib3.exceptions import NewConnectionError

from . import __version__
from xpanse.const import (
    HTTPVerb,
    CORTEX_FQDN,
    CORTEX_API_KEY,
    CORTEX_API_KEY_ID,
)
from xpanse.error import (
    XpanseException,
    InvalidApiCredentials,
)

from xpanse.utils import normalize_param_names
from xpanse.api.asset_management import ServicesApi, OwnedIpRangesApi, AssetsApi
from xpanse.api.attack_surface_rules import AttackSurfaceRulesApi
from xpanse.api.incident_management import AlertsApi, IncidentsApi
from xpanse.api.tags import TagsApi


class XpanseClient:
    """
    Interface for Cortex Xpanse APIs.

    Args:
        url (str, required):
            The base URL that the paths will be appended onto. This field is required to be set either during
            instantiation, or using the environment variable `CORTEX_FQDN`.
        api_key_id (Union[str, int], required):
            The API Key ID associated with the generated credentials. This can be located after generating
            the credentials in the API Keys table under the 'ID' column. i.e. 1, 2, 3, etc. This field is required
            to be set either during instantiation, or using the environment variable `CORTEX_API_KEY_ID`.
        api_key (str, required):
            The API Key generated when provisioning the credentials in your product. It is recommended that
            the API Key defaults are kept (i.e. using Advanced keys). This field is required to be set either during
            instantiation, or using the environment variable `CORTEX_API_KEY`.
        use_advanced_auth (bool, optional):
            A flag used to determine which type of API Key is being used. 'Advanced' is used when True,
            'Standard' is used when False. This is configured when generating your API Keys is in the product.
            The default is True.
            See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-Started-with-APIs
        custom_ua (str, optional):
            A custom string can be provided that will be sent within the user-agent header on all
            requests to Xpanse. Final format will be `Xpanse SDK+<custom_ua>/__version__ ...`
        proxies (MutableMapping[str, str], optional):
            A dictionary detailing what proxy should be used for what transport protocol.
            This value will be passed to the session object after it has been either attached or
            created. For details on the structure of this dictionary, consult the
            :requests:`proxies <user/advanced/#proxies>` section of the Requests documentation.
        verify (bool, optional):
            Whether or not SSL verification should occur. This is `True` by default. Disabling certificate
            verification is strongly discouraged.
            See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings InsecureRequestWarning
    """

    """Xpanse URL - Default is set by the CORTEX_FQDN_URL environment variable"""
    _url: str

    """Public API Key ID"""
    _api_key_id: str

    """Public API Key"""
    _api_key: str

    """Uses a nonce and timestamp when true.
       See: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-Started-with-APIs
    """
    _use_advanced_auth: bool = True

    """Proxies"""
    _proxies: Optional[MutableMapping[str, str]] = None

    """Verify SSL"""
    _verify = True

    """Max Retry Count"""
    _max_retries: int = 1

    """Error Codes to Retry"""
    _retry_error_codes: List[int] = [503]

    """Vendor Name for UA"""
    _vendor: str = "Xpanse"

    """Product Name for UA"""
    _product: str = "Xpanse SDK"

    """Xpanse SDK Build # for UA"""
    _build: str = "unknown"

    """Python version for UA"""
    _python_version: str = "unknown"

    """OS for UA"""
    _os: str = "unknown"

    """Active Session"""
    _session: requests.Session = requests.Session()

    """Class Methods"""

    def __init__(
        self,
        url: Optional[str] = None,
        api_key_id: Optional[Union[str, int]] = None,
        api_key: Optional[str] = None,
        use_advanced_auth: bool = True,
        custom_ua: Optional[str] = None,
        proxies: Optional[MutableMapping[str, str]] = None,
        verify: bool = True,
    ):
        # Format logger
        self._log = logging.getLogger(
            "{}.{}".format(self.__module__, self.__class__.__name__)
        )

        # Get install details
        self._set_os()
        self._set_current_python_version()

        # If a custom UA product is desired, include that
        if custom_ua is not None:
            self._product += f"+{custom_ua}"

        # Configure URL
        env_url = os.getenv(CORTEX_FQDN)
        if url is not None:
            self._url = url
        elif env_url is not None:
            self._url = env_url
        else:
            raise ValueError(
                "A 'url' must be provided. Set the 'url' client parameter or set the 'CORTEX_FQDN' "
                "environment variable."
            )

        if not self._url.startswith("http"):
            self._url = f"https://{self._url}"

        host = urlparse(self._url).netloc
        if host.startswith("api-"):
            self._url = f"https://{host}"
        else:
            self._url = f"https://api-{host}"

        # Configure Auth Session
        self._proxies = proxies

        if isinstance(verify, bool):
            self._verify = verify

        if isinstance(use_advanced_auth, bool):
            self._use_advanced_auth = use_advanced_auth
        if not self._use_advanced_auth:
            self._log.warning(
                "'Advanced Authentication' is disabled, your requests may be vulnerable to replay attacks. "
                "See https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-Started-with-APIs "
                "for more information."
            )

        self._setup_auth(api_key=api_key, api_key_id=api_key_id)

    def _setup_auth(
        self, api_key: Optional[str], api_key_id: Optional[Union[str, int]]
    ):
        """
        Check for a valid set of authentication inputs. This can be one of the following (in order of priority):
            1. Setting api_key_id and api_key from the XpanseClient constructor
            2. Setting the CORTEX_API_KEY_ID and CORTEX_API_KEY environment variables

        Args:
            api_key (str, Optional):
                The api_key provided from the constructor
            api_key_id (str, Optional):
                The api_key_id provided from the constructor
        """
        if api_key is not None:
            self._api_key = api_key
        elif os.getenv(CORTEX_API_KEY) is not None:
            self._api_key = str(os.getenv(CORTEX_API_KEY))
        else:
            raise ValueError(
                "An 'api_key' must be provided. Set the 'api_key' parameter or set the 'CORTEX_API_KEY' "
                "environment variable."
            )

        if api_key_id is not None:
            self._api_key_id = str(api_key_id)
        elif os.getenv(CORTEX_API_KEY_ID) is not None:
            self._api_key_id = str(os.getenv(CORTEX_API_KEY_ID))
        else:
            raise ValueError(
                "An 'api_key_id' must be provided. Set the 'api_key_id' parameter or set the "
                "'CORTEX_API_KEY_ID' environment variable."
            )

        self._create_session()

        if not self._validate_auth():
            key_type = "Advanced" if self._use_advanced_auth else "Standard"
            raise InvalidApiCredentials(
                "Failed to authenticate with the provided 'api_key' and 'api_key_id' using "
                f"'{key_type}' authentication."
            )

    def _validate_auth(self) -> bool:
        """
        Validates the provided API Keys

        Returns:
            :bool: True when the keys are valid, False when the keys are invalid or expired.
        """
        res = self.post("api_keys/validate/")

        if res is None or res.status_code == 401:
            return False

        return res.json()

    def _get_auth_headers(self) -> dict:
        """
        Generates authorization headers for both Standard and Advanced API Keys

        Returns:
            :dict: Authorization headers
        """
        if self._use_advanced_auth:
            # Generate a 64 bytes random string
            nonce = "".join(
                [
                    secrets.choice(string.ascii_letters + string.digits)
                    for _ in range(64)
                ]
            )
            # Get the current timestamp as milliseconds.
            timestamp = int(datetime.now(timezone.utc).timestamp()) * 1000
            # Generate the auth key
            auth_key = "%s%s%s" % (self._api_key, nonce, timestamp)
            # Convert to bytes object
            auth_key_bytes = auth_key.encode("utf-8")
            # Calculate sha256:
            api_key_hash = hashlib.sha256(auth_key_bytes).hexdigest()
            return {
                "x-xdr-timestamp": str(timestamp),
                "x-xdr-nonce": nonce,
                "x-xdr-auth-id": str(self._api_key_id),
                "Authorization": api_key_hash,
            }
        else:
            return {
                "x-xdr-auth-id": str(self._api_key_id),
                "Authorization": self._api_key,
            }

    def _refresh_auth(self):
        """
        Refresh auth in session.
        """
        self._session.headers.pop("x-xdr-timestamp", None)
        self._session.headers.pop("x-xdr-nonce", None)
        self._session.headers.update(self._get_auth_headers())

    def _create_session(self):
        """
        Creates a request session with auth.
        """
        self._session = requests.Session()

        if self._proxies is not None:
            self._session.proxies.update(self._proxies)

        self._session.verify = self._verify

        self._session.headers.update(self._get_auth_headers())

    def _set_current_python_version(self):
        """
        Get current installed python version.
        """
        self._python_version = ".".join([str(i) for i in sys.version_info][0:3])

    def _set_os(self):
        """
        GET OS version.
        """
        self._os = f"{platform.version()}"

    def _generate_user_agent(self):
        """
        Generate UA String.
        """
        return f"{self._product}/{__version__} ({self._os}) Python/{self._python_version} {self._vendor}"

    def _request(
        self, method: str, path: str, **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Request builder.
        """
        retries = 0
        while retries <= self._max_retries:
            try:
                if self._use_advanced_auth:
                    self._refresh_auth()

                kwargs = normalize_param_names(kwargs)
                self._log.debug(
                    f"REQUEST TO: {method} {self._url}/{path} WITH PAYLOAD: {kwargs}"
                )
                resp = self._session.request(method, f"{self._url}/{path}", **kwargs)
                if resp.status_code < 400:
                    return resp
                else:
                    if resp.status_code in self._retry_error_codes:
                        retries += 1
                        continue
                    else:
                        self._log.error(f"Error response: {resp.text}")
                        return resp
            except (
                ConnectionError,
                NewConnectionError,
            ) as err:
                self._log.error(err)
                retries += 1
                continue
            except XpanseException as err:
                self._log.error(err)
                break
        return None

    def get(self, path: str, **kwargs: Any) -> Optional[requests.Response]:
        """
        Initiates an HTTP GET request using the specified path.  Refer to
        :obj:`requests.request` for more detailed information on what
        keyword arguments can be passed:

        Args:
            path (str):
                The path to be appended onto the base URL for the request.
            **kwargs (dict):
                Keyword arguments to be passed to the Requests Sessions request
                method.

        Returns:
            :obj:`requests.Response`
        """
        return self._request(HTTPVerb.HTTP_GET.value, path, **kwargs)

    def post(self, path: str, **kwargs: Any) -> Optional[requests.Response]:
        """
        Initiates an HTTP POST request using the specified path.  Refer to
        :obj:`requests.request` for more detailed information on what
        keyword arguments can be passed:

        Args:
            path (str):
                The path to be appended onto the base URL for the request.
            **kwargs (dict):
                Keyword arguments to be passed to the Requests Sessions request
                method.

        Returns:
            :obj:`requests.Response`
        """
        return self._request(HTTPVerb.HTTP_POST.value, path, **kwargs)

    def patch(self, path: str, **kwargs: Any) -> Optional[requests.Response]:
        """
        Initiates an HTTP PATCH request using the specified path.  Refer to
        :obj:`requests.request` for more detailed information on what
        keyword arguments can be passed:

        Args:
            path (str):
                The path to be appended onto the base URL for the request.
            **kwargs (dict):
                Keyword arguments to be passed to the Requests Sessions request
                method.

        Returns:
            :obj:`requests.Response`
        """
        return self._request(HTTPVerb.HTTP_PATCH.value, path, **kwargs)

    def put(self, path: str, **kwargs: Any) -> Optional[requests.Response]:
        """
        Initiates an HTTP PUT request using the specified path.  Refer to
        :obj:`requests.request` for more detailed information on what
        keyword arguments can be passed:

        Args:
            path (str):
                The path to be appended onto the base URL for the request.
            **kwargs (dict):
                Keyword arguments to be passed to the Requests Sessions request
                method.

        Returns:
            :obj:`requests.Response`
        """
        return self._request(HTTPVerb.HTTP_PUT.value, path, **kwargs)

    def delete(self, path: str) -> Optional[requests.Response]:
        """
        Initiates an HTTP DELETE request using the specified path.  Refer to
        :obj:`requests.request` for more detailed information on what
        keyword arguments can be passed:

        Args:
            path (str):
                The path to be appended onto the base URL for the request.
            **kwargs (dict):
                Keyword arguments to be passed to the Requests Sessions request
                method.

        Returns:
            :obj:`requests.Response`

        """
        return self._request(HTTPVerb.HTTP_DELETE.value, path)

    ############################################
    # API Definitions
    ###########################################

    @property
    def assets(self):
        """Assets API"""
        return AssetsApi(self)

    @property
    def owned_ip_ranges(self):
        """Owned IP Ranges API"""
        return OwnedIpRangesApi(self)

    @property
    def services(self):
        """Services API"""
        return ServicesApi(self)

    @property
    def attack_surface_rules(self):
        """Attack Surface Rules API"""
        return AttackSurfaceRulesApi(self)

    @property
    def incidents(self):
        """Incidents API"""
        return IncidentsApi(self)

    @property
    def alerts(self):
        """Alerts V2 API"""
        return AlertsApi(self)

    @property
    def tags(self):
        """Tags API"""
        return TagsApi(self)
