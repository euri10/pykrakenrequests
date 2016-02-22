import pykrakenrequests


def kpublic_time(client):
    c = client._post("/0/public/Time", "")
    return c['result']['unixtime'], c['result']['rfc1123']


def kpublic_assets(client, aclass=None, asset=None):
    params = {}
    assetList = ''
    if asset:
        for a in asset:
            assetList += a+','
        assetList = assetList[:-1]
        params['asset'] = assetList
    if aclass:
        if aclass is not "currency":
            raise pykrakenrequests.exceptions.BadParamterError()
    params['info'] = 'info'
    c = client._post("/0/public/Assets", params)
    return c['result']


