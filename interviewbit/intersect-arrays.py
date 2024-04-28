'''
Find the intersection of two sorted arrays OR in other words, given 2 sorted arrays, find all the elements which occur in both arrays.

NOTE: For the purpose of this problem ( as also conveyed by the sample case ), assume that elements that appear more than once in both arrays should be included multiple times in the final output.
'''
class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return a list of integers
	def intersect(self, A, B):
		i, j = 0, 0
		result = []
		while i < len(A) and j < len(B):
			if A[i] < B[j]:
				i += 1
			elif A[i] > B[j]:
				j += 1
			else:  # arr1[i] == arr2[j]
				result.append(A[i])
				i += 1
				j += 1
		return result

s = Solution()
A= [1 ,2, 3, 3, 4, 5, 6]
B= [3, 3, 5]
print(s.intersect(A,B)) # [3, 3, 5]