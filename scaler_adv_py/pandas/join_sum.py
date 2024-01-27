import pandas as pd

data = {
    'cust_id': [101, 102, 103, 104],
    'name': ['rick', 'morty', 'pickle', 'jerry']
}

customer = pd.DataFrame(data)
print("customer table\n", customer)

data = {
    'order_id': ['OR1', 'OR3', 'OR23', 'OR42'],
    'cust_id': [102, 105, 101, 102],
    'amount': [1200, 650, 120, 989]
}

orders = pd.DataFrame(data)
print("order table\n", orders)

''' Problem Statement:

Given two dataframes customer (containing details of customer) and orders (having details of orders).

Also, name is given which is a customer's name.

Perform the following operation:

Merge the dataframe such that the resultant dataframe should contain records of all customer ids present in customer dataframe.

Calculate the total order amount for given customer name

Return the merged dataframe and the sum amount.'''


# left join the table
merge_cust = customer.merge(orders, on="cust_id", how="left")
print("left merge table\n", merge_cust)

# sum amount for given customer - morty
name = "morty"
name_merge_cust = merge_cust[merge_cust["name"] == name]
total = name_merge_cust["amount"].sum()
print(total)
