'''
Suppose a sorted array A is rotated at some pivot unknown to you beforehand.

(i.e., 1 2 4 5 6 7 might become 4 5 6 7 1 2).

Find the minimum element.

The array will not contain duplicates.

Note:- Use the circular rotated property of the array to solve the problem'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        low, high = 0, len(A) - 1
        while low <= high:
            if A[low] <= A[high]:
                return A[low]
            mid = low + (high - low) // 2
            next = (mid + 1) % len(A)
            prev = (mid + len(A) - 1) % len(A)
            if A[mid] <= A[next] and A[mid] <= A[prev]:
                return A[mid]
            elif A[mid] <= A[high]:
                high = mid - 1
            elif A[mid] >= A[low]:
                low = mid + 1
        return -1

s = Solution()
A = [7, 2, 4, 5]
print(s.findMin(A)) # expected: 2