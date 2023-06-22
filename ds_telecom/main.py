import matplotlib.pyplot as plt
import seaborn as sbn
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
import pathlib

csvFile = ""
for dirname, _, filenames in os.walk(pathlib.Path().resolve()):
    for filename in filenames:
        # print(os.path.join(dirname, filename))
        if filename == "telecom_customer_churn.csv":
            csvFile = os.path.join(dirname, filename)
# print(csvFile)

telecom = pd.read_csv(csvFile)
# print(telecom)
print(telecom.info())

print(telecom.groupby('Customer Status')['Monthly Charge'].describe())

print(telecom.describe().T)

print(telecom.groupby(['Customer Status', 'Gender'])
      ['Monthly Charge'].describe())

# Line chart
ax = sbn.lineplot(
    x='Tenure in Months', y='Monthly Charge', data=telecom)
ax.set(xlabel='Tenure', ylabel='Charge')
plt.title('Telecom graph')

plt.show()

# Bar chart
sbn.countplot(
    x='Customer Status', data=telecom)
plt.show()

# Here will show 25%, 50% and 75% box chart
sbn.boxplot(
    x='Customer Status', y='Monthly Charge', data=telecom)
plt.show()
