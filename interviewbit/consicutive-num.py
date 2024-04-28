'''
Given an array of integers, find two numbers such that they add up to a specific target number.
'''

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
    def twoSum(self, A, B):
        hash_map = {}
        for i, num in enumerate(A):
            complement = B - num
            if complement in hash_map:
                return [hash_map[complement]+1, i+1]
            elif num not in hash_map:
                hash_map[num] = i        
        return []

s = Solution()
A = [ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ]
B = -3

print(s.twoSum(A,B)) # [4,8]

A = [ 10, -3, 5, -7, -4, 5, 6, -7, 8, -5, 8, 0, 8, -5, -10, -1, 1, -6, 4, -1, -2, -2, 10, -2, -4, -7, 5, 1, 7, -10, 0, 5, 8, 6, -8, 8, -8, -8, 3, -9, -10, -5, -5, -10, 10, -4, 8, 0, -6, -2, 3, 7, -5, 5, 1, -7, 0, -5, 1, -3, 10, -4, -3, 3, 3, 5, 1, -2, -6, 3, -4, 10, -10, -3, -8, 2, -2, -3, 0, 10, -6, -8, -10, 6, 7, 0, 3, 9, -10, -7, 8, -7, -7 ]
B = -2
print(s.twoSum(A,B)) # [3,4]
