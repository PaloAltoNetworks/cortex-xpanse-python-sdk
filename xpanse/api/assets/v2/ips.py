from typing import Any

from xpanse.const import V2_PREFIX
from xpanse.endpoint import ExEndpoint
from xpanse.iterator import ExResultIterator


class IpsEndpoint(ExEndpoint):
    """
    Part of the Assets v2 API for handling Recent IPs.
    See: https://api.expander.expanse.co/api/v1/docs/
    """

    def list(self, **kwargs: Any) -> ExResultIterator:
        """
        Returns the list of Recent IPs. Arguments should be passed as keyword args using
        the names below.

        Args:
            assetKey (str, optional):
                Filter by asset key.
            assetType (str, optional):
                Filter by asset type.
            inetSearch (str, optional):
                Filter by IP, IP range, IP CIDR or IP wildcard.
            providerId (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
            providerName (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
            businessUnitId (str, optional):
                Comma-separated string; Returns only results whose Business Unit's ID falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
            minLastObservedDate (str, optional):
                Filter by last observed timestamp. Date formatted string (YYYY-MM-DD).
            hostingEnvironment (str, optional):
                Filter by Hosting Environment. Allowed values are `ON_PREM`, `CLOUD`, `NONE`, `RESERVED_IPS`.
            sort (str, optional):
                Comma-separated string; orders results by the given fields. If the field name is
                prefixed by a -, then the ordering will be descending for that field.
            limit (int, optional):
                Returns at most this many results in a single api call.
            pageToken (str, optional):
                Returns results starting at this Page Token.

        Returns:
            :obj:`ExResultIterator`:
                An iterator containing all of the ip results. Results can be iterated
                or called by page using `<iterator>.next()`.

        Examples:
            >>> # Return all ips and print each resource:
            >>> for ips in client.assets.ips.v2.list():
            ...     for resource in ips:
            ...         print(resource)
        """
        return ExResultIterator(self._api, f"{V2_PREFIX}/assets/ips", kwargs)

    def csv(self, file: str, **kwargs: Any) -> bool:
        """
        Download a CSV file of asset IPs. This endpoint contains the IP addresses that your organization’s domains
        resolve to and certificates are advertised on. For on-premise IP ranges attributed to your organization,
        please use the `IpRangeEndpoint.list()` method (defaults 30 days).

        Downloads filtered ips as a csv file. Arguments should be passed as keyword args using
        the names below.

        Args:
            file (str):
                A relative path for saving the downloaded csv file.
            assetKey (str, optional):
                Filter by asset key.
            assetType (str, optional):
                Filter by asset type.
            providerId (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
            providerName (str, optional):
                Comma-separated string; Returns only results that were found on the given providers.
                If not set, results will include anything regardless of provider status.
            businessUnitId (str, optional):
                Comma-separated string; Returns only results whose Business Unit's ID falls in the provided list.
                NOTE: If omitted, API will return results for all Business Units the user has permissions to view.
            minLastObservedDate (str, optional):
                Filter by last observed timestamp. Date formatted string (YYYY-MM-DD).
            hostingEnvironment (str, optional):
                Filter by Hosting Environment. Allowed values are `ON_PREM`, `CLOUD`, `NONE`, `RESERVED_IPS`.

        Returns:
            :obj:`boolean`:
                `True` if the download was successful, otherwise `False`.

        Examples:
            >>> # Download a csv named `cloud-ips.csv` for all ips hosted in the cloud.
            >>> client.assets.ips.v2.csv(file="cloud-ips.csv", hostingEnvironment="CLOUD")
        """
        return self._api.csv(path=f"{V2_PREFIX}/assets/ips/csv", file_=file, **kwargs)
