# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn')


# %%
data = pd.read_csv('./healthcare-dataset-stroke-data.csv',sep = ',',header = 0) 


# %%
data.head(10)


# %%
data.shape


# %%
#check if data type is correct
data.info()


# %%
#check duplicated data
data.duplicated().sum()


# %%
#drop id column
data.drop('id', inplace=True, axis=1)


# %%
#check the variable in each column
for col in data.columns:
    print(data[col].value_counts())
    print("-"*15)


# %%
#replace the unknown in smoking status to it median values
data["smoking_status"].replace("Unknown", data["smoking_status"].mode().values[0], inplace=True)


# %%
#check if there is null in data
data.isnull().sum()


# %%
# Calculating the percentage of missing values in each column is often more meaningful to me
print('PERCENTAGE OF MISSING VALUES IN EACH COLUMN:\n')
for col in data.columns:
    missing = np.mean(data[col].isnull())
    print('{}:  {:.2f}%'.format(col, missing*100))


# %%
# Showing rows where values for bmi are missing
missing_bmi=data[pd.isnull(data.bmi)]
missing_bmi.head(5)


# %%
#replace null data with median
data["bmi"].fillna(data["bmi"].median(), inplace=True)


# %%
#describe the data
data.describe()


# %%
#add bmi status column (changing the bmi value to underweight,normal and overweight)
criteria = [data['bmi'].between(0, 18.5), data['bmi'].between(18.6, 24.9), data['bmi'].between(25, 100)]
values = ['underweight', 'normal', 'overweight']

data['bmi_status'] = np.select(criteria, values, 0)
data

# %% [markdown]
# # Univariate

# %%
#displaying data for bmi
sns.displot(data['bmi_status'])
plt.show()


# %%
#displaying data for smoking status

sns.displot(data['smoking_status'])
plt.show()

# %% [markdown]
# # Bivariate

# %%
# un normalized bivariate of stroke and bmi
fig, ax = plt.subplots(figsize=(8,8))
sns.countplot(hue='stroke',x='bmi_status',data=data)
plt.show()


# %%
#normalized plot for bmi and stroke
x,y = 'bmi_status', 'stroke'

(data
.groupby(x)[y]
.value_counts(normalize=True)
.mul(100)
.rename('percent')
.reset_index()
.pipe((sns.catplot,'data'), x=x,y='percent',hue=y,kind='bar'))
plt.show()


# %%
# un normalized plot for stroke and smoking status
fig, ax = plt.subplots(figsize=(8,8))
sns.countplot(hue='stroke',x='smoking_status',data=data)
plt.show()


# %%
#normalized plot for smoking & stroke
x,y = 'smoking_status', 'stroke'
(data
.groupby(x)[y]
.value_counts(normalize=True)
.mul(100)
.rename('percent')
.reset_index()
.pipe((sns.catplot,'data'), x=x,y='percent',hue=y,kind='bar'))
plt.show()

# %% [markdown]
# # Multivariate

# %%
#multivariate boxplot of stroke,smoking status and bmi
sns.boxplot(x="bmi",y="smoking_status",hue="stroke",data=data)
plt.show()


