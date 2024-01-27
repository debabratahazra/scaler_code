'''Problem Description
 
 

Given a string A consisting of lowercase characters.

Check if characters of the given string can be rearranged to form a palindrome.

Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.'''


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        dic = {}
        for ch in A:
            if dic.get(ch) == None:
                dic[ch] = 1
            else:
                old = dic.get(ch)
                old += 1
                dic[ch] = old
        allow = False
        for key in dic.keys():
            if dic[key] % 2 == 0:
                continue
            else:
                if not allow:
                    allow = True
                else:
                    return 0
        return 1


s = Solution()
A = "abcde"
print(s.solve(A))

A = "abbaee"
print(s.solve(A))

A = "abbaeefg"
print(s.solve(A))
