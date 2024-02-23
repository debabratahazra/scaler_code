import pandas as pd

''' As an educational institute, you need to keep a track of all the registered students.

Here you're given the registration IDs and the corresponding dates of a batch of students.

You need to return a DataFrame containing the columns as follows:

RID: Id of the student
RDate: Date of joining of the student
RMonth: Month of joining of the student
RYear: Year of joining of the student
RDay: Day of joining of the student '''


def solve(reg_id, reg_dates):
    res_df = pd.DataFrame(zip(reg_id, reg_dates), columns=["RID", "RDate"])
    """
    input:
    reg_id -> id of the input dataframe
    reg_dates -> dates of the input dataframe
    res_df -> the input dataframe

    output:
    return the resultant dataframe after performing the required operation
    """
    # YOUR CODE GOES HERE
    res_df['RDate'] = pd.to_datetime(res_df['RDate'])

    # create month column
    res_df['RMonth'] = res_df['RDate'].dt.month
    # create year column
    res_df['RYear'] = res_df['RDate'].dt.year
    # create day column
    res_df['RDay'] = res_df['RDate'].dt.day

    return res_df


reg_id = [56, 92, 29, 93, 55, 32]
reg_dates = ['2021-01-01', '2021-02-12', '2021-04-16',
             '2021-01-22', '2021-01-15', '2021-02-26']
print(solve(reg_id, reg_dates))
