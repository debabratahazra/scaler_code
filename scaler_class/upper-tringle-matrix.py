# Upper Triangular Matrix, where A[i,j]=0 where j<i

# https://www.scaler.com/academy/mentee-dashboard/class/159479/homework/problems/11471?navref=cl_tt_nv


class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != 0 and j < i:
                    return 0

        return 1


s = Solution()
A = [
    [1, 2, 3, 4],
    [0, 2, 3, 4],
    [0, 0, 3, 4],
    [0, 0, 0, 4]
]

print(s.solve(A))
