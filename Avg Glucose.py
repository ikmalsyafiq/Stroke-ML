import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
plt.style.use('seaborn')

data = pd.read_csv('./healthcare-dataset-stroke-data.csv',sep = ',',header = 0)
data.drop('id', inplace=True, axis=1)

# Below is the data correlation part.
# data.corr()
sns.heatmap(data.corr(),cmap='Dark2_r',annot=True)
plt.title("Correlation")
#plt.show()
#Change other columns to numeric data
Another_data = data.copy()
Another_data['gender'] = np.where((Another_data['gender'] == "Female"), 1, 0)
Another_data['ever_married'] = np.where((Another_data['ever_married'] == "Yes"), 1, 0)
Another_data['Residence_type'] = np.where((Another_data['Residence_type'] == "Urban"), 1, 0)
Another_data['work_type'] = Another_data['work_type'].factorize()[0]
Another_data['smoking_status'] = Another_data['smoking_status'].factorize()[0]
#Another_data.head(20)
plt.figure(figsize=(9,9))
sns.heatmap(Another_data.corr(),annot=True, linewidths=0.1)
plt.title("Expanded Correlation")
#plt.show()

# Below is the Avg_glucose_level Analysis part
fig, ax= plt.subplots(figsize=(9,7))
sns.histplot(x="avg_glucose_level",hue = "stroke", data=data, ax=ax)
plt.xlabel("Avg_glucose_level")
plt.ylabel("Count")
#plt.legend(loc='upper right', title='Residence_type:', labels=['Urban','Rural'])
#plt.show()


#add bmi status column (changing the bmi value to underweight,normal and overweight)
criteria_glucose = [data['avg_glucose_level'].between(0, 70), data['avg_glucose_level'].between(70.0001, 140), data['avg_glucose_level'].between(140.0001, 3000)]
values = ['low', 'normal', 'high']
data['glucose_level_status'] = np.select(criteria_glucose, values, 0)

#normalized plot for bmi and stroke
x,y = 'glucose_level_status', 'stroke'

data.groupby(x)[y].value_counts(normalize=True).mul(100).rename('percent').reset_index().pipe((sns.catplot,'data'), x=x, y='percent', hue=y, kind='bar')
plt.show()