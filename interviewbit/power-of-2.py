''' Problem Description
 
 

Find if the given number is a power of 2 or not. More specifically, find if the given number can be 
expressed as 2^k where k >= 1.
Note: The number length can be more than 64, which means the number can be greater than 2 ^ 64 
(out of long long range) '''


class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        A_int = int(A)
        if A_int < 2:
            return 0
        while A_int >= 2:
            if A_int % 2 == 0:
                A_int = A_int // 2
                continue
            else:
                return 0
        return 1


s = Solution()

A = "128"
print(s.power(A))

A = "147573952589676412928"
print(s.power(A))

A = "20077000522611464285"
print(s.power(A))
