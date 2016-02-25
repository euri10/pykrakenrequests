import pykrakenrequests


def kpublic_time(client):
    c = client._post("/0/public/Time")
    return c['result']['unixtime'], c['result']['rfc1123']


def commasep(entryList, sep=','):
    outStr = ''
    return sep.join(entryList)

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
