''' Problem Description
 
 

Given a string A, find the frequency of all the characters in it.'''


class Solution:
    # @param A : string
    # @return a list of integers
    def solve(self, A):
        frequency_table = {}
        s = "abcdefghijklmnopqrstuvwxyz"
        for ch in s:
            frequency_table[ch] = 0
        for ch in A:
            frequency_table[ch] = frequency_table.get(ch) + 1
        chars = []
        for ch in frequency_table.keys():
            chars.append(frequency_table[ch])
        return chars


s = Solution()
A = "abcdefghijklmnopqrstuvwxyz"
# output: {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
print(s.solve(A))

A = "interviewbit"
# output {0, 1, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 2, 0, 1, 1, 0, 0, 0}
print(s.solve(A))
