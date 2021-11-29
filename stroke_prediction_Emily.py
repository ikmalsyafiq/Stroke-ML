#!/usr/bin/env python
# coding: utf-8


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


'''
This file contains code for EDA on gender, age and stroke columns of the
dataset. Specifically, univariate, bivariate, and multivariate analyses for
each feature and combination of features.
'''

# Load dataset
data = pd.read_csv('./healthcare-dataset-stroke-data.csv',sep = ',',header = 0) 

# See first 10 rows of dataframe
data.head(10)

# Make Dataframe copy with all columns I'm looking at
df = data[['gender', 'age', 'stroke']].copy()

#Check for null values in this dataframe
df.isnull().values.any()


#--------------------------Univariate Analysis: Gender-------------------------


# Look at unique values in gender column
df.gender.value_counts()

#Get rid of outlier
df = df[df.gender != 'Other']

# Check unique values in gender column again
df.gender.value_counts()

# Store counts for Female and Male in gender column in fem_ct and men_ct
fem_ct = df.gender.value_counts().Female
men_ct = df.gender.value_counts().Male

# Bar chart of Female and Male counts in dataset
x = ['Female', 'Male']
y = [fem_ct, men_ct]
c = ['steelblue', 'seagreen']
plt.bar(x, height = y, color = c)
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

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

# Display counts for Female and Male
print(fem_ct)
print(men_ct)

# Calculate the difference in counts of Female and Male
x = fem_ct - men_ct
print(x)
# 879 more Women included in dataset than men


#-------------------Univariate analysis: Age-----------------------------------

# Use describe() to see min value of age column
df.describe()

# Clean up age column, get rid of outliers
for index, row in df.iterrows():
    if row['age'] < 1.00:
        df.drop(index, inplace=True)

# Turn age dtype to int
df = df.astype({'age': 'int64'})
df['age']

# Prepare age data with value counts for plotting
age_ct_df = pd.DataFrame(df['age'].value_counts())
age_ct_df = age_ct_df.rename(columns={'age': 'count'})
age_ct_df

# Scatter plot of age vs. count
plt.style.use('seaborn')
plt.scatter(age_ct_df.index, age_ct_df['count'])
plt.xlabel('Age')
plt.ylabel('Count')


#-------------------Bivariate analysis: Gender vs. Stroke----------------------

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


#------------------Bivariate analysis: Age vs. Stroke--------------------------

# Scatterplot of age vs. count with color of pt meaning stroke or no stroke
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


#------------Mulitvariate analysis: Gender vs. Age vs. Stroke------------------

# Scatterplots of age vs. count and color of points representing gender
fem_stroke = stroke.loc[stroke['gender'] == 'Female']
fem_no_stroke = no_stroke.loc[no_stroke['gender'] == 'Female']
men_stroke = stroke.loc[stroke['gender'] == 'Male']
men_no_stroke = no_stroke.loc[no_stroke['gender'] == 'Male']

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
