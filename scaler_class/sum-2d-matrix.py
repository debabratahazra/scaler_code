# https://www.scaler.com/academy/mentee-dashboard/class/159479/homework/problems/11617?navref=cl_tt_nv
# sum of each row element and each column element

class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        sum = []
        # Addition for each row element
        for i in range(len(A)):
            total = 0
            for j in range(len(A[0])):
                print(i, j)
                total += A[i][j]
            sum.append(total)

        print()

        # Addition for each column element
        for col in range(len(A[0])):
            total = 0
            for row in range(len(A)):
                print(row, col)
                total += A[row][col]
            sum.append(total)

        return sum


s = Solution()
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(s.solve(A))
