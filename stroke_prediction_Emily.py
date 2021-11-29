#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Load dataset
data = pd.read_csv('./healthcare-dataset-stroke-data.csv',sep = ',',header = 0) 


# In[3]:


# See first 10 rows of dataframe
data.head(10)


# In[4]:


# Make Dataframe copy with all columns I'm looking at
df = data[['gender', 'age', 'stroke']].copy()
df


# In[5]:


#Check for null values in this dataframe
df.isnull().values.any()


# # Univariate Analysis: Gender

# In[6]:


# Look at unique values in gender column
df.gender.value_counts()


# In[7]:


#Get rid of outlier
df = df[df.gender != 'Other']


# In[8]:


# Check unique values in gender column again
df.gender.value_counts()


# In[9]:


# Store counts for Female and Male in gender column in fem_ct and men_ct, respectively
fem_ct = df.gender.value_counts().Female
men_ct = df.gender.value_counts().Male


# In[10]:


# Bar chart of Female and Male counts in dataset
x = ['Female', 'Male']
y = [fem_ct, men_ct]
c = ['steelblue', 'seagreen']
plt.bar(x, height = y, color = c)
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()


# In[11]:


# Same bar chart as above but with Normalized Data
fem_ct = df.gender.value_counts(normalize=True).Female
men_ct = df.gender.value_counts(normalize=True).Male
x = ['Female', 'Male']
y = [fem_ct, men_ct]
c = ['steelblue', 'seagreen']
plt.bar(x, height = y, color = c)
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()


# In[12]:


# Display counts for Female and Male
print(fem_ct)
print(men_ct)


# In[13]:


# Calculate the difference in counts of Female and Male
2994-2115


# In[14]:


# 879 more Women included in dataset than men


# # Univariate analysis: Age

# In[15]:


# Use describe() to see min value of age column
df.describe()


# In[16]:


# Clean up age column, get rid of outliers
for index, row in df.iterrows():
    if row['age'] < 1.00:
        df.drop(index, inplace=True)
df


# In[17]:


# Turn age dtype to int
df = df.astype({'age': 'int64'})
df['age']


# In[18]:


# Prepare age data with value counts for plotting
age_ct_df = pd.DataFrame(df['age'].value_counts())
age_ct_df = age_ct_df.rename(columns={'age': 'count'})
age_ct_df


# In[19]:


# Scatter plot of age vs. count
plt.style.use('seaborn')
plt.scatter(age_ct_df.index, age_ct_df['count'])
plt.xlabel('Age')
plt.ylabel('Count')


# # Bivariate analysis: Gender vs. Stroke

# In[24]:


# Bar chart of gender vs. stroke with normalized values for gender counts
x,y = 'gender', 'stroke'
(df
.groupby(x)[y]
.value_counts(normalize=True)
.mul(100)
.rename('percent')
.reset_index()
.pipe((sns.catplot,'data'), x=x,y='percent',hue=y,kind='bar'))
plt.show()


# # Bivariate analysis: Age vs. Stroke

# In[25]:


# Scatterplot of age vs. count with color of point corresponding to stroke or no stroke
plt.style.use('seaborn')
stroke = df.loc[df['stroke'] == 1]
no_stroke = df.loc[df['stroke'] == 0]

stroke_age = pd.DataFrame(stroke.age.value_counts())
stroke_age = stroke_age.rename(columns={'age': 'count'})
no_stroke_age = pd.DataFrame(no_stroke.age.value_counts())
no_stroke_age = no_stroke_age.rename(columns={'age': 'count'})

plt.scatter(stroke_age.index, stroke_age['count'], color = 'steelblue')

plt.scatter(no_stroke_age.index, no_stroke_age['count'], color = 'seagreen')
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend(['Stroke', 'No stroke'])
plt.show()


# # Mulitvariate analysis: Gender vs. Age vs. Stroke

# In[26]:


# Scatterplots of age vs. count and color of points representing gender
fem_stroke = stroke.loc[stroke['gender'] == 'Female']
fem_no_stroke = no_stroke.loc[no_stroke['gender'] == 'Female']
men_stroke = stroke.loc[stroke['gender'] == 'Male']
men_no_stroke = no_stroke.loc[no_stroke['gender'] == 'Male']

fem_stroke
#Plot those w/ Stroke
fem_stroke_ct = pd.DataFrame(fem_stroke['age'].value_counts())
fem_stroke_ct = fem_stroke_ct.rename(columns={'age': 'count'})
plt.scatter(fem_stroke_ct.index, fem_stroke_ct['count'], c='steelblue')
men_stroke_ct = pd.DataFrame(men_stroke['age'].value_counts())
men_stroke_ct = men_stroke_ct.rename(columns={'age': 'count'})
plt.scatter(men_stroke_ct.index, men_stroke_ct['count'], c='seagreen')
plt.xlabel('Age w/ Stroke')
plt.ylabel('Count')
plt.legend(['Female', 'Male'])
plt.show()

#Plot those w/o Stroke
fem_no_stroke_ct = pd.DataFrame(fem_no_stroke['age'].value_counts())
fem_no_stroke_ct = fem_no_stroke_ct.rename(columns={'age': 'count'})
plt.scatter(fem_no_stroke_ct.index, fem_no_stroke_ct['count'], c='steelblue')
men_no_stroke_ct = pd.DataFrame(men_no_stroke['age'].value_counts())
men_no_stroke_ct = men_no_stroke_ct.rename(columns={'age': 'count'})
plt.scatter(men_no_stroke_ct.index, men_no_stroke_ct['count'], c='seagreen')
plt.xlabel('Age w/o Stroke')
plt.ylabel('Count')
plt.legend(['Female', 'Male'])
plt.show()


# In[ ]:




