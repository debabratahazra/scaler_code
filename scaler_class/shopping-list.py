# https://www.scaler.com/academy/mentee-dashboard/class/159481/assignment/problems/14306/?navref=cl_pb_nv_tb

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer

    def shoppingList(self, A, B):
        m = len(A)
        n = len(B)
        curr = [0 for i in range(m)]
        cnt = 0
        ans = n+1
        tot = 0
        l = 0
        for i in range(m):
            tot += A[i]
            if A[i] == 0:
                cnt += 1
        for i in range(n):
            w = B[i]-1
            curr[w] += 1
            if curr[w] == A[w]:
                cnt += 1
            while cnt == m:
                ans = min(ans, i-l+1-tot)
                w = B[l]-1
                curr[w] -= 1
                if curr[w] == A[w] - 1:
                    cnt -= 1
                l += 1
        if ans > n:
            return -1
        else:
            return ans


s = Solution()
A = [1, 2]
B = [2, 1, 2, 1, 1, 2, 1, 1]
print(s.shoppingList(A, B))

A = [2, 1]
B = [1, 2, 2, 2, 2, 1]
print(s.shoppingList(A, B))
