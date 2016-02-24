import pykrakenrequests

def kprivate_getBalance(client):
    c = client._post("/0/private/Balance", "")
    return c['result']