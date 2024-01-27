class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        find = -1
        for i in range(len(A)):
            if A[i] == B[0] and len(A[i:]) >= len(B):
                find = i
                for ind in range(len(B)):
                    if A[i+ind] == B[ind] and len(B) == ind + 1:
                        return find
                    elif A[i+ind] == B[ind]:
                        continue
                    else:
                        find = -1
                        break
        return find


s = Solution()
A = "bbaabbbbbaabbaabbbbbbabbbabaabbbabbabbbbababbbabbabaaababbbaabaaaba"
B = "babaaa"
index = s.strStr(A, B)
print(index)
