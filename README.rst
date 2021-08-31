Xpanse Python SDK
==================
.. image:: https://github.com/PaloAltoNetworks/cortex-xpanse-python-sdk/blob/main/docs/_source/_static/xpanse_banner.png?raw=true
   :width: 800
   :target: https://expanse.co/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

Overview
--------

This library is intended to be an interface to the `Xpanse Expander API <https://knowledgebase.xpanse.co/expander-apis/>`_.

Install
-------
.. code-block:: python

    pip install xpanse

Requirements
------------

Python 3.6+

Usage
-----
`Documentation <https://cortex-xpanse-python-sdk.readthedocs.io/en/latest/>`_
.. code-block:: python

    # Import client
    from xpanse.client import ExClient

    # initialize client
    client = ExClient()

    # get ip_range iterator object and dump to a list
    ranges = client.assets.ip_range.list().dump()

You can view more example code in the `examples <https://github.com/PaloAltoNetworks/cortex-xpanse-python-sdk/tree/main/examples>`_ directory.

Configuration
-------------

A valid Bearer token or JWT is required for use. Bearer tokens are suggested as JWTs have a limited lifespan. 

RECOMMENDED
***********
You can supply them as environment variables using the variable names ``XPANSE_BEARER_TOKEN`` and/or ``XPANSE_JWT_TOKEN``.

.. code-block:: python

    export XPANSE_BEARER_TOKEN=<Bearer Token>
    # or
    export XPANSE_JWT_TOKEN=<JWT>
    

NOT RECOMMENDED
***************
You can also provided these keys directly at client initialization by doing

.. code-block:: python

    client = ExClient(jwt=<JWT>)
    # or
    client = ExClient(bearer=<Bearer>) 

Logging
-------
Logging is handled through the python logging package. To enable different levels of verbosity in your scripts you can do the following:

.. code-block:: python

    import logging
    logging.basicConfig(level=logging.DEBUG)

You can read more at `<https://docs.python.org/3/library/logging.html>`_.
