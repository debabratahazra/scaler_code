'''
Given an array of integers A, every element appears twice except for one. Find that single one.'''

class Solution:
	# @param A : tuple of integers
	# @return an integer
    def singleNumber(self, A):
        result = 0
        for num in A:
            result ^= num
        return result

s = Solution()
A = [1, 2, 2, 3, 1]
print(s.singleNumber(A)) # expected: 3