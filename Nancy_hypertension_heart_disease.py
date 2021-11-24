import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def univariate(df):
    grp = df.groupby('hypertension').count()
    plt.figure()
    plt.bar(grp.index, grp.id, color=['#666666','#CC9999'], tick_label=grp.index)
    plt.title('hypertension')
    plt.figure()
    grp = df.groupby('heart_disease').count()
    plt.bar(grp.index, grp.id, color=['#669999', '#CC9966'], tick_label=grp.index)
    plt.title('heart_disease')
    plt.show()

def bivariate(df):
    plt.figure()
    grp = df.groupby(['stroke','hypertension']).count()
    a = grp.loc[(0,0):(0,1)].id
    b = grp.loc[(1,0):(1,1)].id
    plt.bar([0,1],a, color=['#99CC99'], tick_label=[0,1],label='not stroke')
    plt.bar([0,1],b, color=['#154406'], bottom=a,tick_label=[0,1],label='stroke')
    plt.title('hypertension vs stroke')
    plt.xlabel('hypertension')
    plt.legend()

    plt.figure()
    grp = df.groupby(['stroke','heart_disease']).count()
    a = grp.loc[(0,0):(0,1)].id
    b = grp.loc[(1,0):(1,1)].id
    plt.bar([0,1],a,color=['#3399CC'],alpha=0.9, tick_label=[0,1],label='not stroke')
    plt.bar([0,1],b, color=['#003366'],alpha=0.8,dbottom=a,tick_label=[0,1],label='stroke')
    plt.title('heart_disease vs stroke')
    plt.xlabel('heart_disease')
    plt.legend()
    plt.show()

def multivariate(df):
    grp = df.groupby(['stroke', 'heart_disease', 'hypertension']).count()
    ax = plt.figure().add_subplot(projection='3d')
    width = depth = 0.5
    xs = np.array([0, 0, 1, 1]) - width / 2
    ys = np.array([0, 1, 0, 1]) - width / 2
    ax.bar3d(xs, ys, 0, width, depth, grp.loc[(0, 0, 0):(0, 1, 1)].id,
             label='not stroke', alpha=0.5, color='#FFFFCC')
    ax.bar3d(xs, ys, grp.loc[(0, 0, 0):(0, 1, 1)].id, width, depth, grp.loc[(1, 0, 0):(1, 1, 1)].id,
             label='stroke', alpha=0.5, color='#99CCCC')
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

