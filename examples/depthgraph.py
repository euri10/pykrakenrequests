from examples.config import API_KEY, PRIVATE_KEY, PROXY
from pykrakenrequests.client import Client
import pandas as pd
import matplotlib.pyplot as plt
client = Client(API_KEY, PRIVATE_KEY, requests_kwargs=PROXY)
depth = client.kpublic_depth(pair=['XETHZEUR'])
print(depth)
bidsdf = pd.DataFrame(depth['XETHZEUR']['bids'])
bidsdf = bidsdf.astype(float)
print bidsdf.head(5)
bidsdf[1].plot(kind='barh')

plt.show()
