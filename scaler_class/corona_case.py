class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        # A is recover case in a day
        # B is new case in a day
        # C is existing case in a day

        day = 1
        while True:
            curr = C + B - A
            if curr <= 0:
                return day
            day += 1
            C = curr


s = Solution()
day = s.solve(4, 3, 2)
print(day)
