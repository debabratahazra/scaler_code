import numpy as np
import pandas as pd
import os

print(os.getcwd())
df = pd.read_csv("./scaler_adv_py/pandas/tips.csv")
print(df.head())

print(df.loc[:, ['time', 'total_bill', 'tip']])
print(pd.DataFrame(df, columns=['time', 'total_bill', 'tip']))
print(df[['time', 'total_bill', 'tip']])
print(df.iloc[:, 0:2])  # not print all required columns

print("iloc :2, :2\n", df.iloc[:2, :2])
print("loc :2, total_bill:sex\n", df.loc[:2, "total_bill":"sex"])
#########
print(df.head())
print(df["sex"].unique())
print(df["sex"].nunique())
print(df.nunique())
###########
df = pd.read_csv("./scaler_adv_py/pandas/tips.csv")
print("head 10 lines:\n", df.head(10))
print("df.iloc 1-5,1-3\n", df.iloc[1:5, 1:3])

list_index = np.arange(len(df))
print("df index value:\n", df.index.values)
df.index = list_index

# not possible as colimn name 1:3 range name is not specified
# print("df.loc 1-5,1-3\n", df.loc[1:5, 1:3])

################################################################
print(df.head())
print(df.loc[:, 'tip'])
print()
print(df['total_bill'])
# this below code will not work
# print(df.iloc[:, 'tip'])
