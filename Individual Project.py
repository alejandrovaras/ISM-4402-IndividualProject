#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[3]:


df['Cars Sold'].mean()


# In[4]:


df['Cars Sold'].max()


# In[5]:


df['Cars Sold'].min()


# In[6]:


pd.pivot_table(df,
 values=['Cars Sold'],
 index=['Gender'])


# In[19]:


df.loc[df['Cars Sold']>3]['Hours Worked'].mean()


# In[20]:


df['Years Experience'].mean()


# In[21]:


df.loc[df['Cars Sold']>3]['Years Experience'].mean()


# In[28]:


pd.pivot_table(df,
 values=['Cars Sold'],
 index=['SalesTraining'])


# In[30]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[31]:


df.hist(column="Years Experience", by="SalesTraining")


# In[36]:


df.boxplot(by='Gender', column='Cars Sold')


# In[ ]:




