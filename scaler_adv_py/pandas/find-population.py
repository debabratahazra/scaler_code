import pandas as pd

data = {
    'Country': ['Afghanistan', 'Australia', 'Brazil', 'China', 'France', 'India', 'United States'],
    'Year':  [1952, 1957, 1962, 1957, 1957, 1952, 1957],
    'Population':  [8425333.0, 9712569.0, 76039390.0, 637408000.0, 44310863.0, 372000000.0,  171984000.0],
    'Continent':  ['Asia', 'Oceania', 'Americas', 'Asia', 'Europe', 'Asia', 'Americas']
}

df = pd.DataFrame(data)
print(df)

''' Given dataframe consists of the following information about different countries :

The population,
The year it was measured, and
The continent it belongs to.
Complete the function population_df() to return a dataframe consisting of records 
where the population is greater than 10 million.

The dataframe should be sorted in ascending order, first by year and then by population column. '''

# filter by population column with >= 10 million
df = df[df['Population'] >= 10000000]

# sorting
df = df.sort_values(['Year', 'Population'])
print(df)

# reset index
df = df.reset_index(drop=True)
print(df)
