import math
# Round the float value to it's nearest integer value

# Ans: if the float value is positive then add 0.5 and floor it.
# if the float value is negative then subtract 0.5 and ceil it.


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        val = A/200
        if val > 0:
            val += 0.5
            return math.floor(val)
        elif val < 0:
            val -= 0.5
            return math.ceil(val)
        else:
            return 0


s = Solution()
print(s.solve(-650))
