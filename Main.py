from numbers import Number
import pandas as pd
from pandas.api.types import is_numeric_dtype
import matplotlib.pyplot as plt
data1 = pd.read_csv('.\data\Entrenamieto_ECI_2020.csv')
for i in data1.columns:
    if is_numeric_dtype(data1[i]):
        print(i, ' : ', type(data1[i][0]))


series_1 = data1[(data1['Total_Amount']/data1['Total_Amount'].max()) <= 0.2]['Total_Amount']
series_2 = series_1/series_1.max()


fig1 = plt.figure()
plt.hist(series_2, bins=200,range=(0,0.004))

for i in range(1,10):
    fig1.savefig(f'fig_{i}.png')









