### Brief Introduction

A stroke is harmful damage to the brain. In order to explore the reason to cause the stroke, We analyze stroke condition on a dataset containing 5110 observations with 12 attributes. Our Objective is to provide a comprehensive exploratory data analysis (EDA) on the dataset. To be clear, we examine all of data from it and determine which factors lead to higher risk of stroke. The following is performed on the data:

* Univariate Analysis
* Bivariate Analysis
* Correlation Analysis

### Building Requirements

Our program requires an environment of Python 3.0+. Following main third-party libraries are used: 

* Pandas 0.23.4+ 

`pip install pandas==0.23.4`

* Seaborn 0.9.0+

`pip install seaborn==0.9.0`

* Matplotlib 2.2.3+

`pip install matplotlib==2.2.3`

* Numpy 1.15.1+

`pip install numpy==1.15.1`

Our dataset are directly downloaded from Kaggle: Stroke Prediction Dataset. Link: https://www.kaggle.com/fedesoriano/stroke-prediction-dataset

If you've already built up the environment containg all the required third-party libraries, simply run .py files in the EDA directory to get the output described and shown in the notebook. Note that different .py file is for different attribute analysis.

### File structure

* data: the directory containing the original .csv data file

* notebook: the directory containing the jupyter notebook with data visualizations used in presentation

* EDA: the directory containing the .py files realated to exploratory data analysis

## Data Pre-treatment

The stroke dataset requires some pre-treatment. Column "id" is deleted since it's useless. For missing data in the bmi attribute and unknown data in the smoking-status attribute, we just omit them. 

In order to get the correlation value for labeled attribute without numerical values. We define "0/1" values for the attribute with "Yes/No" properties. For example, we define "0" for "No" and "1" for "Yes" for "ever_married". We calculate the corresponding correlations according to these defined values.

## Plotting

Visualization is of great importance in our work. All visualizations used in our presentation are in the jupyter notebook in the notebook directory. Different attributes of data are plotted in different ways based on their own characteristics. For example, bar plot is applied for labeled data, histogram is applied for numerical data, and heatmap is applied for correlation data.

## Data Analysis

Data is analyzed by various methods, including Univariate Analysis and Bivariate Analysis. We try to find the insight connection between different factors with stroke. Detailed methods are shown in the EDA directory and presentation PPT.




