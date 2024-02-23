"""Problem Description

You are given an integer N and the task is to reverse the digits of the given integer. Return 0 if the result overflows and does not fit in a 32 bit signed integer


Look at the example for clarification."""


class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        # Initialize reverse number as  0
        num = A
        rev = 0
        # Check sign of the number
        sign = -1 if num < 0 else 1
        # Take absolute value of the number
        num = abs(num)
        # Reverse the digits
        while num != 0:
            # Get the last digit
            rem = num % 10
            # Remove the last digit from the number
            num //= 10
            # Check if the reverse number will overflow  32-bit integer
            if rev > 2**31 // 10 or (rev == 2**31 // 10 and rem > 7):
                return 0
            # Check if the reverse number will underflow  32-bit integer
            if rev < -(2**31) // 10 or (rev == -(2**31) // 10 and rem < -8):
                return 0
            # Update the reverse number
            rev = rev * 10 + rem
        # Return the reverse number with the original sign
        return sign * rev


s = Solution()
A = 123
print(s.reverse(A))
