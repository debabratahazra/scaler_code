import pandas as pd

'''
Using the below-given dataset, determine the average number of bookings in the year 2015.'''

# File: Listing_Dataset.xlsx

# Specify the path to the Excel file
file_path = "\C:\Users\Hazra\Desktop\DS\Python_github\scaler_code\product_matric\Listings_dataset.xlsx"


# Load the Excel file into a pandas DataFrame
df = pd.read_excel(file_path)

# Now you can work with the DataFrame to determine the average number of bookings in 2015

print(df.head())