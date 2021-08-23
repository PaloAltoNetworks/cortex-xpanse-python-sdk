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


    pip install xpanse-<version>.tar.gz


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

A valid Bearer token or JWT is required for use. Bearer tokens are suggested as JWTs have a limited lifespan. 

**RECOMMENDED**
or you can supply them as environment variables using the variable names ``XPANSE_BEARER_TOKEN`` and/or ``XPANSE_JWT_TOKEN``.

**NOT RECOMMENDED**
You can either provided these keys directly at client initialization by doing

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