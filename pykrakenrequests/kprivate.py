import pykrakenrequests
from pykrakenrequests.convert import commasep


def kprivate_getBalance(client):
    c = client._post("/0/private/Balance")
    return c['result']


def kprivate_getTradeBalance(client, aclass='currency', asset='ZUSD'):
    params = {}
    if aclass:
        params['aclass'] = aclass
    if asset:
        params['asset'] = asset
    c = client._post("/0/private/TradeBalance", params)
    return c['result']


def kprivate_getOpenOrders(client, trades=False, userref=None):
    params = {}
    if trades:
        params['trades'] = trades
    if userref:
        params['userref'] = userref
    c = client._post("/0/private/OpenOrders", params)
    return c['result']


def kprivate_getClosedOrders(client, trades=False, userref=None, start=None, end=None, ofs=None, closetime='both'):
    params = {}
    if trades:
        params['trades'] = trades
    if userref:
        params['userref'] = userref
    if start:
        params['start'] = start
    if end:
        params['end'] = end
    if ofs:
        params['ofs'] = ofs
    if closetime:
        params['closetime'] = closetime

    c = client._post("/0/private/ClosedOrders", params)
    return c['result']


def kprivate_queryOrders(client, trades=False, userref=None, txid=None):
    params = {}
    if trades:
        params['trades'] = trades
    if userref:
        params['userref'] = userref
    if txid:
        params['txid'] = commasep(txid)

    c = client._post("/0/private/QueryOrders", params)
    return c['result']


def kprivate_tradesHistory(client, typet=None, trades=False, start=None, end=None, ofs=None):
    params = {}
    if typet and typet in ['all', 'any position', 'closed position', 'closing position', 'no position']:
        # using typet variable as type is reserved, but it need to be type in the params dictionnary
        params['type'] = typet
    if trades:
        params['trades'] = trades
    if start:
        params['start'] = start
    if end:
        params['end'] = end
    if ofs:
        params['ofs'] = ofs

    c = client._post("/0/private/TradesHistory", params)
    return c['result']


def kprivate_queryTrades(client, txid=None, trades=False):
    params = {}
    if txid and len(txid) <= 20 and isinstance(txid, list):
        params['txid'] = commasep(txid)
    if trades:
        params['trades'] = trades
    c = client._post("/0/private/QueryTrades", params)
    return c['result']

def kprivate_openPositions(client, txid=None, docalcs=False):
    params = {}
    if txid and isinstance(txid, list):
        params['txid'] = commasep(txid)
    if docalcs:
        params['docalcs'] = docalcs

    c = client._post("/0/private/OpenPositions", params)
    return c['result']
