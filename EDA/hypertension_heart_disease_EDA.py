import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def univariate(df):
    grp = df.groupby('hypertension').count()
    plt.style.use('seaborn')
    plt.figure()
    # plt.bar(grp.index, grp.id, tick_label=grp.index)
    # plt.xticks(np.arange(2), ('no hypertension', 'hypertension'))
    # plt.ylabel('count', rotation=60)
    plt.pie(grp.id, labels=['no hypertension','hypertension'], autopct='%3.f%%',explode=[0.1,0],shadow=True)
    # plt.pie(grp.id, autopct='%3.f%%', explode=[0.1, 0], shadow=True)
    plt.legend()
    plt.title('hypertension')

    plt.figure()
    grp = df.groupby('heart_disease').count()
    # plt.bar(grp.index, grp.id, tick_label=grp.index)
    # plt.xticks(np.arange(2), ('no heart_disease', 'heart_disease'))
    # plt.ylabel('count', rotation=60)
    plt.pie(grp.id, labels=['no heart_disease', 'heart_disease'], autopct='%3.f%%', explode=[0.1, 0], shadow=True)
    plt.legend()
    plt.title('heart_disease')
    plt.show()

def bivariate(df):
    plt.figure()
    grp = df.groupby(['stroke','hypertension']).count()
    a = list(grp.loc[(0,0):(0,1)].id)
    b = list(grp.loc[(1,0):(1,1)].id)
    plt.style.use('seaborn')
    # plt.bar([0,1],a,tick_label=[0,1],label='not stroke')
    # plt.bar([0,1],b, bottom=a,tick_label=[0,1],label='stroke')
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

    plt.figure()
    grp = df.groupby(['stroke','heart_disease']).count()
    # a = grp.loc[(0,0):(0,1)].id
    # b = grp.loc[(1,0):(1,1)].id
    a = list(grp.loc[(0,0):(0,1)].id)
    b = list(grp.loc[(1,0):(1,1)].id)
    # plt.bar([0,1],a,tick_label=[0,1],label='not stroke')
    # plt.bar([0,1],b, bottom=a,tick_label=[0,1],label='stroke')

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

def multivariate(df):
    plt.style.use('seaborn')
    grp = df.groupby(['stroke', 'heart_disease', 'hypertension']).count()
    ax = plt.figure().add_subplot(projection='3d')
    width = depth = 0.5
    xs = np.array([0, 0, 1, 1]) - width / 2
    ys = np.array([0, 1, 0, 1]) - width / 2
    a = list(grp.loc[(0, 0, 0):(0, 1, 1)].id)
    b = list(grp.loc[(1, 0, 0):(1, 1, 1)].id)
    print(a)
    print(b)
    aa = []
    bb = []
    for i in range(len(a)):
        aa.append(a[i]/(a[i]+b[i]))
        bb.append(b[i] / (a[i] + b[i]))

    ax.bar3d(xs, ys, 0, width, depth, aa,
             label='not stroke', alpha=0.8, color='#FFFFCC')
    ax.bar3d(xs, ys, aa, width, depth, bb,
             label='stroke', alpha=0.8, color='#99CCCC')
    # ax.legend()
    ax.set_xlabel('heart_disease')
    ax.set_ylabel('hypertension')
    ax.set_zlabel('number of stroke or not stroke')
    ax.set_yticks([0, 1])
    ax.set_xticks([0, 1])
    ax.view_init(elev=20., azim=-35)
    ax.set_title("multivariate")
    plt.show()

if __name__ == '__main__':
    '''
    Only one graph of these three functions can appear at the one time,
    because plt.show() can be blocked by previous plt.show()
    '''
    df = pd.read_csv('healthcare-dataset-stroke-data.csv')
    univariate(df)
    bivariate(df)
    multivariate(df)

# analyze for hypertension and age vs stroke
plt.figure(figsize=(5,5))
sns.set_theme(style="darkgrid")
sns.swarmplot(x="stroke", y="age",hue="hypertension", data=df, palette="PRGn")
# analyze for heart disease and age vs stroke
plt.figure(figsize=(5,5))
sns.set_theme(style="darkgrid")
sns.swarmplot(x="stroke", y="age",hue="heart_disease", data=df, palette="PRGn")
plt.show()




