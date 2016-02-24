import pykrakenrequests

def kprivate_getBalance(client):
    c = client._post("/0/private/Balance", "")
    return c['result']

def kprivate_getTradeBalance(client):
    c = client._post("/0/private/TradeBalance", "")
    return c['result']