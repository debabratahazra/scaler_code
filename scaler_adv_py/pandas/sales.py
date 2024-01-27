import pandas as pd

df = pd.read_csv('./scaler_adv_py/pandas/resources/sales.csv')


df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

df['Date'] = pd.to_datetime(df['InvoiceDate'].dt.date)
print(df)

ans = df[df['Date'] == pd.Timestamp('2011-06-22')]
print(ans)

print(ans['Customer ID'].nunique())

# sales
df['sales'] = df['Quantity'] * df['Price']
print(df)

# only France country
new_df = df.loc[df['Country'] == 'France']

# group by date abd calc the total sum for each date
df_france = new_df.groupby("Date")['sales'].sum().to_frame()

# sort the data frame
df_sort = df_france.sort_values(by='sales', axis=0, ascending=False)
print(df_sort.head(1))


# sorting based on Quantity column and group by Description columns
df = pd.read_csv('./scaler_adv_py/pandas/resources/sales.csv')
item_to_quantity_df = df.groupby('Description')['Quantity'].sum().to_frame()
item_to_quantity_df = item_to_quantity_df.sort_values(
    "Quantity", ascending=False)
print("Sorting of Quantities...")
print(item_to_quantity_df.head())
