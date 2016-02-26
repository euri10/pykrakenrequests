import pykrakenrequests
from pykrakenrequests.convert import commasep

def kprivate_getBalance(client):
    c = client._post("/0/private/Balance")
    return c['result']

def kprivate_getTradeBalance(client, aclass='currency', asset='ZUSD'):
    params = {}
    if aclass:
        params['aclass']=aclass
    if asset:
        params['asset']=asset
    c = client._post("/0/private/TradeBalance", params)
    return c['result']

def kprivate_getOpenOrders(client, trades=False, userref=None):
    params = {}
    if trades:
        params['trades'] = trades
    if userref:
        params['userref']= userref
    c = client._post("/0/private/OpenOrders", params)
    return c['result']

def kprivate_getClosedOrders(client, trades=False, userref=None, start=None, end=None, ofs=None, closetime='both'):
    params = {}
    if trades:
        params['trades'] = trades
    if userref:
        params['userref']= userref
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
    params ={}
    if trades:
        params['trades'] = trades
    if userref:
        params['userref']= userref
    if txid:
        params['txid'] = commasep(txid)

    c = client._post("/0/private/QueryOrders", params)
    return c['result']
