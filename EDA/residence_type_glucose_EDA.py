#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd 
import numpy as np


# In[48]:


data = pd.read_csv('./healthcare-dataset-stroke-data.csv',sep = ',',header = 0) 


# In[49]:


data.head(10)


# In[50]:


#drop id column
data.drop('id', inplace=True, axis=1)


# In[51]:


data.head(10)


# # Correlation

# In[12]:


data.corr()


# In[33]:


sns.heatmap(data.corr(),cmap='Dark2_r',annot=True)
plt.title("Correlation")
plt.show()


# In[72]:


#Change other columns to numeric data
Another_data = data.copy()
Another_data['gender'] = np.where((Another_data['gender'] == "Female"), 1, 0)
Another_data['ever_married'] = np.where((Another_data['ever_married'] == "Yes"), 1, 0)
Another_data['Residence_type'] = np.where((Another_data['Residence_type'] == "Urban"), 1, 0)
Another_data['work_type'] = Another_data['work_type'].factorize()[0]
Another_data['smoking_status'] = Another_data['smoking_status'].factorize()[0]
Another_data.head(20)


# In[77]:


plt.figure(figsize=(9,9))
sns.heatmap(Another_data.corr(),annot=True, linewidths=0.1)
plt.title("Expanded Correlation")
plt.show()


# ## Residence-type and Avg_glucose_level Analysis

# In[6]:


from matplotlib import pyplot as plt
import seaborn as sns
plt.style.use('seaborn')


# In[7]:


fig, ax= plt.subplots(figsize=(9,7))
sns.countplot(x='Residence_type', data=data, ax=ax)
plt.xlabel("Residence_type")
plt.ylabel("Count")
plt.show()


# In[8]:


fig, ax= plt.subplots(figsize=(9,7))
sns.countplot(x="stroke",hue = "Residence_type", data=data, ax=ax)
plt.xlabel("Stroke")
plt.ylabel("Count")
plt.legend(loc='upper right', title='Residence_type:', labels=['Urban','Rural'])
plt.show()


# In[9]:


fig, ax= plt.subplots(figsize=(9,7))
sns.histplot(x="avg_glucose_level", data=data, ax=ax)
plt.xlabel("Avg_glucose_level")
plt.ylabel("Count")
#plt.legend(loc='upper right', title='Residence_type:', labels=['Urban','Rural'])
plt.show()


# In[10]:


fig, ax= plt.subplots(figsize=(9,7))
sns.histplot(x="avg_glucose_level",hue = "stroke", data=data, ax=ax)
plt.xlabel("Avg_glucose_level")
plt.ylabel("Count")
#plt.legend(loc='upper right', title='Residence_type:', labels=['Urban','Rural'])
plt.show()


# ### Multivariate Analysis 

# In[22]:


plt.figure(figsize=(9,7))
sns.histplot(x="avg_glucose_level",hue = "Residence_type", data=data)
plt.xlabel("Avg_glucose_level")
plt.ylabel("Count")
#plt.legend(loc='upper right', title='Residence_type:', labels=['Urban','Rural'])
plt.show()


# In[20]:


sns.relplot(x="avg_glucose_level",y = "Residence_type",hue = "stroke", data=data)
plt.xlabel("Avg_glucose_level")
plt.ylabel("Residence_type")
plt.show()
#Actually 


# In[21]:


sns.pairplot(data, hue = 'stroke')


# In[ ]:




