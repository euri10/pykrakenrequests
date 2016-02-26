from examples.config import API_KEY, PRIVATE_KEY, PROXY
from pykrakenrequests.client import Client
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

client = Client(API_KEY, PRIVATE_KEY, requests_kwargs=PROXY)
depth = client.kpublic_depth(pair=['XETHZEUR'])
print(depth)
# bidsdf = pd.DataFrame([[d[1], d[2]] for d in depth['XETHZEUR']['bids']],
#                       index=[d[0] for d in depth['XETHZEUR']['bids']])
bidsdf = pd.DataFrame(depth['XETHZEUR']['bids'])
bidsdf = bidsdf.astype(float)
# asksdf = pd.DataFrame([[d[1], d[2]] for d in depth['XETHZEUR']['asks']],
#                       index=[d[0] for d in depth['XETHZEUR']['asks']])

asksdf = pd.DataFrame(depth['XETHZEUR']['asks'])
asksdf = asksdf.astype(float)
print bidsdf.head(5)
print bidsdf.tail(5)

print asksdf.head(5)
print asksdf.tail(5)

print bidsdf.columns
print bidsdf.dtypes

bidsdf['t'] = 'bids'
asksdf['t'] = 'asks'
df = bidsdf.append(asksdf)
df.columns = ['price', 'volume', 'timestamp', 't']
print(df)
#TODO : palette that tells its red when col is red and green when col is green
pal = {v: "r" if v == 'asks' else 'g' for v in df['volume']}
print(pal)
sns.barplot(x='volume', y='price', data=df, orient='h', palette=pal)
plt.show()
