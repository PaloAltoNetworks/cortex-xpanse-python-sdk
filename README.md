Cortex Xpanse Python SDK
========================
<p align="center">
    <a href="https://expanse.co/">
        <img src="https://github.com/PaloAltoNetworks/cortex-xpanse-python-sdk/blob/main/docs/_source/_static/xpanse_banner.png?raw=true"/>
    </a>
</p>

<p align="center">
    <a href="https://github.com/psf/black">
        <img src="https://img.shields.io/badge/code%20style-black-000000.svg"/>
    </a>
    <a href="https://pypi.python.org/pypi/xpanse">
        <img src="https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blueviolet"/>
    </a>
    <a href="https://github.com/PaloAltoNetworks/cortex-xpanse-python-sdk/blob/main/LICENSE">
        <img src="https://img.shields.io/pypi/l/xpanse"/>
    </a>
    <a href="https://github.com/PaloAltoNetworks/cortex-xpanse-python-sdk/graphs/contributors">
        <img src="https://img.shields.io/github/contributors/PaloAltoNetworks/cortex-xpanse-python-sdk"/>
    </a>
</p>

Overview
--------

This library is intended to be an interface to the
<a href="https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference">Cortex Xpanse Public API</a>.

Install
-------
```python
pip install xpanse
```

Requirements
------------

`Python 3.7+`

Usage
-----
<a href="https://cortex-xpanse-python-sdk.readthedocs.io/en/latest/">Cortex Xpanse Public API Documentation</a>

```python
# Import client
from xpanse.client import XpanseClient

# Initialize client
client = XpanseClient()

# Get assets iterator object and dump to a list
assets = client.assets.list().dump()
```

You can view more example code in the <a href="https://github.com/PaloAltoNetworks/cortex-xpanse-python-sdk/tree/main/examples">examples</a> directory.

Configuration
-------------
A valid `API Key`, `API Key ID`, and `Fully Qualified Domain Name (FQDN)` are required for use.

Reference the docs for more information with <a href="https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-API-Reference/Get-Started-with-APIs">Getting Started</a>.

#### RECOMMENDED
***********
You can supply them as environment variables.

```shell script
export CORTEX_FQDN=<Your Xpanse Instance URL>
export CORTEX_API_KEY=<API Key>
export CORTEX_API_KEY_ID=<API Key ID>
```
    
#### NOT RECOMMENDED
***************
The following parameters can be set inline using the `XpanseClient` constructor.

_This is not recommended, as it easily exposes sensitive credentials in your source code._ 

```python
# Import client
from xpanse.client import XpanseClient

# Initialize client - THIS IS NOT RECOMMENDED, SET ENVIRONMENT VARIABLES INSTEAD
client = XpanseClient(url="https://my-company.crtx.us.paloaltonetworks.com",
                      api_key="xxxxxxxxxxxxxxxApiKeyxxxxxxxxxxxxxxx",
                      api_key_id=1)
```

Logging
-------
Logging is handled through the python logging package. To enable different levels of verbosity in your scripts you can do the following:

```python
import logging

# Set the logging level
logging.basicConfig(level=logging.DEBUG)
```

You can read more at <https://docs.python.org/3/library/logging.html>.
