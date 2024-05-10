'''
Given a sorted array A and a target value B, return the index if the target is found. If not, 
return the index where it would be if it were inserted in order.'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) // 2

            if A[mid] == B:
                return mid
            elif A[mid] < B:
                left = mid + 1
            else:
                right = mid - 1
        return left

s = Solution()
A = [1, 3, 5, 6]
B = 5
print(s.searchInsert(A, B)) # expected: 2