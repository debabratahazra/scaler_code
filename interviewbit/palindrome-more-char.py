def min_insertions(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]

    # Initialize diagonal with 0s
    for i in range(n):
        dp[i][i] = 0

    # Fill rest of the table in bottom up manner
    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i+cl-1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])
    for row in dp:
        print(row)
    return dp[0][n-1]


s = "banana"
print(min_insertions(s))


###########

def min_insertions_begining_2(s):
    count = 0
    s = s[::-1]
    if s == s[::-1]:
        return count

    # Find the longest common suffix of the reversed string and the original string
    for i in range(len(s)):
        text = s[i:]
        rev_text = text[::-1]
        if text == rev_text:
            break
        else:
            count += 1

    return count


s = "banana"
print(min_insertions_begining_2(s))   # expect 5
s = "AACECAAAA"
print(min_insertions_begining_2(s))   # expect 2
s = "aaaaa"
print(min_insertions_begining_2(s))   # expect 0
s = "hqghumeaylnlfdxfi"
print(min_insertions_begining_2(s))   # expect 16


# Best solution #############

class Solution:
    # @param A : string
    # @return an integer
    def create_lps(self, A):
        M = len(A)
        lps = [None]*M
        l = 0
        lps[0] = l
        i = 1

        while i < M:
            if A[i] == A[l]:
                l += 1
                lps[i] = l
                i += 1
            else:
                if l != 0:
                    l = lps[l-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def solve(self, A):
        lps = self.create_lps(A+"$"+A[::-1])
        return len(A)-lps[-1]


sol = Solution()

s = "banana"
print(sol.solve(s))   # expect 5
s = "AACECAAAA"
print(sol.solve(s))   # expect 2
s = "aaaaa"
print(sol.solve(s))   # expect 0
s = "hqghumeaylnlfdxfi"
print(sol.solve(s))   # expect 16
