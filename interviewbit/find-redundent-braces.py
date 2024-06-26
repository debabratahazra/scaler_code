'''
Given a string A denoting an expression. It contains the following operators '+', '-', '*', '/'.

Chech whether A has redundant braces or not.

NOTE: A will be always a valid expression.'''

class Solution:
	# @param A : string
	# @return an integer
    def braces(self, A):
        stack = []

        for char in A:
            if char in "*/+-":
                stack.append(char)
            elif char == "(":
                stack.append(char)
            elif char == ")":
                if stack[-1] == "(":
                    # This means we encountered a pair of braces with no operator in between
                    return 1
                while stack[-1] != "(":
                    # Pop all operators until we find the matching '('
                    stack.pop()
                stack.pop()  # Pop the '(' itself

        return 0
    
s = Solution()
A = "((a+b))"
print(s.braces(A)) # 1

A = "(a+(a+b))"
print(s.braces(A)) # 0

A = "((a*b)+(c+d))"
print(s.braces(A)) # 0
