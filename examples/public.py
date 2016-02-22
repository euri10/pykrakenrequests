from pprint import pprint

import pykrakenrequests
from examples.config import PROXY, API_KEY

client = pykrakenrequests.Client(API_KEY, requests_kwargs=PROXY)
t = client.kpublic_time()
print("time as epoch: {}, time as UTC: {}".format(t[0], t[1]))

a = client.kpublic_assets(asset=['XETH', 'XBTC'])
pprint(a)
