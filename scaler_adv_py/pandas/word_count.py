import pandas as pd


def solve(string):
    """
    returns a series object with word count as values and words as the indices.
    """
    # store the frequency of the strings in a series
    freq = pd.Series(string.split())
    # print(freq)
    # sort the indices
    res = freq.value_counts()
    # print(res)

    res.sort_index(axis=0, ascending=True, inplace=True)
    return res


A = "How much wood would a woodchuck chuck if a woodchuck could chuck wood"
print(solve(A))
