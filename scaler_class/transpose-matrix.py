# https://www.scaler.com/academy/mentee-dashboard/class/159479/homework/problems/11615?navref=cl_tt_nv

# convert row element of 2d matrix to column wise and column element move to row wise position

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        transpose = []
        for col in range(len(A[0])):
            column = []
            for row in range(len(A)):
                print(row, col)
                column.append(A[row][col])
            transpose.append(column)
        return transpose


s = Solution()

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(s.solve(A))
