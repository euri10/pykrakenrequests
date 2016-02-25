import pykrakenrequests
import unittest
from examples.config import PROXY, API_KEY, PRIVATE_KEY


class ClientTestPrivate(unittest.TestCase):

    def test_balance(self):
        client = pykrakenrequests.Client(key=API_KEY, private_key=PRIVATE_KEY, requests_kwargs=PROXY)
        t = client.kprivate_getBalance()
        self.assertTrue('XXBT' in t.keys())

    def test_trade_balance(self):
        client = pykrakenrequests.Client(key=API_KEY, private_key=PRIVATE_KEY, requests_kwargs=PROXY)
        t = client.kprivate_getTradeBalance()
        print(t.keys())
        # ml should be in this list, dunno why on my account it's not, maybe because i don't have margin yet
        tbkeys = ['eb', 'tb', 'm', 'n', 'c', 'v', 'e', 'mf' ]
        tbbool = [k in t.keys() for k in tbkeys]
        self.assertTrue(all(tbbool))

    def test_open_orders(self):
        client = pykrakenrequests.Client(key=API_KEY, private_key=PRIVATE_KEY, requests_kwargs=PROXY)
        t = client.kprivate_getOpenOrders(trades=True)
        print(t)