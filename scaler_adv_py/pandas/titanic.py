import numpy as np
import pandas as pd

df = pd.read_csv("./scaler_adv_py/pandas/titanic.csv")
print("head\n", df.head())

titanic = df
o0 = titanic.T
print("o0\n", o0)
print()

o1 = titanic.T.drop_duplicates(keep="first")
print("o1\n", o1)
print()

o2 = titanic.drop_duplicates(keep="first")
print("o2\n", o2)
print()

o3 = titanic.drop_duplicates(keep="last")
print("o3\n", o3)

####################################
# filter out and show only male whose age is between 23 and 30

df = pd.read_csv("./scaler_adv_py/pandas/titanic.csv")
print("head -10\n", df.head(10))

male_df = df[df['sex'] == 'male']
print("male df\n", male_df)

age_male_df = male_df[(male_df['age'] >= 23.0) & (male_df['age'] <= 30.0)]
print("filter male 23-30\n", age_male_df)
####################

df = pd.read_csv("./scaler_adv_py/pandas/titanic.csv")
print("head -10\n", df.head())
# survived -> 1 and gender Male/Female ?
survive = df.loc[df['survived'] == 1]
print(survive['gender'].value_counts())

# age 20-40
age = df.loc[(df['age'] >= 20) & (df['age'] <= 40)]
print(age['sex'].value_counts())
print(df['sex'].value_counts())
