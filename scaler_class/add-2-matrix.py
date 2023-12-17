class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        sum = []
        for i in range(len(A)):
            total = []
            for j in range(len(A[0])):
                val = A[i][j] + B[i][j]
                total.append(val)
            sum.append(total)

        return sum


s = Solution()
A = [
    [1, 2,],
    [3, 4]
]

B = [
    [6, 9,],
    [5, 2]
]

sumMatrix = s.solve(A, B)
print(sumMatrix)
