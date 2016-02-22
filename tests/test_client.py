import time

from datetime import datetime, timedelta

import pykrakenrequests
from pykrakenrequests import client as _client
import unittest
from examples.config import PROXY


class ClientTest(unittest.TestCase):
    def test_no_api_key(self):
        with self.assertRaises(Exception):
            client = pykrakenrequests.Client()

    def test_server_time(self):
        client = pykrakenrequests.Client('superpublickey', requests_kwargs=PROXY)
        t = client.kpublic('Time')
        # t_compare = datetime.strptime(t[1], '%a, %d %b %y %H:%M:%S +0000')
        t_compare = t[0]
        utcnow = time.time()
        print(utcnow)
        delta = t_compare - utcnow
        print(delta)
        self.assertLess(delta, 2)
