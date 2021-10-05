#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np
import pandas as pd
df = pd.read_csv('data.csv')
df.head()


# In[26]:


df1 = pd.read_csv('activity_data.csv')
df1.head()


# In[27]:


df.drop(['_type', '_id', '_score'], axis = 1, inplace = True)


# In[28]:


df

