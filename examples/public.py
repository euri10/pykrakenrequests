from pprint import pprint

import pykrakenrequests
from examples.config import PROXY, API_KEY, PRIVATE_KEY

client = pykrakenrequests.Client(API_KEY, PRIVATE_KEY, requests_kwargs=PROXY)
t = client.kpublic_time()
print("time as epoch: {}, time as UTC: {}".format(t[0], t[1]))

a = client.kpublic_assets(asset=['XETH', 'XBTC'])
pprint('===================================================================================')
pprint(a)
assetpairs = client.kpublic_assetpairs()
pprint('===================================================================================')
pprint(assetpairs.keys())
depth = client.kpublic_depth(pair=['XETHXXBT'])
pprint('===================================================================================')
pprint(depth)
trades = client.kpublic_trades(pair=['XETHXXBT'])
pprint('===================================================================================')
pprint(trades)
spread = client.kpublic_spread(pair=['XETHXXBT'])
pprint('===================================================================================')
pprint(spread)