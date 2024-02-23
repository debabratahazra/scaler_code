''' Given a string A of size N, find and return the longest palindromic substring in A.

Substring of string A is A[i...j] where 0 <= i <= j < len(A)

Palindrome string:

A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.

Incase of conflict, return the substring which occurs first ( with the least starting index).
'''


class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        input_string = A
        n = len(input_string)
        table = [[False]*n for _ in range(n)]
        maxLength = 1
        start = 0
        for i in range(n):
            table[i][i] = True
        for cl in range(2, n+1):
            for i in range(n - cl + 1):
                j = i + cl - 1
                if input_string[i] == input_string[j]:
                    if cl == 2:
                        table[i][j] = True
                    elif table[i+1][j-1]:
                        table[i][j] = True
                if table[i][j] and cl > maxLength:
                    start = i
                    maxLength = cl
        return input_string[start:start + maxLength]

    def longest_palindrome(self, s):
        # Preprocess the string to handle even length palindrome
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n-1):
            if R > i:
                P[i] = min(R-i, P[2*C-i])
            while T[i+1+P[i]] == T[i-1-P[i]]:
                P[i] += 1
                if i+P[i] > R:
                    C, R = i, i+P[i]
        # here consider the last occurrence of the palindrome
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))

        # consider only the first occurrence of palindrome
        centerIndex = P.index(maxLen)
        return s[(centerIndex - maxLen)//2: (centerIndex + maxLen)//2]


s = Solution()
A = "aaaabaaa"
print(s.longestPalindrome(A))

# optimized way
A = "abbcccbbbcaaccbababcbcabca"
print(s.longest_palindrome(A))
