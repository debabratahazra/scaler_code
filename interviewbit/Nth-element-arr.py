'''
Find the Bth smallest element in an unsorted array of non-negative integers A.
Definition of kth smallest element: The kth smallest element is the minimum possible n such that there are at least k elements in the array <= n.
In other words, if the array A was sorted, then Ak - 1

NOTE: You are not allowed to modify the array (The array is read-only). Try to do it using constant extra space.

The Bth will be in the sorted array of A. This need to find it from unsorted array A.
'''

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
    def kthsmallest(self, A, B):
        left, right = 0, 2**31 - 1
        while left <= right:
            mid = (left + right) // 2
            count = 0
            for num in A:
                if num <= mid:
                    count += 1
            if count < B:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
s = Solution()
A = [2, 1, 4, 3, 2]
B = 3
print(s.kthsmallest(A,B))
