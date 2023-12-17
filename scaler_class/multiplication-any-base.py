class Solution:
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

    # @param A : integer - base
    # @param B : integer - value 1
    # @param C : integer - value 2
    # @return an integer - return value in base A
    def AnyBaseMultiplication(self, A, B, C):
        num1 = Solution.baseX_to_decimal(B, A)
        num2 = Solution.baseX_to_decimal(C, A)
        multi = num1 * num2
        result = Solution.decimal_to_baseX(multi, A)
        return result


s = Solution()
A = 3
B = 11
C = 10

print(s.AnyBaseMultiplication(A, B, C))
