import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

print("Dataframe\n", df)

# Check if values 1 and 2 exist in the whole DataFrame
print("is in 1,2\n", df.isin([1, 2]))

# check in only A column
print("check in A\n", df.isin({'A': [1, 2, 5]}))

# checkin only B column
print("check in B\n", df.isin({'B': [4, 2, 9]}))
