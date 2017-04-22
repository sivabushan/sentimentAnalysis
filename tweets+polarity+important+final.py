
# coding: utf-8

# In[234]:

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import re
import pandas as pd
import numpy as np
import array


# In[235]:

get_ipython().magic('matplotlib inline')


# In[236]:

tweet_files = [r'C:\Users\Shrekar\Documents\PYTHON\twitter_search-master\Trump\trumpdate.json']
tweets = []
for file in tweet_files:
    with open(file, 'r') as f:
        for line in f.readlines():
            tweets.append(json.loads(line))


# In[237]:

df = pd.DataFrame(tweets)


# In[238]:

df


# In[239]:

df['text']


# In[240]:

tweet=df['text']


# In[241]:

blob = TextBlob(tweet[1])
blob.sentiment


# In[243]:

polar = pd.DataFrame()
n = int(len(tweet)) 
sen = []
for i in range(n):
    blob = TextBlob(tweet[i])
    k = blob.sentiment.polarity
    sen.append(k)


# In[244]:

polar['polarity'] = sen
polar


# In[245]:

senf_tran = senf.transpose

sennew = senf_tran
sennew


# In[246]:

df['favorite_count'].plot()


# In[247]:

import time
import pylab as pl


# In[248]:


from IPython import display
for i in range(10):
    pl.plot(pl.randn(10))
    display.clear_output(wait=True)
    display.display(pl.gcf())
    time.sleep(1.0)


# In[249]:


from IPython import display
for i in range(10):
    pl.plot(pl.polar.loc['polarity'])
    display.clear_output(wait=True)
    display.display(pl.gcf())
    time.sleep(1.0)


# In[250]:

#plt.axis([ 0, 100, -5,5])
plt.xlabel('Time')
plt.ylabel('Sentiment Polarity')
plt.plot(polar,'bo')
plt.show()
plt.pause(1)


# In[252]:

retweet = df['retweet_count']


# In[ ]:




# In[ ]:




# In[ ]:




# In[253]:

polar.hist()


# In[ ]:

polar.plot.bar()


# In[ ]:

polar.plot.line(x=polar.index,y='polarity',figsize=(12,3),lw=1)


# In[256]:

polar.plot.scatter(x='polarity',y='polarity')


# In[258]:

polar.plot.hexbin(x='polarity',y='polarity',gridsize=25,cmap='Oranges')


# In[ ]:



