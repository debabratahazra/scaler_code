'''
Write a function that takes an integer and returns the number of 1 bits it has.'''

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        count = 0
        while A:
            count += A & 1
            A >>= 1
        return count

s = Solution()
A = 11
print(s.numSetBits(A))  # expected: 3 (11 -> 1101)