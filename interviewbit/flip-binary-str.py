'''Problem Description

You are given an numeric string A which only contains 0's and 1's. You have to find a range, such that if we flip all the elements within the range, we will get largest substring of contiguous 1's.

Return the length of largest substring of contiguous 1's after flipping exactly one substring.

NOTE:

Given string always contains atleast one zero.'''

from itertools import groupby


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        res = ["".join(group) for ele, group in groupby(A)]
        length = 0
        max_lengh = 0
        for index in range(len(res)):
            if res[index].startswith("0"):
                length = len(res[index])
                if index - 1 >= 0:
                    # check prev index
                    length += len(res[index - 1])
                if index + 1 <= len(res)-1:
                    # check next index
                    length += len(res[index+1])
            max_lengh = max(length, max_lengh)
        return max_lengh


s = Solution()
A = "000"
print(s.solve(A))

A = "110001100"
print(s.solve(A))

A = "10010"
print(s.solve(A))
