"""Problem Description
 
 

Given a number A, find all prime numbers up to A (A included).
Make sure the returned array is sorted."""

import math


class Solution:
    # @param A : integer
    # @return a list of integers
    def is_prime(self, number):
        if number <= 1:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(number)) + 1, 2):
            if number % i == 0:
                return False
        return True

    def sieve(self, A):
        primes = [num for num in range(2, A + 1) if self.is_prime(num)]
        return sorted(primes)


s = Solution()
A = 100
print(s.sieve(A))
