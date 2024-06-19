#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[4]:


df_Budget = pd.read_csv(r"C:\Users\karki\Downloads\Starter_Code (4)\Starter_Code\PyBank\Resources\budget_data.csv")


# In[6]:


df_Budget.head()


# In[8]:


df_total_months = len(df_Budget['Date'].value_counts())
df_total_months


# In[10]:


df_Total = df_Budget['Profit/Losses'].sum()
df_Total


# In[12]:


df_mean = df_Budget['Profit/Losses'].mean()
df_mean.round(decimals=2)


# In[16]:


min_least = df_Budget['Profit/Losses'].min()
min_least


# In[ ]:


max_index = df_Budget['Profit/Losses'].idxmax()
df_max = df_Budget.iloc[max_index]
df_max


# In[ ]:


print('Financial analysis')
print('----------------------------------')
print('Total Months :') 
print(df_total_months)
print("Total Profit/Losses:")
print(df_Total)
print('Average Change: ')
print(df_mean.round(decimals=2))

print('Greatest Increase in Profits:')
print(df_max)
print('---------------------------')
print('Greatest Decrease in Profits:')
print(df_min)


# In[ ]:




