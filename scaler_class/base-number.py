# https://www.scaler.com/academy/mentee-dashboard/class/159481/assignment/problems/27569?navref=cl_tt_nv

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def AnyBaseAddition(self, A, B, C):
        base = A
        decimal_num1 = Solution.baseX_to_decimal(B, base)
        decimal_num2 = Solution.baseX_to_decimal(C, base)

        decimal_sum = decimal_num1 + decimal_num2
        base3_value = Solution.decimal_to_baseX(decimal_sum, base)

        return base3_value

    def decimal_to_baseX(decimal_num, base):
        if decimal_num == 0:
            return '0'
        digits = []
        while decimal_num:
            decimal_num, remainder = divmod(decimal_num, base)
            digits.append(str(remainder))
        return ''.join(digits[::-1])

    def baseX_to_decimal(number, base):
        decimal = 0
        power = 0
        while number > 0:
            digit = number % 10
            decimal += digit * (base ** power)
            number //= 10
            power += 1
        return decimal


s = Solution()
A = 4
B = 22
C = 121

print(s.AnyBaseAddition(A, B, C))
