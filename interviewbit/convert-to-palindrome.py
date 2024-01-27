''' Problem Description

Given a string A consisting only of lowercase characters, we need to check whether it is possible to make this string a palindrome after removing exactly one character from this.

If it is possible then return 1 else return 0.'''


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        for i in range(len(A)):
            sub_A = A[:i] + A[i+1:]
            rev_A = sub_A[::-1]
            if rev_A == sub_A:
                return 1
        return 0


# Python program to check whether it is possible to make
# string palindrome by removing one character

# Utility method to check if substring from
# low to high is palindrome or not.
def isPalindrome(string: str, low: int, high: int) -> bool:
    while low < high:
        if string[low] != string[high]:
            return False
        low += 1
        high -= 1
    return True


def possiblepalinByRemovingOneChar(string: str) -> int:

    # Initialize low and right by
    # both the ends of the string
    low = 0
    high = len(string) - 1

    # loop untill low and high cross each other
    while low < high:

        # If both characters are equal then
        # move both pointer towards end
        if string[low] == string[high]:
            low += 1
            high -= 1
        else:

            # If removing str[low] makes the whole string palindrome.
            # We basically check if substring str[low+1..high] is
            # palindrome or not.
            if isPalindrome(string, low + 1, high):
                return 1

            # If removing str[high] makes the whole string palindrome
            # We basically check if substring str[low+1..high] is
            # palindrome or not
            if isPalindrome(string, low, high - 1):
                return 1
            return 0

    # We reach here when complete string will be palindrome
    # if complete string is palindrome then we can remove mid character
    return 1


class Solution2:
    # @param A : string
    # @return an integer
    def solve_good(self, A):
        return possiblepalinByRemovingOneChar(A)


s = Solution()
A = "abcba"
print(s.solve(A))

A = "abecbea"
print(s.solve(A))
