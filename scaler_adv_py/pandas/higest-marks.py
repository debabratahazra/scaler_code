import pandas as pd

data = {
    'roll_no': [1, 2, 1, 3, 1, 3, 3, 3, 2, 2, 1, 2],
    'subject': ['NN', 'DL', 'ML', 'Prob', 'DL', 'ML', 'DL', 'NN', 'NN', 'Prob', 'Prob', 'ML'],
    'marks': [97, 63, 63, 71, 64, 90, 66, 46, 74, 62, 94, 67]
}

df = pd.DataFrame(data)
print(df)

''' Problem Statement:

Given a dataframe containing student's marks for multiple subjects,

Return a dataframe which contains records of subject-wise highest marks along with their roll number.
'''


def get_marks(df):
    '''
    INPUT: df -> dataframe

    OUTPUT: result -> dataframe
    '''

    # STEP 1: group the df using subject and get max marks

    max_marks = df.groupby('subject')['marks'].max()
    print("Max marks based on subjects: ")
    print(max_marks)

    # STEP 2: reset the index

    max_marks = max_marks.reset_index()
    print("After reset index")
    print(max_marks)

    # STEP 3: merge with original df to get roll id
    # inner join with two columns ON condition
    result = max_marks.merge(df, on=['subject', 'marks'])

    return result


print(get_marks(df))
