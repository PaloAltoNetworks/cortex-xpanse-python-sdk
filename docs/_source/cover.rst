Xpanse Python SDK
==================
.. image:: _static/xpanse_banner.png
   :width: 600
   :target: https://expanse.co/

Overview
--------

This library is intended to be an interface to the `Xpanse Expander API <https://knowledgebase.expanse.co/expander-apis/>`_.

Install
-------
.. code-block:: python


    pip install xpanse


Requirements
------------

Python 3.7+

Usage
-----

.. code-block:: python

    # Import client
    from xpanse.client import ExClient

    # initialize client
    client = ExClient()

    # get ip_range iterator object and dump to a list
    ranges = client.assets.ip_range.list().dump()

You can view more example code in the examples directory.

Configuration
-------------

A valid Client ID and Secret is required for use. This is recommended over using a JWT, as they have limited lifespans.
While a bearer token is supported in this version, this auth flow is being deprecated. Therefore, it is highly recommended to use Client Credentials.

**RECOMMENDED**
You can supply them as environment variables using the variable names ``XPANSE_CLIENT_ID`` AND ``XPANSE_CLIENT_SECRET``.

.. code-block:: python

    export XPANSE_CLIENT_ID=<Client ID>
    export XPANSE_CLIENT_SECRET=<Client Secret>

**NOT RECOMMENDED**
To use a short lived JWT, you can supply the JWT as an environmental variable using the name ``XPANSE_JWT_TOKEN``

.. code-block:: python

    export XPANSE_JWT_TOKEN=<JWT>

[Deprecated]
A valid Bearer token can be supplied as an environment variable

To supply a valid bearer token as an environment variable, you can use the variable names ``XPANSE_BEARER_TOKEN``.

.. code-block:: python

    export XPANSE_BEARER_TOKEN=<Bearer Token>

Logging
-------
Logging is handled through the python logging package. To enable different levels of verbosity in your scripts you can do the following:

.. code-block:: python

    import logging
    logging.basicConfig(level=logging.DEBUG)

You can read more at `<https://docs.python.org/3/library/logging.html>`_.