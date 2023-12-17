# find the diff bet

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        min = float('inf')
        max = float('-inf')
        for i in A:
            if i > max:
                max = i
            if i < min:
                min = i

        return max-min


s = Solution()
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
value = s.solve(A)
print(value)
