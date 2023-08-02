
.. image:: https://img.shields.io/pypi/v/cdumay-rest-client.svg
   :target: https://pypi.python.org/pypi/cdumay-rest-client/
   :alt: Latest Version

.. image:: https://travis-ci.org/cdumay/cdumay-rest-client.svg?branch=master
   :target: https://travis-ci.org/cdumay/cdumay-rest-client
   :alt: Latest version

.. image:: https://readthedocs.org/projects/cdumay-rest-client/badge/?version=latest
   :target: http://cdumay-rest-client.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://img.shields.io/badge/license-BSD3-blue.svg
    :target: https://github.com/cdumay/cdumay-rest-client/blob/master/LICENSE

.. image:: https://github.com/cdumay/cdumay-rest-client/blob/reports/junit/tests-badge.svg?raw=true
   :target: https://htmlpreview.github.io/?https://github.com/cdumay/cdumay-rest-client/blob/reports/junit/report.html
   :alt: Tests

.. image:: https://github.com/cdumay/cdumay-rest-client/blob/reports/flake8/flake8-badge.svg?raw=true
   :target: https://htmlpreview.github.io/?https://github.com/cdumay/cdumay-rest-client/blob/reports/flake8/index.html
   :alt: Lint

.. image:: https://github.com/cdumay/cdumay-rest-client/blob/reports/coverage/coverage-badge.svg?raw=true
   :target: https://htmlpreview.github.io/?https://github.com/cdumay/cdumay-rest-client/blob/reports/coverage/html/index.html
   :alt: Coverage badge

cdumay-rest-client
==================

This library is a basic REST client with exception formatting.

Quickstart
----------

First, install cdumay-rest-client using 
`pip <https://pip.pypa.io/en/stable/>`_:

    $ pip install cdumay-rest-client

Next, add a `RESTClient` instance to your code:

.. code-block:: python

    import json, sys
    from cdumay_rest_client.client import RESTClient

    client = RESTClient(server="http://jsonplaceholder.typicode.com")
    json.dump(
        client.do_request(method="GET", path="/posts/1"),
        sys.stdout,
        sort_keys=True,
        indent=4,
        separators=(',', ': ')
    )

Result:

.. code-block:: python

    {
        "body": "quia et suscipit\nsuscipit recusandae [...]",
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "userId": 1
    }

Exception
---------

You can use `marshmallow <https://marshmallow.readthedocs.io/en/latest>`_
to serialize exceptions:

.. code-block:: python

    import json, sys
    from cdumay_rest_client.client import RESTClient
    from cdumay_http_client.exceptions import HTTPException, HTTPExceptionValidator

    try:
        client = RESTClient(server="http://jsonplaceholder.typicode.com")
        data = client.do_request(method="GET", path="/me")
    except HTTPException as exc:
        data = HTTPExceptionValidator().dump(exc).data

    json.dump(data, sys.stdout, sort_keys=True, indent=4, separators=(',', ': '))

Result:

.. code-block:: python

    {
        "code": 404,
        "extra": {},
        "message": "Not Found"
    }

License
-------

Licensed under `BSD 3-Clause License <./LICENSE>`_ or https://opensource.org/licenses/BSD-3-Clause.