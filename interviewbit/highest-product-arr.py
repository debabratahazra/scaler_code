'''
Given an array A, of N integers A.
Return the highest product possible by multiplying 3 numbers from the array.
NOTE: The solution will fit in a 32-bit signed integer.
'''

class Solution:
	# @param A : list of integers
	# @return an integer
    def maxp3(self, A):
        nums = A
        nums.sort()
		
		# The array length  
        n = len(nums)
		
		# Case 1: Product of the three largest numbers
        product1 = nums[n - 1] * nums[n - 2] * nums[n - 3]
		
		# Case 2: Product of two smallest numbers and the largest number
        product2 = nums[0] * nums[1] * nums[n - 1]
		
		# Return the maximum of the two cases
        return max(product1, product2)
    
s = Solution()
A=[1,2,3,4,5,6]
print(s.maxp3(A))  # Output: 120

	
