import numpy as np

''' Given a NumPy array of shape (n,m). Add padding of a layer of 0 s on all 4 boundaries 
of the matrix.
'''


def add_padding(mat):
    '''mat-> NumPy array
       output-> NumPy array is expected to be returned'''

    # YOUR CODE GOES HERE

    # Step 1: vstack with padding 0 on top and down
    zero_arr = np.zeros(mat.shape[1], dtype=np.int8)
    print(zero_arr)
    mat_vstack = np.vstack((zero_arr, mat, zero_arr))
    print(mat_vstack)

    # Step 2: hstack with padding 0 on left and right
    zero_arr = np.zeros(mat.shape[0]+2, dtype=np.int8).reshape(-1, 1)
    print(zero_arr)
    mat_hstack = np.hstack((zero_arr, mat_vstack, zero_arr))
    print(mat_hstack)

    res = mat_hstack

    return res


''' 
Expected output
[[0 0 0 0]
 [0 1 2 0]
 [0 3 4 0]
 [0 5 6 0]
 [0 0 0 0]]
 
 '''

mat = np.arange(1, 7).reshape(3, 2)
print(mat)

print(add_padding(mat))
