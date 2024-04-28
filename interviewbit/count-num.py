'''
Given a sorted array of integers, find the number of occurrences of a given target value.

Your algorithm’s runtime complexity must be in the order of O(log n).
'''

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
    def findCount(self, A, B):
        def findFirst(A, B):
            low, high = 0, len(A) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if A[mid] == B and (mid == 0 or A[mid - 1] < B):
                    return mid
                elif A[mid] < B:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
        
        def findLast(A, B):
            low, high = 0, len(A) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if A[mid] == B and (mid == len(A) - 1 or A[mid + 1] > B):
                    return mid
                elif A[mid] > B:
                    high = mid - 1
                else:
                    low = mid + 1
            return -1
        
        first = findFirst(A, B)
        last = findLast(A, B)
        if first == -1 or last == -1:
            return 0
        return last - first + 1

s = Solution()
A = [1, 2, 3, 4, 5, 5, 5, 5, 6, 7]
B = 5
print(s.findCount(A, B))    # expected: 4