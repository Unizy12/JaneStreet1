from main import Process
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('E:/Janestreet_data/train.csv', usecols=['date','weight','resp'])
df = pd.DataFrame()
for p in np.arange(0,0.005,0.001):
    ProcessedData = Process(data).pDist(p)
    df = df.append(ProcessedData,ignore_index=True)
df = df.set_index(['p'])
df[[c for c in df.columns if 'count' in c]].plot.bar(rot=0)
plt.show()
df[[c for c in df.columns if 'respmean' in c]].plot(style='o')
plt.show()