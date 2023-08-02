#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>


"""
import unittest
from unittest.mock import patch

from requests import Response

from cdumay_rest_client.client import RESTClient


class BaseTestCase(unittest.TestCase):
    def test_init(self):
        """Client inititialization"""
        client = RESTClient(server="http://localhost", timeout=15)
        self.assertEqual(client.server, "http://localhost")
        self.assertEqual(client.timeout, 15)
        self.assertEqual(client.headers, {'Accept': 'application/json', 'Content-Type': 'application/json'})
        self.assertIsNone(client.auth)
        self.assertEqual(client.ssl_verify, True)
        self.assertEqual(client.retry_number, 10)
        self.assertEqual(client.retry_delay, 30)
        self.assertEqual(repr(client), 'Connection: http://localhost')

    def test_get(self):
        client = RESTClient(server="http://localhost", timeout=15)
        resp = Response()
        resp.status_code = 200
        resp.encoding = 'UTF-8'
        resp._content = b'{"user_id": 1, "name": "john"}'
        with patch('requests.request', return_value=resp):
            data = client.do_request(method="GET", path="/posts/1")
        self.assertEqual(data['user_id'], 1)
        self.assertEqual(data['name'], "john")
        self.assertNotIn('age', data)
