import pandas as pd

df = pd.DataFrame({
    "Accessories": ["Laptop", "Laptop", "Ipad", "Ipad", "Tablet", "Laptop"],
    "customer": ["Andrew", "Andrew", "Tom", "Andrew", "Tobey", "Peter"],
    "quantity": [1, 2, 2, 3, 1, 2],
})

print(df)

''' Which of the given option(s) are the right method and syntax for pivoting the below-mentioned 
dataframe such that each customer would have a value that is the total quantity of a particular 
type of accessories he holds? '''

df = df.groupby(['Accessories', 'customer']).quantity.sum()
print(df)
