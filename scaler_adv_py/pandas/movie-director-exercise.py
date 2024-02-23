import pandas as pd
import numpy as np


# Load data set from csv file
movies = pd.read_csv("./scaler_adv_py/pandas/resources/movies.csv")
print("movies:\n", movies.head())
directors = pd.read_csv("./scaler_adv_py/pandas/resources/directors.csv")
print("directors:\n", directors.head())

# remove un-necessary column
movies.drop(columns='Unnamed: 0', inplace=True)
print("movies after remove un-necessary column :\n", movies.head())
directors.drop(columns='Unnamed: 0', inplace=True)
print("directors after remove un-necessary column:\n", directors.head())

# Join two tables together (left join) and assign in 'data' data-frame
data = movies.merge(directors, how="left",
                    left_on="director_id", right_on="id")
print("merged two tables:\n", data.head())
print("merge data info:")
print(data.info())

# After join remove redundant column id_y as director_id and id_y have same info
data.drop(columns=['id_y'], inplace=True)
print("After remove id_y column:")
print(data.info())

# rename id_x to id in merge table
data.rename({'id_x': 'id'}, axis=1, inplace=True)
print("after rename id_x column to id: ")
print(data.info())

print("merge data set:")
print(data.head())

print("Data set numerical statistics:")
print(data.describe())

# convert budget and revenue column in million unit to read data easy
data['revenue'] = (data['revenue'] / 1000000).round(2)
data['budget'] = (data['budget'] / 1000000).round(2)
print("After redound figure revenue and budget columns:")
print(data.head())

# filter data: show data whose vote_average is higher than 7
vote_avg_7 = data.loc[data['vote_average'] > 7]
print("Vote average more than 7 votes:")
print(vote_avg_7[['id', 'vote_average']])

# isin operator: show T/F based on match the value from list of data and return True or False
isData = data['year'].isin([2012, 2015, 2016])
print("Year in year:\n", isData)

# Ques: display the title and direct_name where vote_average > 7
print("Display title and direct_name where vote_average >7")
print(data[['title', 'director_name']].loc[data['vote_average'] > 7])
# or
# filter on row and column as well
# here. Before comma it's row filter condition and after comma it's column filter condition
print(data.loc[data['vote_average'] > 7, ['title', 'director_name']])


# Ques, whose vote_average is >7 and release in or post 2015
print("Whose vote average >7 and release in or post 2015")
print(data.loc[(data['vote_average'] > 7) & (data['year'] >= 2015), :])

# Ques: show details who is release on Fri or Sat
print("Release on Friday or Saturday")
print(data.loc[(data['day'] == "Friday") | (data['day'] == 'Saturday'), :])
# or
print("using isin function:")
print(data.loc[data['day'].isin(['Friday', 'Saturday'])])
# print(data[:, data.isin({'day': ['Friday', 'Saturday']})])


# Ques: Encode the Male -> 0 and Female/NaN -> 1 in the 'gender' column
def encode_gender(gender):
    if gender == "Male":
        return 0
    else:
        return 1


print("Before gender encode apply:")
print(data.head())
print("After gender encode apply:")
data['gender'] = data['gender'].apply(encode_gender)
print(data.head())

# apply numpy sum function on 'revenue' and 'budget' columns
data_sum = data[['revenue', 'budget']].apply(np.sum, axis=0)
print("column wise sum:")
print(data_sum)

# To do the same as above for each row
data_sum = data[['revenue', 'budget']].apply(np.sum, axis=1)
print("row wise sum:")
print(data_sum.head())


# Ques: find the Profit based on budget and revenue
def calc_profit(df):
    profit = df['revenue'] - df['budget']
    return profit


data['profit'] = data[['revenue', 'budget']].apply(calc_profit, axis=1)
print("Profit column added:")
print(data.head())


# ###################
# # GROUP BY
print("Movies Data Frame:\n", data)
print(data.columns)

# group by director name
print("Total group number:\n", data.groupby('director_name').ngroups)
print("Total group names:\n", data.groupby('director_name').groups)

# get specific director name from group
print("Specific group data:\n", data.groupby(
    'director_name').get_group("Adam McKay"))
