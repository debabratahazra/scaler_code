'''Problem Description
 
 

Given a string A consisting of lowercase characters.

You have to find the number of substrings in A which starts with vowel and end with consonants or vice-versa.

Return the count of substring modulo 109 + 7.'''


class Solution:
    # Proper solution
    def solve_good(self, A):
        vow_presum = [0]*len(A)
        cons_presum = [0]*len(A)
        vow = 0
        cons = 0
        for i, ch in enumerate(A):

            if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
                vow += 1
            else:
                cons += 1

            vow_presum[i] = vow
            cons_presum[i] = cons

        s = 0
        for i, ch in enumerate(A):

            if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
                s += cons_presum[-1]-cons_presum[i]
            else:
                s += vow_presum[-1]-vow_presum[i]

        return s % (10**9 + 7)

    # @param A : string
    # @return an integer

    def solve(self, A):
        count = 0
        vowel = ['a', 'e', 'i', 'o', 'u']
        if len(A) <= 1:
            return count
        for i in range(len(A)):
            for j in range(i+1, len(A)+1):
                sub_str = A[i:j]
                if len(sub_str) <= 1:
                    continue
                if sub_str[0] in vowel and sub_str[-1] not in vowel:
                    count += 1
                elif sub_str[0] not in vowel and sub_str[-1] in vowel:
                    count += 1
        return count


s = Solution()
A = "aba"
print(s.solve(A))

A = "a"
print(s.solve(A))
