Xpanse Python SDK
==================
<img alt="Xpanse" src="https://github.com/PaloAltoNetworks/cortex-xpanse-python-sdk/blob/main/docs/_source/_static/xpanse_banner.png?raw=true|width=400"/>

Overview
--------

This library is intended to be an interface to the Xpanse Expander API [Xpanse Expander API](https://knowledgebase.xpanse.co/expander-apis/>).

Install
-------

    pip install xpanse

Requirements
------------

Python 3.6+

Usage
-----
Documentation: https://cortex-xpanse-python-sdk.readthedocs.io/en/latest/

    # Import client
    from xpanse.client import ExClient

    # initialize client
    client = ExClient()

    # get ip_range iterator object and dump to a list
    ranges = client.assets.ip_range.list().dump()

You can view more example code in the [examples directory](https://github.com/PaloAltoNetworks/cortex-xpanse-python-sdk/tree/main/examples>).

Configuration
-------------

A valid Bearer token or JWT is required for use. Bearer tokens are suggested as JWTs have a limited lifespan. 

RECOMMENDED
***********
You can supply them as environment variables using the variable names ``XPANSE_BEARER_TOKEN`` and/or ``XPANSE_JWT_TOKEN``.

    export XPANSE_BEARER_TOKEN=<Bearer Token>
    # or
    export XPANSE_JWT_TOKEN=<JWT>
    

NOT RECOMMENDED
***************
You can also provided these keys directly at client initialization by doing

    client = ExClient(jwt=<JWT>)
    # or
    client = ExClient(bearer_token=<BearerToken>) 

Logging
-------
Logging is handled through the python logging package. To enable different levels of verbosity in your scripts you can do the following:

    import logging
    logging.basicConfig(level=logging.DEBUG)

You can read more at https://docs.python.org/3/library/logging.html.
