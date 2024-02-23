import numpy as np

'''
TODO:
Find the matrix multiplication of the given two matrices and
Extract the elements from the output of above step using the given ranges
If matrix multiplication is not possible, return -1
'''


def specific_elements(mat1, mat2, r1, r2, c1, c2):
    '''mat1,mat2 are the two 2d numpy array.
       r1,r2 are the start and end of rows indices
       c1,c2 are the start and end of columns indices
       Output = Return a numpy array according to indices'''

    # STEP1 CHECK whether matrix multiplication is possible
    m_shape = mat1.shape
    n_shape = mat2.shape
    if not (len(m_shape) == 2 and len(n_shape) == 2 and m_shape[1] == n_shape[0]):
        # matrix multiplication not possible
        return -1

    # STEP 2 Perform matrix multiplication

    matmul_array = mat1@mat2

    # STEP 3 slice the array based on range value

    result = matmul_array[r1:r2, c1:c2]

    return result


mat1 = np.array([[6, 6, 4, 7, 9],
                 [0, 2, 2, 9, 3],
                 [6, 0, 2, 5, 2],
                 [2, 4, 3, 5, 5]])

mat2 = np.array([[8, 6, 6, 8, 3],
                 [2, 7, 0, 3, 1],
                 [3, 2, 1, 5, 2],
                 [7, 0, 7, 6, 8],
                 [1, 5, 6, 4, 5]])

r1 = 1
r2 = 3
c1 = 2
c2 = 4

print(specific_elements(mat1, mat2, r1, r2, c1, c2))
