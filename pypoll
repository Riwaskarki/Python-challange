#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import numpy as np


# In[4]:


df_election = pd.read_csv(r"C:\Users\karki\Downloads\Starter_Code (4)\Starter_Code\PyPoll\Resources\election_data.csv")


# In[12]:


display(df_election)


# In[14]:


df_election_list = df_election['Candidate'].unique()


# In[16]:


df_election_list


# In[20]:


df_election_total =len(df_election.value_counts())
df_election_total


# In[64]:


df_total_votes = df_election['Candidate'].value_counts()
df_total_votes


# In[50]:


df_election['Candidate'].value_counts(normalize=True)


# In[56]:


df_percent = df_election['Candidate'].value_counts(normalize=True).mul(100).round(3).astype(str) + '%'
df_percent


# In[98]:


print('Election Results')
print('----------------------------------')
print('Total Votes:')
print(df_election_total)
print('----------------------------------')
print(df_percent)
print('----------------------------------')
print('Winner : Diana DeGette with 73.812% vote')
print('----------------------------------')
      


# In[ ]:




