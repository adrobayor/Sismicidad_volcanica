
# coding: utf-8

# # señal

# In[1]:

from obspy import read


# In[2]:

import numpy as np


# In[3]:

from obspy import UTCDateTime, Stream


# In[4]:

from scipy import signal


# In[5]:

from numpy.fft import fft
from numpy import array


# In[6]:

st = read("Package_AguilleDru_2377562_SED.mseed")


# In[7]:

st2 = st.select(id="CH.EMV..HHZ")
st3 = st.select(id="CH.EMV..HHN")
st4 = st.select(id="CH.EMV..HHE")
st5 = st.select(id="CH.FUSIO..HHZ")
st6 = st.select(id="CH.FUSIO..HHN")
st7 = st.select(id="CH.FUSIO..HHE")


# In[8]:

print(st2, st3, st4)


# In[10]:

st2.plot(color="red")
st3.plot(color="blue")
st4.plot(color="orange")
st5.plot(color="green")
st6.plot()



# In[11]:

len(st2)
len(st3)
len(st4)
len(st5)
len(st6)


# In[12]:

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[13]:

import obspy


# In[14]:

import obspy.signal


# In[15]:

data = st2[0].data
npts = st2[0].stats.npts
samprate = st[0].stats.sampling_rate


# In[16]:

st2_filt = st2.copy()
st2_filt.filter("bandpass", freqmin=1, freqmax=30, corners=2, zerophase=True)


# In[17]:

data_envelope = obspy.signal.filter.envelope(st2[0].data)


# In[18]:

plt.figure(figsize=(8,3))
plt.plot(data_envelope)


# In[19]:

x = st2[0].data 


# In[20]:

x2 = x-np.mean(x)


# In[23]:

plt.figure(figsize=(8,4))
plt.plot(x2)


# In[24]:

x2 = signal.detrend(x2)


# In[25]:

plt.plot(x2)


# In[26]:

np.array([x2])


# In[27]:

a = np.array([x2])


# In[ ]:



