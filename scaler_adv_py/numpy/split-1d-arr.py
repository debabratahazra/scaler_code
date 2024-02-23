import numpy as np

'''
Given an 1D array and an integer k that specifies the number of equal parts to split the array into,

Perform the following operations:

Split the array into k number of equal parts.
Return the list of split arrays.
'''


def split(arr, k):
    '''
    INPUT: arr, k

    OUTPUT: split_arr -> list of arrays
    '''

    split_arr = np.split(arr, k)

    return split_arr


arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
k = 3
print(split(arr, k))
