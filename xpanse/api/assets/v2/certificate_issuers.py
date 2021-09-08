from typing import Any

from xpanse.const import V2_PREFIX
from xpanse.endpoint import ExEndpoint
from xpanse.iterator import ExResultIterator


class CertificateIssuersEndpoint(ExEndpoint):
    """
    Part of the Assets v2 API for handling Asset Certificate Issuers.
    See: https://api.expander.expanse.co/api/v1/docs/
    """

    def list(self, **kwargs: Any) -> ExResultIterator:
        """
        Returns the list of Certificate Issuers. Arguments should be passed as keyword args using
        the names below.

        Args:
            limit (int, optional):
                Returns at most this many results in a single api call.
                Default is 100, max is 10000.
            pageToken (str, optional):
                Returns results starting at this Page Token.
        Returns:
            :obj:`ExResultIterator`:
                An iterator containing all of the certificate issuers results. Results can be iterated
                or called by page using `<iterator>.next()`.
        Examples:
            >>> # Return all certificate issuers and print each one:
            >>> for props in client.assets.certificate_issuers.v2.list():
            ...     for prop in props:
            ...         print(prop)
        """
        return ExResultIterator(
            self._api, f"{V2_PREFIX}/assets/certificate-issuers", kwargs
        )
