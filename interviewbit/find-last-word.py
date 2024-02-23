''' Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Please make sure you try to solve this problem without using library functions. Make sure you only traverse the string once. '''


class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        # trim the string
        A = A.strip()
        # reverse the string
        rev_str = A[::-1]
        ret_str = ""
        for ch in rev_str:
            if not ch.isspace():
                # if not space add characters
                ret_str += ch
            elif ch.isspace():
                # if space found, terminate and return with reverse order
                return ret_str[::-1]
            # if only one word present, return also in reverse order
        return ret_str[::-1]


s = Solution()
A = " hello world "
print(s.lengthOfLastWord(A))
