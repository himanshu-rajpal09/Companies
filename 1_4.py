#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib


# In[67]:


df1 = pd.read_csv('C:\\Users\\Himanshu\\Downloads\\singapore-residents-by-age-group-ethnic-group-and-sex-end-june-annual.csv')


# In[68]:


df2 = df1.groupby(['year', 'level_1']).agg({'value':'sum'}).reset_index()


# In[69]:


df2.head()


# In[89]:


df3 = df2[df2.level_1 == 'Total Residents'].value.reset_index()
df3


# In[71]:


df3.drop('index', axis = 'columns', inplace = True)
df3.head()


# In[72]:


df4 = pd.read_csv('C:\\Users\\Himanshu\\Downloads\\Year.csv')
df4


# In[80]:


frames = [df4,df3]
result = pd.concat(frames, axis = 1)
result.head()


# In[94]:


result.plot(x='year', y='value', kind = 'bar', figsize = (20,10))


# In[ ]:




