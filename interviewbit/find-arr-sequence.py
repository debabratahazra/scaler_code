'''
Given an array of non negative integers A, and a range (B, C), 

find the number of continuous subsequences in the array which have sum S in the range [B, C] or B <= S <= C

Continuous subsequence is defined as all the numbers A[i], A[i + 1], .... A[j]

where 0 <= i <= j < size(A)

Example :

A : [10, 5, 1, 0, 2]
(B, C) : (6, 8)
ans = 3 
'''

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @param C : integer
	# @return an integer
    def numRange(self, A, B, C):
        count = 0
        for i in range(len(A)):
            current_sum = 0
            for j in range(i, len(A)):
                current_sum += A[j]
                if B <= current_sum <= C:
                    count += 1
                # Since we are dealing with non-negative integers, if the sum has exceeded 'C',
                # it cannot fall back into the range [B, C] on adding more non-negative numbers.
                # We can break the inner loop here.
                elif current_sum > C:
                    break
        return count

s = Solution()
A = [10, 5, 1, 0, 2]
B = 6
C = 8
print(s.numRange(A,B,C)) # 3