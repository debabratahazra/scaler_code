# https://www.scaler.com/academy/mentee-dashboard/class/159481/assignment/problems/27546

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def FrequencyOfDigit(self, A, B):
        count = 0
        while A > 0:
            digit = A % 10
            if digit == B:
                count += 1
            A = A // 10
        return count


s = Solution()
A = 122312232
B = 2
print(s.FrequencyOfDigit(A, B))
