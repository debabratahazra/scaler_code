import math


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        # find the count of division factor of A
        """ 
        # Time complexity is more this one

        count = 1
        range_val = (A // 2) + 1
        for i in range(1, range_val, 1):
            if A % i == 0:
                print(i)
                count += 1
        print(count)
        return count """

        count = 0
        root = (int)(math.sqrt(A))
        print("Root value:", root)
        for i in range(1, root + 1):
            print(i)
            if A % i == 0:
                if i * i == A:
                    # print(i)
                    count += 1
                else:
                    # print(i)
                    count += 2
        print(count)
        return count


sol = Solution()
val = int(input("Enter the number: "))
Solution.solve(sol, val)
