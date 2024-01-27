'''Given a string A of parantheses  ‘(‘ or ‘)’.

The task is to find minimum number of parentheses ‘(‘ or ‘)’ (at any positions) we must add to make the resulting parentheses string valid.

An string is valid if:

Open brackets must be closed by the corresponding closing bracket.
Open brackets must be closed in the correct order.'''


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        open_par = 0
        count = 0
        for ch in A:
            if ch == '(':
                open_par += 1
            if ch == ')':
                if open_par > 0:
                    open_par -= 1
                else:
                    count += 1

        if open_par < 0:
            return count + (open_par * -1)
        else:
            return count + open_par

        # Function to return required
        # minimum number
        def minParentheses(p):

            # maintain balance of string
            bal = 0
            ans = 0
            for i in range(0, len(p)):
                if (p[i] == '('):
                    bal += 1
                else:
                    bal += -1

                # It is guaranteed bal >= -1
                if (bal == -1):
                    ans += 1
                    bal += 1
            return bal+ans


s = Solution()
A = "())"
print(s.solve(A))

A = "((("
print(s.solve(A))

A = ")("
print(s.solve(A))
