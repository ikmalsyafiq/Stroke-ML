import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

"""
This code will run a script that gathers data from the 
Stroke data set. The data gathered is ever_married responses,
and work type. 

Univariate, Bivariate, and Multivariate graphs are created to 
help with any stroke correlation. 
"""

data = pd.read_csv('./healthcare-dataset-stroke-data.csv',sep = ',',header = 0) 

data.head(20)
plt.style.use('seaborn')
emwtdf = data[['ever_married', 'work_type', 'stroke']]

emwtdf

#Check to see if any data values are null
emwtdf.isnull().values.any()

#get frame shape : 5110 columns, 3 rows
emwtdf.shape

#get info of data, shows no-null data 
emwtdf.info()

#get ever_married grouping and count for yes/no
emgrp = data.groupby('ever_married').count()
emgrp

#---------------ever-married univariate--------------------------------
fig, ax = plt.subplots(figsize = (18, 5))
ax.barh(emgrp.index, emgrp.id, color=['lightsteelblue', 'peachpuff'],tick_label=emgrp.index)
ax.set_xlabel('Count')
ax.set_ylabel('Response')
plt.title('Ever Married?')

fig.show()

##---------------work_type univariate--------------------------------
wtgrp = data.groupby('work_type').count()
wtgrp
fig2, ax2 = plt.subplots(figsize = (18, 10))
ax2.barh(wtgrp.index, wtgrp.id, color=['gold', 'plum', 'palegreen', 'salmon', 'paleturquoise'],tick_label=wtgrp.index)
ax2.set_xlabel('Count')
ax2.set_ylabel('Work Type')
plt.title('Work Type')

fig2.show()
###----------ever-married-bivariate-----------------------------------

fig3, ax3 = plt.subplots(figsize = (22, 10))
#emS = sns.countplot(hue='stroke', y = 'ever_married', data=data, palette=['cornflowerblue', 'hotpink'])

x,y = 'ever_married', 'stroke'

(data
.groupby(x)[y]
.value_counts(normalize=True)
.mul(100)
.rename('percent')
.reset_index()
.pipe((sns.catplot,'data'), x=x,y='percent',hue=y,kind='bar'))
plt.show()

#plt.legend(loc='lower right')


####---------work_type bivariate-----------------------------------------------
fig, ax4 = plt.subplots(figsize = (27, 8))
#wtS = sns.countplot(hue='stroke', y = 'work_type', data=data, palette=['cornflowerblue', 'hotpink'])
x,y = 'work_type', 'stroke'

(data
.groupby(x)[y]
.value_counts(normalize=True)
.mul(100)
.rename('percent')
.reset_index()
.pipe((sns.catplot,'data'), x=x,y='percent',hue=y,kind='bar'))
plt.show()
#plt.legend(loc='lower right')


#####---------multivariate work_type/ever_married--------------------

new = data[["work_type", "stroke", "ever_married", "age"]]
new_df = new.copy()
new_df["combined"] = new_df['work_type'] + " " + new_df['ever_married'] + " " + new_df['stroke'].astype(str)

multi_dict = {}
list_a = []
for i in new_df["combined"]:
  list_a.append(i)

for i in list_a:
  multi_dict[i] = list_a.count(i)
  
fig2, ax3 = plt.subplots(figsize = (18, 10))

lists = sorted(multi_dict.items())
x,y = zip(*lists)

ax3.barh(x, y,tick_label=x)
ax3.set_xlabel('Number of Samples')
ax3.set_ylabel('Work_Type Ever_married? Stroke?')

ax3

