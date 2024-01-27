'''
Given the array of strings A, you need to find the longest string S which is the prefix of
ALL the strings in the array.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is 
the prefix of both S1 and S2.

For Example: longest common prefix of "abcdefgh" and "abcefgh" is "abc".
'''

import os


class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        common_prefix = ""
        for string in A:
            if common_prefix == "":
                common_prefix = string
                continue
            else:
                common_prefix = os.path.commonprefix([common_prefix, string])
        return common_prefix


s = Solution()
A = ["abcdefgh", "abcefgh"]
print(s.longestCommonPrefix(A))

A = ["abcdefgh", "aefghijk", "abcefgh"]
print(s.longestCommonPrefix(A))

A = ["abab", "ab", "abcd"]
print(s.longestCommonPrefix(A))
