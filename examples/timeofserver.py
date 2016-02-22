import pykrakenrequests
from config import PROXY

client = pykrakenrequests.Client('totokey',requests_kwargs=PROXY)
print(client.kpublic("Time"))
