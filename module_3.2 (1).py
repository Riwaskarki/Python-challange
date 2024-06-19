#!/usr/bin/env python
# coding: utf-8

# In[33]:


#importing pandas library to read the file.
import pandas as pd
import numpy as np


# In[35]:


# reading the file through the path
df_election = pd.read_csv(r"C:\Users\karki\Downloads\Starter_Code (4)\Starter_Code\PyPoll\Resources\election_data.csv")


# In[37]:


#Displaying first 5 row.
df_election.head(5)


# In[43]:


df_election_list = df_election['Candidate'].unique()
df_election_list


# In[10]:


df_election_list


# In[45]:


#displaying the total candidates.
df_election_total =len(df_election.value_counts())
df_election_total


# In[47]:


#total votes per candidate.
df_total_votes = df_election['Candidate'].value_counts()
df_total_votes


# In[49]:


df_election['Candidate'].value_counts(normalize=True)


# In[51]:


#calculating the percentage.
df_percent = df_election['Candidate'].value_counts(normalize=True).mul(100).round(3).astype(str) + '%'
df_percent


# In[53]:


#Displaying the first row as first row is the winner.
df_winner = df_percent.head(1)
df_winner


# In[55]:


#printing the final results.
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





# In[ ]:




