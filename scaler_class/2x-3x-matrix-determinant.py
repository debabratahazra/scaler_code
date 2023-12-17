# https://www.scaler.com/academy/mentee-dashboard/class/159479/homework/problems/11488?navref=cl_tt_nv

# find the determinant of 2x2 or 3x3 matrix

class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        print("Matrix length: ", len(A))
        if len(A) == 2:
            # 2x2 matrix
            det = (A[0][0] * A[1][1]) - (A[1][0] * A[0][1])
            return det

        elif len(A) == 3:
            # 3x3 matrix
            a = A[0][0] * (A[1][1] * A[2][2] - A[1][2]*A[2][1])
            b = A[0][1] * (A[1][0] * A[2][2] - A[1][2]*A[2][0])
            c = A[0][2] * (A[1][0] * A[2][1] - A[1][1]*A[2][0])
            det = a - b + c
            return det


s = Solution()
A = [
    [1, 2],
    [3, 4]
]

print(s.solve(A))

B = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(s.solve(B))

C = [
    [6, 1, 1],
    [4, -2, 5],
    [2, 8, 7]
]
print(s.solve(C))
