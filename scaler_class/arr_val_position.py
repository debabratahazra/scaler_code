'''
arr [1,2,3]

Here in index 0, value is 1. So retuRn array where arr index of 1 is 0
'''


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        B = A.copy()
        for i in range(len(A)):
            index = A[i]
            value = i
            B[index] = value
        print(B)


s = Solution()
A = [9, 11, 0, 4, 13, 8, 6, 7, 5, 14, 3, 1, 2, 10, 12]
s.solve(A)

# ans: [2 11 12 10 3 8 6 7 5 0 13 1 14 4 9]
