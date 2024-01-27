import numpy as np

'''
Given an MxN 2D array (M >= 4),

Split the array column wise such that,

1st sub array contains the first 2 columns
2nd sub array contains the 3rd column
3rd sub array contains the rest of the columns
'''


def split(arr):
    '''
    INPUT: arr -> 2D array

    OUTPUT: subarrays -> list of 2D arrays
    '''

    subarrays = np.hsplit(arr, [2, 3])
    # CODE starts here

    return subarrays


'''
Expected output
[
array([[ 0,  1],
       [ 4,  5],
       [ 8,  9],
       [12, 13],
       [16, 17],
       [20, 21]]), 
array([[ 2],
       [ 6],
       [10],
       [14],
       [18],
       [22]]), 
array([[ 3],
       [ 7],
       [11],
       [15],
       [19],
       [23]])]
       
'''

arr = np.array([[0, 1, 2, 3],
                [4, 5, 6, 7],
                [8, 9, 10, 11],
                [12, 13, 14, 15],
                [16, 17, 18, 19],
                [20, 21, 22, 23]])

print(split(arr))
