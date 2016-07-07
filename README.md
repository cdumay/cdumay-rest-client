[![Build Status](https://travis-ci.org/cdumay/cdumay-rest-client.svg?branch=master)](https://travis-ci.org/cdumay/cdumay-rest-client)

# cdumay-rest-client

This library is a basic REST client with exception formatting.

## Quickstart

First, install cdumay-rest-client using 
[pip](https://pip.pypa.io/en/stable/):

    $ pip install flask-zookeeper

Next, add a `RESTClient` instance to your code:

```python
    >>> from cdumay_rest_client.client import RESTClient
    >>> 
    >>> client = RESTClient(server="http://jsonplaceholder.typicode.com")
    >>> print(client.do_request(method="GET", path="/posts/1"))
    {'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto', 'userId': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'id': 1}
```


       
## Exception

You can use [marshmallow](https://marshmallow.readthedocs.io/en/latest)
to serialize exceptions:

```python
    >>> from cdumay_rest_client.client import RESTClient
    >>> from cdumay_rest_client.exceptions import HTTPException, HTTPExceptionValidator
    >>> 
    >>> client = RESTClient(server="http://jsonplaceholder.typicode.com")
    >>> try:
    >>>    print(client.do_request(method="GET", path="/me"))
    >>> except HTTPException as exc:
    >>>    print(HTTPExceptionValidator().dump(exc).data)
    {'code': 404, 'message': 'Not Found', 'extra': {}}
```

## License

Apache License 2.0