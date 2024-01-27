''' Problem Description
 
 

You are given a string A of size N.

 

Return the string A after reversing the string word by word.

NOTE:

A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.
  '''

import re


class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        # strip string
        A = A.strip()

        # split string with space
        split_A = re.split('\s+', A)
        new_string = ""
        for i in range(len(split_A)-1, -1, -1):
            new_string += split_A[i] + " "

        return new_string.strip()


s = Solution()
A = "    this    is a string   with many words  "
print(s.solve(A))
