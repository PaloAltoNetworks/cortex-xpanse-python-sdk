import logging
import os
import platform
from typing import Any, List, MutableMapping, Optional
import sys

import requests
from requests.exceptions import ConnectionError
from urllib3.exceptions import NewConnectionError

from . import __version__
from xpanse.const import (
    XPANSE_BEARER_TOKEN,
    XPANSE_JWT_TOKEN,
    HTTPVerb,
    ID_TOKEN_URL,
)
from xpanse.error import (
    UnexpectedValueError,
    JWTExpiredError,
    XpanseException,
)
from xpanse.api.annotations import AnnotationsApi
from xpanse.api.assets import AssetsApi
from xpanse.api.behavior import BehaviorApi
from xpanse.api.entities import EntitiesApi
from xpanse.api.issues import IssuesApi
from xpanse.api.services import ServicesApi
from xpanse.api.targeted_ips import TargetedIPsApi
from xpanse.api.connectors import ConnectorsApi
from xpanse.utils import normalize_param_names


class ExClient:
    """
    Interface for Xpanse APIs.

    Args:
        url (str, optional):
            The base URL that the paths will be appended onto.  The default
            is ``https://api.expander.expanse.co``
        bearer_token (str, optional):
            The Bearer token for the Xpanse API, which is used to request emphemeral JWT tokens.
            More details at ``https://knowledgebase.expanse.co/expander-apis/#getting``
        jwt (str, optional):
            The JWT for the Xpanse API. Note JWTs are temporary so they are not intended for use
            with long-running applications.
            More details at ``https://knowledgebase.expanse.co/expander-apis/#getting``
        custom_ua (str, optional):
            A custom string can be provided that will be sent within the user-agent header on all
            requests to Xpanse. Final format will be `Xpanse SDK+<custom_ua>/__version__ ...`
        proxies (dict, optional):
            A dictionary detailing what proxy should be used for what transport protocol.
            This value will be passed to the session object after it has been either attached or
            created. For details on the structure of this dictionary, consult the
            :requests:`proxies <user/advanced/#proxies>` section of the Requests documentation.
        verify (bool, optional):
            Whether or not SSL verification should occur. This is `True` by default. Disabling certificate
            verification is strongly discouraged.
            See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings InsecureRequestWarning
    """

    """Xpanse URL"""
    _url: str = "https://api.expander.expanse.co"

    """Bearer Token"""
    _bt: Optional[str] = None

    """JWT"""
    _jwt: Optional[str] = None

    """Proxies"""
    _proxies: Optional[str] = None

    """Verify SSL"""
    _verify = True

    """JWT is valid"""
    _jwt_valid: bool = False

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
        url=None,
        bearer_token=None,
        jwt=None,
        custom_ua=None,
        proxies=None,
        verify=True,
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

        # Configure URL and Auth tokens
        if url is not None:
            self._url = url

        if bearer_token is not None:
            self._bt = bearer_token
        else:
            self._bt = os.environ.get(XPANSE_BEARER_TOKEN, None)

        if proxies is not None:
            self._proxies = proxies

        if isinstance(verify, bool):
            self._verify = verify

        if jwt is not None:
            self._jwt = jwt
            self._jwt_valid = True
        else:
            env_jwt = os.environ.get(XPANSE_JWT_TOKEN, None)
            if env_jwt is not None:
                self._jwt = env_jwt
                self._jwt_valid = True
            else:
                self._refresh_jwt()

        if not self._bt and not self._jwt_valid:
            raise UnexpectedValueError(
                "A valid Xpanse Bearer token or JWT token is required."
            )

        # create Session
        self._create_session()

    def _refresh_jwt(self, is_retry: bool = False):
        """
        Refreshes JWT using Bearer token.
        """
        try:
            if self._bt is not None:
                resp = requests.get(
                    f"{self._url}/{ID_TOKEN_URL}",
                    headers={
                        "Authorization": f"Bearer {self._bt}",
                        "Content-Type": "application/json",
                    },
                    timeout=30,
                    proxies=self._proxies,
                    verify=self._verify,
                ).json()
                if "error" in resp or "token" not in resp:
                    raise UnexpectedValueError(
                        f"API returned an error while refreshing JWT: {resp['error']}"
                    )
                else:
                    self._jwt_valid = True
                    self._jwt = resp["token"]
            else:
                raise UnexpectedValueError(
                    "A valid Xpanse Bearer token or JWT token is required."
                )
        except ConnectionError as request_exception:
            if is_retry:
                raise UnexpectedValueError(
                    "Request returned an exception"
                ) from request_exception
            logging.warn(f"ConnectionError encountered during JWT refresh, will retry.")
            self._refresh_jwt(is_retry=True)
        except requests.RequestException as request_exception:
            raise UnexpectedValueError(
                "Request returned an exception"
            ) from request_exception

    def _create_session(self, session: Optional[Any] = None):
        """
        Add JWT auth to session.
        """
        if session is not None:
            self._session = session
        self._session = requests.Session()
        self._session.headers.update(
            {
                "User-Agent": self._generate_user_agent(),
                "Content-Type": "application/json",
                "Authorization": f"JWT {self._jwt}",
            }
        )

        if self._proxies is not None:
            self._session.proxies.update(self._proxies)  # type: ignore

        self._session.verify = self._verify

    def _refresh_session(self):
        """
        Refresh JWT auth if the old token expires.
        """
        if not self._bt:
            raise UnexpectedValueError("No valid Xpanse Bearer token was found.")
        self._refresh_jwt()
        self._session.headers.update({"Authorization": f"JWT {self._jwt}"})

    def _check_response_for_invalid_session(self, resp: requests.Response) -> bool:
        """
        Check response for expired JWT.
        """
        if resp.status_code == 401:
            try:
                resp_json = resp.json()
                if (
                    "detail" in resp_json
                    and resp_json["detail"] == "Signature has expired."
                ):
                    return True
            except ValueError:
                # Some 401 responses are returned without a body
                pass
        return False

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
                kwargs = normalize_param_names(kwargs)
                self._log.debug(
                    f"REQUEST TO: {method} {self._url}/{path} WITH PAYLOAD: {kwargs}"
                )
                resp = self._session.request(method, f"{self._url}/{path}", **kwargs)
                if resp.status_code < 400:
                    return resp
                else:
                    if self._check_response_for_invalid_session(resp):
                        # JWT has expired, try to generare a new one if a bearer token exists
                        # and retry the request without incrementing our retry counter.
                        if self._bt is not None:
                            self._refresh_session()
                            continue
                        else:
                            raise JWTExpiredError("JWT has expired", resp)
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

    def direct_get(self, url: str, **kwargs: Any) -> Optional[requests.Response]:
        """
        Fetches direct without url formatting.
        """
        resp = self._session.request(HTTPVerb.HTTP_GET.value, url, **kwargs)
        return resp

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

    def csv(self, path: str, file_: str, **kwargs: Any) -> bool:
        """
        Initiates an HTTP GET request using the specified path with special handling
        for downloading a csv file. Refer to :obj:`requests.request` for more detailed
        information on what keyword arguments can be passed:

        Args:
            path (str):
                The path to be appended onto the base URL for the request.
            file_ (str):
                The file name with path where the resulting csv file should be saved.
            **kwargs (dict):
                Keyword arguments to be passed to the Requests Sessions request
                method.

        Returns:
            :obj:`boolean`:
                `True` if the download was successful, otherwise `False`.
        """
        try:
            with requests.Session() as s:
                s.headers.update(
                    {
                        "User-Agent": self._generate_user_agent(),
                        "Accept": "text/csv",
                        "Authorization": f"JWT {self._jwt}",
                    }
                )
                resp = s.get(f"{self._url}/{path}", params=kwargs, stream=True)
                if resp.status_code < 400:
                    with open(file_, "wb") as f:
                        for chunk in resp.iter_content(1024 * 1024):
                            f.write(chunk)
                            self._log.debug(f"Writing {path} output to {file_}")
                    return True
                else:
                    self._log.error(f"Error response: {resp.text}")
                    return False
        except requests.exceptions.RequestException:
            self._log.exception(f"Error response")
            return False

    ############################################
    # API Definitions
    ###########################################

    @property
    def annotations(self):
        """Annotations API"""
        return AnnotationsApi(self)

    @property
    def assets(self):
        """Assets API"""
        return AssetsApi(self)

    @property
    def behavior(self):
        """Behavior API"""
        return BehaviorApi(self)

    @property
    def entities(self):
        """Entities API"""
        return EntitiesApi(self)

    @property
    def issues(self):
        """Issues API"""
        return IssuesApi(self)

    @property
    def services(self):
        """Services API"""
        return ServicesApi(self)

    @property
    def targeted_ips(self):
        """Targeted IPs API"""
        return TargetedIPsApi(self)

    @property
    def connectors(self):
        """Connectors API"""
        return ConnectorsApi(self)
