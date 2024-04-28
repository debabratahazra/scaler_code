'''
Implement pow(x, n) % d.
In other words, given x, n and d,
Find (xn % d)
Note that remainders on division cannot be negative. In other words, make sure the answer you return is non-negative integer.'''

class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if n == 0:
            return 1 % d
        if n == 1:
            return x % d
        temp = self.pow(x, n // 2, d)
        if n % 2 == 0:
            return (temp * temp) % d
        else:
            return (x * temp * temp) % d

s = Solution()
print(s.pow(2,3,3)) # expected: 2