import pandas as pd

df = pd.read_csv("./scaler_adv_py/pandas/titanic.csv")
print("before \n", df)
for x in df.columns:
    if df[x].nunique() == 1:
        df.drop(x, axis=1, inplace=True)
print("after \n", df)


##########################

data = {
    'name': ['Jim', 'Clarke', 'Kent', 'Mark'],
    'username': ['itsjimhere', 'clark002', 'itskentment', 'markyoumustknow'],
    'userid': [20, 10, 86, 21]
}

df = pd.DataFrame(data)
print("data frame:\n", df)

''' In the above-given dataframe, usernames are the display names of the learner's accounts shown on a video-conferencing app when taking classes.

The instructor clearly said to the learners that usernames must contain the real name (name) of the learners.

We tried to print the userid of the learners who haven't followed the instruction: '''


def check(name, username):
    return name.lower() in username


new_df = df[~(df.apply(lambda x:check(
    x['name'], x['username']), axis=1))]['userid']
print("Update Table:")
print(new_df)
#########################
'''Problem Description:

Given a dataset about salesperson and customer orders, the task is to group the data as per salesman_id and customer_id, and return a new dataframe with the ord_no count for each salesman_id and customer_id pair.'''

data = {
    'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013],
    'purch_amt': [150.50, 270.65, 65.26, 110.50, 948.50, 2400.60, 5760.00, 1983.43, 2480.40, 250.45, 75.29, 3045.60],
    'ord_date': ['2012-10-05', '2012-09-10', '2012-10-05', '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
    'customer_id': [3005, 3001, 3002, 3009, 3005, 3007, 3002, 3004, 3009, 3008, 3003, 3002],
    'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]
}

df = pd.DataFrame(data)
print(df.head())


def group_the_data(df):
    '''
    input:
    df -> the dataframe provided to the function

    output:
    result -> the grouped by data as per required in the question
    '''
    result = None

    # Your Code Starts here
    count_df = df.groupby(['salesman_id', 'customer_id'])['ord_no'].count()
    # print(count_df)

    result = count_df.reset_index()

    # Your Code ends here
    return result


print(group_the_data(df))

######
'''Problem Description:

Given a dataframe containing records of some college students, with columns "Name", "Age", "Percentage" and "Stream".

Return the name of the students belonging to either Commerce or Arts Stream and with a Percentage greater than or equal to 75.'''


data = {
    'Name': ['Himanshu', 'Robert', 'Karie', 'Rohan', 'John'],
    'Age': [15, 14, 15, 16, 17],
    'Percentage': [80, 77, 83, 45, 70],
    'Stream': ['Commerce', 'Science', 'Arts', 'Commerce', 'Science']
}

df = pd.DataFrame(data)
print(df.head())

df_new = df.loc[((df['Stream'] == 'Arts') | (
    df['Stream'] == 'Commerce')) & (df['Percentage'] >= 75)]
print(df_new['Name'])
