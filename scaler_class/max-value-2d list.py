# find the max value from each row in 2d list

class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        maxList = []
        for row in A:
            maxVal = float('-inf')
            for elem in row:
                if maxVal < elem:
                    maxVal = elem
            maxList.append(maxVal)

        return maxList


s = Solution()
A = [
    [1, 2, 3, 0, 2, 7, 2],
    [4, 5, 2]
]
print(s.solve(A))
