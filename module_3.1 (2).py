#!/usr/bin/env python
# coding: utf-8

# In[23]:


#importing the panads library
import pandas as pd


# In[25]:


#importing the dataset.
df_Budget = pd.read_csv(r"C:\Users\karki\Downloads\Starter_Code (4)\Starter_Code\PyBank\Resources\budget_data.csv")


# In[27]:


#Reading the 5 headers.
df_Budget.head(5)


# In[29]:


#counting the total months
df_total_months = len(df_Budget['Date'].value_counts())
df_total_months


# In[31]:


#Calculating the total budget.
df_Total = df_Budget['Profit/Losses'].sum()
df_Total


# In[33]:


#Average of the Budget.
df_mean = df_Budget['Profit/Losses'].mean()
df_mean.round(decimals=2)


# In[35]:


#minimum value in profit/losses.
min_least = df_Budget['Profit/Losses'].min()
min_least


# In[37]:


#trying different code to look for max value.
max_index = df_Budget['Profit/Losses'].idxmax()
df_max = df_Budget.iloc[max_index]
df_max


# In[39]:


#printing the final result.
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
print(min_least)


# In[ ]:




