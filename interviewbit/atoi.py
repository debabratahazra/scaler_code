''' Implement atoi to convert a string to an integer.

Example :

Input : "9 2704"
Output : 9
Note: There might be multiple corner cases here. Clarify all your doubts using “See Expected Output”.

Questions:

Q1. Does string contain whitespace characters before the number?

A. Yes

Q2. Can the string have garbage characters after the number?

A. Yes. Ignore it.

Q3. If no numeric character is found before encountering garbage characters, what should I do?

A. Return 0.

Q4. What if the integer overflows?

A. Return INT_MAX if the number is positive, INT_MIN otherwise.

Warning : DO NOT USE LIBRARY FUNCTION FOR ATOI. '''

import sys


class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):

        trim_str = A.strip()
        num_str = ""

        # check negative
        if trim_str[0] == '-':
            negative = True
            trim_str = trim_str[1:]
        elif trim_str[0] == '+':
            negative = False
            trim_str = trim_str[1:]
        else:
            negative = False

        for ch in trim_str:
            if ch.isdigit():
                num_str += ch
            else:
                break
        if len(num_str) == 0:
            return 0

        result = 0
        for i in range(len(num_str)):
            result = result * 10 + (ord(num_str[i]) - ord('0'))

        min_int = -sys.maxsize - 1
        max_int = sys.maxsize

        if negative:
            result = result * -1

        if not negative and result >= max_int:
            result = max_int
        elif not negative and result < max_int:
            return result
        if negative and result <= min_int:
            result = min_int
        elif negative and result < min_int:
            return result

        return result


s = Solution()
A = " -999923454546565654766574675465475678587584574656545465445756785765465654654746756754654654746756767890 sdsafd "
print(s.atoi(A))

A = "5121478262 8070067M75 X199R 547 8C0A11 93I630 4P4071 029W433619 M3 5 14703818 776366059B9O43393"
print(s.atoi(A))
