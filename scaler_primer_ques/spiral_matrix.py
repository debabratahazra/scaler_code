# https://www.scaler.com/academy/mentee-dashboard/class/7327/assignment/problems/63

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):

        array2d = [[0 for _ in range(A)] for _ in range(A)]

        sum = 1
        count = A - 1
        i, j = 0, 0
        while True:
            while j < count:
                array2d[i][j] = sum
                sum = sum + 1
                j = j + 1

            if sum >= A*A:
                array2d[i][j] = sum
                break

            while i < count:
                array2d[i][j] = sum
                sum = sum + 1
                i = i + 1

            if sum >= A*A:
                array2d[i][j] = sum
                break

            while j > A-1-count:
                array2d[i][j] = sum
                sum = sum + 1
                j = j - 1

            if sum >= A*A:
                array2d[i][j] = sum
                break

            while i > A-1-count:
                array2d[i][j] = sum
                sum = sum + 1
                i = i - 1

            i = i + 1
            j = j + 1
            count = count - 1
            if sum >= A*A:
                array2d[i][j] = sum
                break

        return array2d


s = Solution()
return_val = s.generateMatrix(5)

for i in range(5):
    print(return_val[i])
