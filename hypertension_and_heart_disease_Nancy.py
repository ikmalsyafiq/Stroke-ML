import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def bivariate(df):
    """
    visualization of Hypertension and heart disease
    plot out the relation between hypertension and stroke, heart disease and stroke
    :param df: the dataset of stroke
    """
    # hypertension vs stroke
    plt.figure()
    grp = df.groupby(['stroke','hypertension']).count()
    a = list(grp.loc[(0,0):(0,1)].id)
    b = list(grp.loc[(1,0):(1,1)].id)
    plt.style.use('seaborn')
    bar_width = 0.35
    dist_1 = np.array([a[0], b[0]])/(a[0]+b[0])
    dist_2 = np.array([a[1], b[1]]) / (a[1] + b[1])
    a = [dist_1[0],dist_2[0]]
    b = [dist_1[1],dist_2[1]]
    index = np.arange(2)
    rects1 = plt.bar(index, a, bar_width, label='not stroke')
    rects2 = plt.bar(index + bar_width, b, bar_width, label='stroke')
    plt.xticks([bar_width/2,bar_width/2+1], ('not hypertension', 'hypertension'))
    plt.ylabel('rate', rotation=60)
    plt.title('hypertension vs stroke')
    plt.legend()
    # hear disease vs stroke
    plt.figure()
    grp = df.groupby(['stroke','heart_disease']).count()
    a = list(grp.loc[(0,0):(0,1)].id)
    b = list(grp.loc[(1,0):(1,1)].id)
    dist_1 = np.array([a[0], b[0]]) / (a[0] + b[0])
    dist_2 = np.array([a[1], b[1]]) / (a[1] + b[1])
    a = [dist_1[0], dist_2[0]]
    b = [dist_1[1], dist_2[1]]
    index = np.arange(2)
    rects1 = plt.bar(index, a, bar_width, label='not stroke')
    rects2 = plt.bar(index + bar_width, b, bar_width, label='stroke')
    plt.xticks([bar_width / 2, bar_width / 2 + 1], ('not heart_disease', 'heart_disease'))
    plt.ylabel('rate', rotation=60)
    plt.title('heart_disease vs stroke')
    plt.legend()
    plt.show()


def age_vs_health(df):
    """
    find the relationship between age, hypertension and heart disease
    :param df: the dataset of stroke
    """
    plt.figure(figsize=(5, 5))
    sns.set_theme(style="darkgrid")
    sns.swarmplot(x="stroke", y="age", hue="hypertension", data=df, palette="PRGn")
    plt.figure(figsize=(5, 5))
    sns.set_theme(style="darkgrid")
    sns.swarmplot(x="stroke", y="age", hue="heart_disease", data=df, palette="PRGn")
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv('healthcare-dataset-stroke-data.csv')
    bivariate(df)
    age_vs_health(df)