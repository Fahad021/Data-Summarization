#https://pandas.pydata.org/pandas-docs/stable/api.html#dataframe
#https://seaborn.pydata.org/index.html
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")


from pandas import set_option
df=pd.read_csv('E:\ECE 657A\winter 2019\homework\data.csv')

shape = df.shape
print(shape)

types = df.dtypes
print(types)

set_option('display.width', 100)
set_option('precision', 3)

description = df.describe()
print(description)

mode = df.mode()
print(mode)

variance= df.var()
print(variance)

skew=df.skew()
print(skew)

kurt=df.kurtosis()
print(kurt)

PCC= df.corr(method='pearson', min_periods=1)
print (PCC)


writer = pd.ExcelWriter('output.xlsx')
description.to_excel(writer,'Sheet1')
variance.to_excel(writer,'Sheet2')
skew.to_excel(writer,'Sheet3')
kurt.to_excel(writer,'Sheet4')
PCC.to_excel(writer,'Sheet5')
mode.to_excel(writer,'Sheet6')
writer.save()


sns.heatmap(PCC,center=0,cmap="YlGnBu")











