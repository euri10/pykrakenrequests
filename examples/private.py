from pprint import pprint

import pykrakenrequests
from examples.config import PROXY, API_KEY, PRIVATE_KEY

client = pykrakenrequests.Client(API_KEY, PRIVATE_KEY, requests_kwargs=PROXY)
t = client.kpublic_time()


txids = client.kprivate_tradesHistory()
# pprint(txids['trades'])

txid = txids['trades'].keys()[0]

onequery = client.kprivate_queryTrades(txid=[txid])
pprint(onequery)

