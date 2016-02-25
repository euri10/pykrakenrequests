import time
import pykrakenrequests
import unittest
from examples.config import PROXY, API_KEY, PRIVATE_KEY

class ClientTestPublic(unittest.TestCase):
    def test_no_api_key(self):
        with self.assertRaises(Exception):
            client = pykrakenrequests.Client()

    def test_server_time(self):
        client = pykrakenrequests.Client(API_KEY, PRIVATE_KEY, requests_kwargs=PROXY)
        utcnow = time.time()
        t = client.kpublic_time()
        # t_compare = datetime.strptime(t[1], '%a, %d %b %y %H:%M:%S +0000')
        t_compare = t[0]
        print("t_compare: {} utcnow: {}".format(t_compare, utcnow))
        delta = t_compare - utcnow
        self.assertLessEqual(abs(delta), 6)

    def test_assets_asset_parameter(self):
        client = pykrakenrequests.Client(API_KEY, PRIVATE_KEY, requests_kwargs=PROXY)
        t = client.kpublic_assets(asset=['XETH'])
        self.assertTrue(u'XETH' in t.keys())

    def test_assets_aclass_parameter(self):
        with self.assertRaises(pykrakenrequests.exceptions.BadParamterError):
            client = pykrakenrequests.Client(API_KEY, PRIVATE_KEY, requests_kwargs=PROXY)
            t = client.kpublic_assets(aclass='mouahahah bad parameter')

    def test_assetpairs(self):
        client = pykrakenrequests.Client(API_KEY, PRIVATE_KEY, requests_kwargs=PROXY)
        t = client.kpublic_assetpairs()
        # TODO: find a better test
        self.assertTrue('XXBTZUSD' in t.keys())

    def test_ticker(self):
        client = pykrakenrequests.Client(API_KEY, PRIVATE_KEY, requests_kwargs=PROXY)
        t = client.kpublic_ticker(pair=['XETHXXBT'])
        print(t)
        self.assertTrue('XETHXXBT' in t.keys())

    def test_OHLC(self):
        client = pykrakenrequests.Client(API_KEY, PRIVATE_KEY, requests_kwargs=PROXY)
        t = client.kpublic_OHLC(pair=['XETHXXBT'])
        print(t)
        self.assertTrue('XETHXXBT' in t.keys())

    def test_depth(self):
        client = pykrakenrequests.Client(API_KEY, PRIVATE_KEY, requests_kwargs=PROXY)
        t = client.kpublic_depth(pair=['XETHXXBT'])
        print(t)
        self.assertTrue('XETHXXBT' in t.keys())

    def test_trades(self):
        client = pykrakenrequests.Client(API_KEY, PRIVATE_KEY, requests_kwargs=PROXY)
        t = client.kpublic_trades(pair=['XETHXXBT'])
        print(t)
        self.assertTrue('XETHXXBT' in t.keys())

    def test_spread(self):
        client = pykrakenrequests.Client(API_KEY, PRIVATE_KEY, requests_kwargs=PROXY)
        t = client.kpublic_spread(pair=['XETHXXBT'])
        print(t)
        self.assertTrue('XETHXXBT' in t.keys())
