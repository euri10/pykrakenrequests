import pykrakenrequests
from pykrakenrequests.convert import commasep


def kpublic_time(client):
    c = client._post("/0/public/Time")
    return c['result']['unixtime'], c['result']['rfc1123']



def kpublic_assets(client, info='info', aclass=None, asset=None):
    params = {}
    if info:
        params['info'] = info
    if asset:
        params['asset'] = commasep(asset)
    if aclass:
        if aclass is not "currency":
            raise pykrakenrequests.exceptions.BadParamterError()
    c = client._post("/0/public/Assets", params)
    return c['result']


def kpublic_assetpairs(client, info='info', pair=None):
    params = {}
    if info not in ['info', 'leverage', 'fees', 'margin']:
        raise pykrakenrequests.exceptions.BadParamterError()
    else:
        params['info'] = info
    if pair:
        params['pair'] = commasep(pair)

    c = client._post("/0/public/AssetPairs", params)
    return c['result']

def kpublic_ticker(client, pair=None):
    params = {}
    if pair:
        params['pair'] = commasep(pair)
    else:
        raise pykrakenrequests.exceptions.BadParamterError()
    c = client._post("/0/public/Ticker", params)
    return c['result']

def kpublic_OHLC(client, pair=None, interval=1,since=None):
    params = {}
    if pair:
        params['pair'] = commasep(pair)
    else:
        raise pykrakenrequests.exceptions.BadParamterError()
    if interval:
        params['interval'] = interval
    if since:
        params['since'] = since
    c = client._post("/0/public/OHLC", params)
    return c['result']

def kpublic_depth(client, pair=None, count=None):
    params = {}
    if pair:
        params['pair'] = commasep(pair)
    else:
        raise pykrakenrequests.exceptions.BadParamterError()
    if count:
        params['count']=count

    c = client._post("/0/public/Depth", params)
    return c['result']


def kpublic_trades(client, pair=None, since=None):
    params = {}
    if pair:
        params['pair'] = commasep(pair)
    else:
        raise pykrakenrequests.exceptions.BadParamterError()
    if since:
        params['count']=since

    c = client._post("/0/public/Trades", params)
    return c['result']

def kpublic_spread(client, pair=None, since=None):
    params = {}
    if pair:
        params['pair'] = commasep(pair)
    else:
        raise pykrakenrequests.exceptions.BadParamterError()
    if since:
        params['count']=since

    c = client._post("/0/public/Spread", params)
    return c['result']

