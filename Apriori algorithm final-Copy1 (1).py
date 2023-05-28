#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import the packages
import pandas as pd
import numpy as np
from apyori import apriori


# In[4]:


#Load the dataset from the system
store_data = pd.read_csv('C:\WORK\Codeclause\Market_Basket_Optimisation.csv',header=None)


# In[5]:


#retrieving first rows of dataframe
store_data.head()


# In[6]:


#data cleaning and checking for irregularity
store_data.fillna(0,inplace=True)


# In[7]:


store_data.head()


# In[8]:


#data is converted into lists
transactions = []

for i in range(0,len(store_data)):
    transactions.append([str(store_data.values[i,j]) for j in range(0,20) if str(store_data.values[i,j])!='0'])


# In[9]:


#verifying if converted
transactions[0]


# In[10]:


#verifying
transactions[1]


# In[11]:


#verifying
transactions[2]


# In[12]:


# calling apriori function where:min_support = 0.003,min_lift = 3,min_confidence = 0.2,min_lenth=2
rules = apriori(transactions, min_support=0.003, min_confidance=0.2, min_lift=3, min_length=2)


# In[13]:


#rules are created
rules


# In[14]:


#rules converted to list
Results = list(rules)
Results


# In[15]:


#create another dataframe store_data_results
store_data_results = pd.DataFrame(Results)


# In[16]:


store_data_results.head()


# In[17]:


#support is kept in another dataframe
support = store_data_results.support


# In[18]:


first_values = []
second_values = []
third_values = []
fourth_value = []
#create list and store values
for i in range(store_data_results.shape[0]):
    single_list = store_data_results['ordered_statistics'][i][0]
    first_values.append(list(single_list[0]))
    second_values.append(list(single_list[1]))
    third_values.append(single_list[2])
    fourth_value.append(single_list[3])


# In[19]:


#convert all list into dataframe
lhs = pd.DataFrame(first_values)
rhs = pd.DataFrame(second_values)

confidance=pd.DataFrame(third_values,columns=['Confidance'])

lift=pd.DataFrame(fourth_value,columns=['lift'])


# In[20]:


#store all lists together in a single dataframe
store_data_final = pd.concat([lhs,rhs,support,confidance,lift], axis=1)
store_data_final


# In[21]:


#arranging the dataframe
store_data_final.fillna(value=' ', inplace=True)
store_data_final.head()


# In[22]:


#set the column names
store_data_final.columns = ['lhs',1,'rhs',2,3,'support','confidance','lift']
store_data_final.head()


# In[23]:


#adding all 3 columns to:
store_data_final['lhs'] = store_data_final['lhs'] + str(", ") + store_data_final[1]

store_data_final['rhs'] = store_data_final['rhs']+str(", ")+store_data_final[2] + str(", ") + store_data_final[3]


# In[24]:


store_data_final.head()


# In[25]:


#dropping columns 1,2 and 3
store_data_final.drop(columns=[1,2,3],inplace=True)


# In[26]:


#final output
store_data_final.head()


# In[28]:


#displaying the items based on lift
store_data_final.sort_values('lift', ascending=False).head(10)


# In[ ]:




