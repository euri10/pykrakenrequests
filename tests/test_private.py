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
        tbkeys = ['eb', 'tb', 'm', 'n', 'c', 'v', 'e', 'mf']
        tbbool = [k in t.keys() for k in tbkeys]
        self.assertTrue(all(tbbool))

    def test_open_orders(self):
        client = pykrakenrequests.Client(key=API_KEY, private_key=PRIVATE_KEY, requests_kwargs=PROXY)
        t = client.kprivate_getOpenOrders(trades=False)
        self.assertTrue('open' in t.keys())

    def test_closed_orders(self):
        client = pykrakenrequests.Client(key=API_KEY, private_key=PRIVATE_KEY, requests_kwargs=PROXY)
        t = client.kprivate_getClosedOrders(trades=False)
        self.assertTrue('closed' in t.keys())

    def test_tradesHistory(self):
        client = pykrakenrequests.Client(key=API_KEY, private_key=PRIVATE_KEY, requests_kwargs=PROXY)
        t = client.kprivate_tradesHistory(trades=False)
        self.assertTrue('count' in t.keys())

    def test_queryTrades(self):
        client = pykrakenrequests.Client(key=API_KEY, private_key=PRIVATE_KEY, requests_kwargs=PROXY)
        t = client.kprivate_queryTrades(trades=False)
        self.assertTrue('count' in t.keys())

    def test_openPositions(self):
        client = pykrakenrequests.Client(key=API_KEY, private_key=PRIVATE_KEY, requests_kwargs=PROXY)
        t = client.kprivate_openPositions()
        # TODO find a better test
        self.assertIsInstance(t, dict)

    def test_getLedgers(self):
        client = pykrakenrequests.Client(key=API_KEY, private_key=PRIVATE_KEY, requests_kwargs=PROXY)
        t = client.kprivate_getLedgers()
        # TODO find a better test
        self.assertTrue('count' in t.keys())

    def test_queryLedgers(self):
        client = pykrakenrequests.Client(key=API_KEY, private_key=PRIVATE_KEY, requests_kwargs=PROXY)
        t = client.kprivate_queryLedgers()
        # TODO find a better test
        self.assertTrue('count' in t.keys())

    def test_tradeVolume(self):
        client = pykrakenrequests.Client(key=API_KEY, private_key=PRIVATE_KEY, requests_kwargs=PROXY)
        t = client.kprivate_tradeVolume()
        # TODO find a better test
        self.assertTrue('count' in t.keys())

    def test_order_required_pair(self):
        with self.assertRaises(pykrakenrequests.exceptions.RequiredParameterError):
            client = pykrakenrequests.Client(key=API_KEY, private_key=PRIVATE_KEY, requests_kwargs=PROXY)
            t = client.kprivate_addOrder()

    def test_addOrder(self):
        # add validate=True just to enter False orders
        client = pykrakenrequests.Client(key=API_KEY, private_key=PRIVATE_KEY, requests_kwargs=PROXY)
        t = client.kprivate_addOrder(pair='XETHZEUR', typeo='buy', ordertype='limit', price=4.23, volume=10,
                                     starttm='+5', validate=True)
        self.assertTrue('descr' in t.keys())
