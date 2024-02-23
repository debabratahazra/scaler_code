import pandas as pd


data = {
    'city': ['Alaska', 'Texas', 'California', 'New York'],
    'area': [1723337, 695662, 423967, 783000],
    'population': [700000, 26448193, 38332521, 19651127]
}

df = pd.DataFrame(data)

# make city column as explicit index
df.set_index('city', inplace=True)

''' Problem Statement:

Given a dataframe containing area and population data, calculate the Population Density for each state.

The function should return a Series of population densities sorted in ascending order.

Note: Population Density is defined as population per unit area. '''

population_density = df['population'] / df['area']
# print(population_density)

population_density = population_density.sort_values(ascending=True)

print(population_density)
