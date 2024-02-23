import pandas as pd

data = {
    'name': ['Elon', 'Jeff', 'Bill', 'Falguni'],
    'gender': ['M', 'F', 'M', 'F'],
    'income': [53000, 28000, 25000, 44000]
}

df = pd.DataFrame(data)
print(df)

income = df["income"]
print("income\n", income)
max_income = income.max()

max_income_details = df[df["income"] == max_income]
print("max income details\n", max_income_details)

# extract string value from data frame
print("Max income name\n",
      max_income_details["name"].loc[max_income_details.index[0]])
