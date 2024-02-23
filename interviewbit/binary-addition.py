''' Problem Description
 
 

Given two binary strings A and B. Return their sum (also a binary string).


Problem Constraints
1 <= length of A <= 105

1 <= length of B <= 105

A and B are binary strings '''


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        a = int(A, 2)
        b = int(B, 2)
        print(a, b)
        return bin(a+b)[2:]


s = Solution()
A = "11010101"
B = "111100111"
print(s.addBinary(A, B))
