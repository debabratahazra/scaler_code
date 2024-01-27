'''Problem Description
 
 

Given a string A consisting of only characters 'a' and 'b'.
Divide the string into substrings of length B.
Find the subtring with maximum count of 'a' and return the count.

Note: If the length of the string is not a multiple of B and there are some characters left in the end consider them also as a substring.

Explanation 1: (baab)
The subtrings are "ba" and "ab".
Both have count of 'a' equal to 1.

Explanation 2: (bba)

The substrings are "bb" and "a".
"a" has the highest count which is 1. '''


class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        sub_str = [A[i:i + B] for i in range(0, len(A), B)]
        max_count = 0
        for s in sub_str:
            max_count = max(max_count, s.count('a'))
        return max_count


s = Solution()
A = "baab"
B = 2
print(s.solve(A, B))

A = "bba"
B = 2
print(s.solve(A, B))
