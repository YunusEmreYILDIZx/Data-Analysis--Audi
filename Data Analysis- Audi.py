#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn


# In[13]:


dataFrame = pd.read_excel("audi.xlsx")


# In[14]:


dataFrame


# In[15]:


dataFrame.describe()


# In[16]:


dataFrame.isnull().sum()


# In[17]:


plt.figure(figsize=(7,5))
sbn.distplot(dataFrame["price"])


# In[18]:


sbn.countplot(dataFrame["year"])


# In[19]:


dataFrame.corr()


# In[20]:


dataFrame.corr()["price"].sort_values()


# In[21]:


sbn.scatterplot(x="mileage",y="price",data=dataFrame)


# In[22]:


dataFrame.sort_values("price",ascending = False).head(20)


# In[23]:


dataFrame.sort_values("price",ascending = True).head(20)


# In[24]:


len(dataFrame)


# In[25]:


len(dataFrame) * 0.01


# In[26]:


yuzdeDoksanDokuzDf = dataFrame.sort_values("price",ascending = False).iloc[131:]


# In[27]:


yuzdeDoksanDokuzDf.describe()


# In[28]:


plt.figure(figsize=(7,5))
sbn.distplot(yuzdeDoksanDokuzDf["price"])


# In[29]:


dataFrame.describe()


# In[30]:


dataFrame.groupby("year").mean()["price"]


# In[31]:


yuzdeDoksanDokuzDf.groupby("year").mean()["price"]


# In[32]:


dataFrame[dataFrame.year != 1970].groupby("year").mean()["price"]


# In[33]:


dataFrame = yuzdeDoksanDokuzDf


# In[34]:


dataFrame.describe()


# In[35]:


dataFrame = dataFrame[dataFrame.year != 1970]


# In[36]:


dataFrame.groupby("year").mean()["price"]


# In[37]:


dataFrame.head()

