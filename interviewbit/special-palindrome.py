'''
Given a string, determine if it is a palindrome. While checking for a palindrome, you have to ignore spaces, case, and all special characters; i.e. consider only alphanumeric characters.

Check the sample test case for reference.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''


class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        filter_str = ""
        for ch in A:
            if ch.isalnum():
                filter_str += ch.lower()
        rever_str = filter_str[::-1]
        if rever_str == filter_str:
            return 1
        else:
            return 0


s = Solution()
A = "A man, a plan, a canal: Panama"
print(s.isPalindrome(A))

A = "race a car"
print(s.isPalindrome(A))
