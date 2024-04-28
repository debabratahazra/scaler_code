'''
Given an integer A.

Compute and return the square root of A.

If A is not a perfect square, return floor(sqrt(A)).

DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY.

NOTE: Do not use sort function from standard library. Users are expected to solve this in O(log(A)) time.'''

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A == 0 or A == 1:
            return A

        start = 1
        end = A

        while start <= end:
            mid = (start + end) // 2

            if mid * mid == A:
                return mid

            if mid * mid < A:
                start = mid + 1
                ans = mid
            else:
                end = mid - 1

        return ans

s = Solution()
A = 100
print(s.sqrt(A))    # expected: 10