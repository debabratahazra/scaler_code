'''
Problem Description
 
 

You are given a string A, and you have to find all the amazing substrings of A.
An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).
Note: Take the mod of the answer with 10003.
'''


from collections import OrderedDict


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        char_list = ['a', 'e', 'i', 'o', 'u']
        count = 0
        for index in range(len(A)):
            if (A[index]).lower() in char_list:
                count += len(A[index:])
                continue
        return count % 10003


s = Solution()
A = "ABEC"
print(s.solve(A))
