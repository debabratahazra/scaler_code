"""Problem Description
 
 

Given a number A, find all factors of A."""


class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        factors = []
        i = 1
        while i * i <= A:
            if A % i:
                i += 1
            else:
                factors.append(i)
                if i != A // i:
                    factors.append(A // i)
                i += 1
        return sorted(factors)


s = Solution()
A = 12345
print(s.allFactors(A))
