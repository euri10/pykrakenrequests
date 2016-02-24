import pykrakenrequests

def kprivate_getBalance(client):
    c = client._post("/0/private/Balance")
    return c['result']

def kprivate_getTradeBalance(client):
    c = client._post("/0/private/TradeBalance")
    return c['result']

def kprivate_getOpenOrders(client, trades=False, userref=None):
    params = {}
    if trades:
        params['trades'] = trades
    if userref:
        params['userref']= userref
    c = client._post("/0/private/OpenOrders", params)
    return c['result']