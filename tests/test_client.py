import time
import pykrakenrequests
from pykrakenrequests import client as _client
import unittest

class ClientTest(unittest.TestCase):

    def test_no_api_key(self):
        with self.assertRaises(Exception):
            client = pykrakenrequests.Client()
