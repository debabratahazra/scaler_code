import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

protein = [4, 3, 4, 4, 2, 2, 2, 3, 2, 3, 1, 6, 1, 3, 1, 2, 2, 1, 1, 3, 3, 2, 2, 2, 2, 1, 3, 3, 3, 1, 2, 1, 3, 3, 3, 1, 3,
           1, 2, 3, 2, 4, 2, 4, 4, 4, 3, 2, 2, 3, 3, 3, 3, 3, 1, 2, 4, 5, 3, 3, 2, 1, 2, 2, 3, 3, 2, 6, 2, 2, 3, 3, 2, 1, 3, 3, 2]
print("protein\n", protein)

'''Given a list consisting of data about the amount of protein in different cereals i.e. list[i] represents the amount of protein in ith cereal.

Interpret the number of cereals for different amounts of protein available in any cereal using a bar graph.

The label of the x-axis should be "Protein amount in grams".
The label of the y-axis should be "Number of cereals".
The title should be "Protein comparison".
The color of the bars should be green 'g'.
Note: The output is verified by using the attributes of the created plot like labels and all the requirements that are mentioned above.
No need to show() the plot. Here the backend will automatically print the heights of the first and last bars of the created bar plot and the string representing your solution's status.'''

x, y = np.unique(protein, return_counts=True)
print("x\n", x)
print("Y\n", y)


fig = plt.figure()

# Create the bar plot
plt.bar(x, y, color='g')

# Add the xlabel
plt.xlabel('Protein amount in grams')

# Add the ylabel
plt.ylabel('Number of cereals')

# Add the title
plt.title('Protein comparison')

plt.show()


#########################

'''Given a dataframe consisting of the data on sales of specific 'Product Type' with 'Month' and 'Selling Price' columns.

Write a program using boxplot() to visualize the selling price distribution for the products in different months where the plots should be colored according to their 'Product Type'.

The plot should have the following attributes:

x-axis labelled "Month"
y-axis labelled "Selling Price"
Input Format:

3 lists which are then combined to form a Dataframe.'''


typ = ['Tablet', 'Desktop', 'Desktop', 'Tablet', 'Laptop']
mnth = ['August', 'September', 'October', 'August', 'December']
prc = [2434, 43543, 85654, 34543, 67768]
df = pd.DataFrame({'Product Type': typ, 'Month': mnth, 'Selling Price': prc})
print(df.head())

# Plot the boxplot in bp
bp = sns.boxplot(data=df, x='Month', y='Selling Price', hue="Product Type")
plt.show()


#############

''' Given a dataframe, create a lineplot using seaborn to visualize the "Profit" against "Selling Price".

The lineplot must meet the following requirements:

1. The x-axis label should be "Selling Price"
2. The y-axis label should be "Profit"
3. The color of the lineplot should be "red" '''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
b = [479.99, 1249.99, 649.99, 399.99, 699.99, 1249.99, 1349.99, 999.99, 649.99, 479.99,
     1349.99, 1249.99, 649.99, 649.99, 999.99, 399.99, 699.99, 999.99, 399.99, 649.99]
c = [143.39, 230.89, 118.64, 72.09, 98.09, 230.89, 180.34, 146.69, 122.34, 143.39,
     180.34, 230.89, 122.34, 118.64, 146.69, 72.09, 98.09, 146.69, 72.09, 122.34]

df = pd.DataFrame({'Sale ID': a, 'Selling Price': b, 'Profit': c})

# Create the lineplot in lp
lp = sns.lineplot(color='red', x=df['Selling Price'], y=df['Profit'])
plt.show()


############
'''Given a dataframe consisting of the sales data of different product types.

Write a program to plot a violin plot where the distribution of sales of specific products can be visualized according to the ages of customers.

Also, visualize the distribution of males and females in different colors with the distribution of males ages on the left side and females on the right of an axis for each product.

x-axis: Product Type
y-axis: Age
hue: Gender
Note: The output will be verified with the attribute labels and legend of the created plot. '''

typ = ['Tablet', 'Desktop', 'Desktop', 'Tablet', 'Laptop']
g = ['M', 'F', 'M', 'M', 'F']
age = [23, 34, 12, 55, 35]
df = pd.DataFrame({'Product Type': typ, 'Gender': g, 'Age': age})
print(df.head())

sns.violinplot(x='Product Type', y='Age', data=df, hue="Gender")
plt.show()


########################
'''Given a dataframe consisting of sales data, with columns "Sale ID", "Source" and "Profit", find out which advertisement source is responsible for how much of the sales. Create a Bar plot to find relation between Advertisement Source and Profit.

x-axis should be "Source"
y-axis should be "Profit"
The output will be verified with the above attributes.'''

# syntax:
# sns.barplot(x='Source', y='Profit', estimator=np.sum, data=df)
##############################
