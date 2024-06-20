#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv("C:/Users/Gayatri/Downloads/HR_Analytics (1).csv")


# In[3]:


data.head()


# In[4]:


data.tail()


# In[5]:


data.info()


# In[6]:


data.isna().sum()


# In[7]:


data.dropna(inplace = True)


# In[8]:


data.isna().sum()


# In[9]:


data.describe()


# In[10]:


data.corr()


# In[15]:


plt.figure(figsize=(30,30))
sns.boxplot(data["MonthlyIncome"])


# In[ ]:




