import pandas as pd

data = {
    'name': ['a', 'b', 'c'],
    'age': [23, 12, 22]
}

df = pd.DataFrame(data)
print(df)

''' Problem Description:

Given a dataframe, a list of rows in the format of list of lists, and a number, "out".

Perform the following operations:

Append the rows from the list of lists to the dataframe
After appending, remove the row at the out position
Input Format:

A dataframe
A list of lists
A variable "out" '''


def add_and_remove(df, data, out):
    '''
    Input:
    df -> The dataframe passed as input
    data -> The list of list variable containg the rows to append
    out -> the variable containing the row index value to be removed

    Output:
    df -> return the dataframe df after doing the above operations
    '''

    # Add the rows
    for row in data:
        df.loc[len(df.index)] = row

    # Remove the out index row
    df = df.drop(out, axis=0)

    return df


data = [['d', 20], ['e', 21], ['f', 22]]
out = 4
print(add_and_remove(df, data, out))
