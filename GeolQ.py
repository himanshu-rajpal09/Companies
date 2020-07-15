#!/usr/bin/env python
# coding: utf-8

# In[139]:


import pandas as pd
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib


# In[166]:


df1 = pd.read_csv('C:\\Users\\Himanshu\\Downloads\\singapore-residents-by-age-group-ethnic-group-and-sex-end-june-annual.csv')


# In[167]:


df1.head()


# In[168]:


df1.dtypes


# In[169]:


df1.head(350)


# In[257]:


df2 = df1.groupby(['year','level_1']).agg({'value':'sum'}).reset_index()


# In[258]:


df2


# In[290]:


df3 = df2[df2.level_1 == 'Total Chinese'].value.reset_index()
df3


# In[269]:


df4 = df3.pct_change().reset_index()


# In[280]:


df4.head()


# In[278]:


df5 = df4.value.mean()
df5*100


# In[288]:


df6 = df2[df2.level_1 == 'Total Residents'].value.reset_index()
df6


# In[297]:


df7 = df3/df6
df7.reset_index()
df7.head(30)


# In[296]:


df7.value.mean()

